# PriceSync - Fiyat Takip ve Karşılaştırma Sistemi

PriceSync, Akakçe'deki rakip fiyatlarını otomatik olarak takip eden ve kendi sitenizle karşılaştıran modern bir Django uygulamasıdır.

## 🚀 Özellikler

- **Modern UI/UX**: Profesyonel PriceSync tasarımı
- **Freemium Model**: İlk 5 ürün linki ücretsiz
- **Otomatik Fiyat Çekme**: Selenium ile Akakçe fiyat takibi
- **Excel Raporları**: Koyu tema ile formatlanmış Excel çıktıları
- **Kategori Yönetimi**: Ürünleri kategorilere ayırma
- **Bildirim Sistemi**: Kullanıcı bildirimleri
- **Responsive Tasarım**: Mobil uyumlu arayüz

## 📋 Gereksinimler

- Python 3.8+
- Django 4.2+
- Chrome/Chromium tarayıcısı
- ChromeDriver

## 🛠️ Kurulum

1. **Projeyi indirin ve çıkarın**

2. **Sanal ortam oluşturun:**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
.\venv\Scripts\activate   # Windows
```

3. **Gerekli paketleri yükleyin:**
```bash
pip install -r requirements.txt
```

4. **ChromeDriver'ı indirin:**
   - [ChromeDriver](https://chromedriver.chromium.org/) sayfasından Chrome sürümünüze uygun driver'ı indirin
   - Driver'ı PATH'e ekleyin veya proje klasörüne koyun

5. **Veritabanını oluşturun:**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Süper kullanıcı oluşturun (isteğe bağlı):**
```bash
python manage.py createsuperuser
```

7. **Sunucuyu başlatın:**
```bash
python manage.py runserver
```

## 🎯 Kullanım

1. **Kayıt Olun**: Ana sayfadan ücretsiz hesap oluşturun
2. **Kategori Ekleyin**: Ürünlerinizi organize etmek için kategoriler oluşturun
3. **Ürün Linklerini Ekleyin**: Akakçe linklerini ve kendi site linklerinizi ekleyin
4. **Fiyatları Çekin**: "Fiyatları Çek ve İndir" butonuyla Excel raporu alın

## 🔧 Yapılandırma

### Environment Variables (.env dosyası)

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
CHROMEDRIVER_PATH=/path/to/chromedriver
```

### Chrome Ayarları

Selenium için Chrome ayarları `views.py` dosyasında yapılandırılmıştır:
- Headless mode aktif
- User-agent ayarlanmış
- GPU devre dışı

## 📁 Proje Yapısı

```
akakcebuybox_final/
├── fiyat_cekici/          # Ana Django projesi
│   ├── settings.py        # Proje ayarları
│   ├── urls.py           # Ana URL yapılandırması
│   └── wsgi.py           # WSGI yapılandırması
├── fiyat_cekme/          # Ana uygulama
│   ├── models.py         # Veritabanı modelleri
│   ├── views.py          # View fonksiyonları
│   ├── urls.py           # URL yapılandırması
│   ├── forms.py          # Django formları
│   └── admin.py          # Admin panel ayarları
├── templates/            # HTML template'leri
│   ├── home.html         # Ana sayfa
│   ├── login.html        # Giriş sayfası
│   ├── register.html     # Kayıt sayfası
│   ├── fiyat_cek.html    # Fiyat çekme paneli
│   └── ...
├── static/              # Statik dosyalar
├── requirements.txt     # Python bağımlılıkları
└── manage.py           # Django yönetim scripti
```

## 🎨 Tasarım

PriceSync modern, profesyonel bir tasarıma sahiptir:
- **Renk Paleti**: Mavi-cyan gradyanları
- **Tipografi**: Inter font ailesi
- **İkonlar**: Font Awesome 6
- **Framework**: Bootstrap 5
- **Responsive**: Mobil-first yaklaşım

## 🔒 Güvenlik

- CSRF koruması aktif
- Rate limiting (10 istek/dakika)
- XSS koruması
- Güvenli session yönetimi

## 📊 Freemium Model

- **Ücretsiz**: İlk 5 ürün linki
- **Premium**: Sınırsız ürün - 75₺/ay
- Otomatik bildirimler ve uyarılar

## 🐛 Sorun Giderme

### ChromeDriver Hataları
```bash
# ChromeDriver yolunu kontrol edin
which chromedriver

# Permissions ayarlayın
chmod +x /path/to/chromedriver
```

### Selenium Hataları
- Chrome tarayıcısının güncel olduğundan emin olun
- ChromeDriver sürümünün Chrome ile uyumlu olduğunu kontrol edin

### Django Hataları
```bash
# Migrations'ları sıfırlayın
python manage.py migrate --run-syncdb

# Static dosyaları toplayın
python manage.py collectstatic
```

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit edin (`git commit -m 'Add amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📞 Destek

Herhangi bir sorun yaşarsanız:
- GitHub Issues kullanın
- E-posta: support@pricesync.com

---

**PriceSync** - Fiyatlarınızı senkronize edin, rekabette öne geçin! 🚀

