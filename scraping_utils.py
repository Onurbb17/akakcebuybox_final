import requests
from bs4 import BeautifulSoup
import time
import random
from urllib.parse import urljoin, urlparse

def akakce_fiyat_cek(url):
    """
    Akakçe'den fiyat bilgilerini Requests ile çeker
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        # Random delay to avoid being blocked
        time.sleep(random.uniform(1, 3))
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Ürün adını çek
        urun_adi = ""
        h1_tag = soup.find('h1')
        if h1_tag:
            urun_adi = h1_tag.get_text(strip=True)
        
        # Fiyat bilgilerini çek
        fiyat = ""
        magaza = ""
        
        # Akakçe'nin fiyat listesi CSS selectors
        fiyat_selectors = [
            'ul#PL li a.iC.xt_v8 .pt_v8',
            '.price-list .price-item .price',
            '.product-price .price-value',
            '.price-box .price',
            '[data-price]'
        ]
        
        magaza_selectors = [
            'ul#PL li a.iC.xt_v8 .v_v8',
            '.price-list .price-item .store',
            '.product-price .store-name',
            '.price-box .store',
            '[data-store]'
        ]
        
        # Fiyat çekmeyi dene
        for selector in fiyat_selectors:
            fiyat_element = soup.select_one(selector)
            if fiyat_element:
                fiyat = fiyat_element.get_text(strip=True)
                break
        
        # Mağaza çekmeyi dene
        for selector in magaza_selectors:
            magaza_element = soup.select_one(selector)
            if magaza_element:
                magaza = magaza_element.get_text(strip=True)
                break
        
        # Fallback: Genel fiyat arama
        if not fiyat:
            price_patterns = soup.find_all(text=lambda text: text and '₺' in text)
            if price_patterns:
                fiyat = price_patterns[0].strip()
        
        return {
            'urun_adi': urun_adi or "Ürün adı bulunamadı",
            'fiyat': fiyat or "Fiyat bulunamadı", 
            'magaza': magaza or "Mağaza bulunamadı",
            'success': True
        }
        
    except requests.RequestException as e:
        return {
            'urun_adi': "Bağlantı hatası",
            'fiyat': "Fiyat alınamadı",
            'magaza': "Mağaza bilgisi yok",
            'success': False,
            'error': str(e)
        }
    except Exception as e:
        return {
            'urun_adi': "Parsing hatası", 
            'fiyat': "Fiyat çekilemedi",
            'magaza': "Mağaza bulunamadı",
            'success': False,
            'error': str(e)
        }

def site_fiyat_cek(url):
    """
    Kullanıcının kendi sitesinden fiyat çeker
    """
    if not url:
        return "Site linki yok"
        
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    try:
        time.sleep(random.uniform(0.5, 1.5))
        
        response = requests.get(url, headers=headers, timeout=8)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Yaygın fiyat CSS selectors
        fiyat_selectors = [
            '.product-price-new',
            '.price',
            '.product-price',
            '.current-price',
            '.sale-price',
            '.price-current',
            '[data-price]',
            '.amount',
            '.cost'
        ]
        
        for selector in fiyat_selectors:
            fiyat_element = soup.select_one(selector)
            if fiyat_element:
                return fiyat_element.get_text(strip=True)
        
        # Fallback: ₺ içeren text ara
        price_patterns = soup.find_all(text=lambda text: text and '₺' in text)
        if price_patterns:
            return price_patterns[0].strip()
            
        return "Fiyat bulunamadı"
        
    except Exception as e:
        return f"Hata: {str(e)[:50]}"

def fiyat_farki_hesapla(akakce_fiyat, site_fiyat):
    """
    İki fiyat arasındaki farkı hesaplar
    """
    try:
        # Fiyatları temizle ve sayıya çevir
        akakce_clean = ''.join(filter(str.isdigit, str(akakce_fiyat).replace(',', '.')))
        site_clean = ''.join(filter(str.isdigit, str(site_fiyat).replace(',', '.')))
        
        if akakce_clean and site_clean:
            af = float(akakce_clean) / 100  # Kuruş to TL
            sf = float(site_clean) / 100
            return round(sf - af, 2)
        
        return ""
    except:
        return ""

