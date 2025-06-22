from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Kategori(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kategoriler")
    isim = models.CharField(max_length=100)
    olusturma_zamani = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.isim

    class Meta:
        verbose_name_plural = "Kategoriler"

class Eslesme(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name="eslesmeler")
    akakce_link = models.URLField(max_length=500)
    site_link = models.URLField(max_length=500, blank=True, null=True)
    olusturma_zamani = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.kategori.isim} - {self.akakce_link[:50]}"

    class Meta:
        verbose_name_plural = "Eşleşmeler"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    default_category_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    class Meta:
        verbose_name_plural = "Kullanıcı Profilleri"

class Bildirim(models.Model):
    NOTIFICATION_TYPES = [
        ('info', 'Bilgi'),
        ('success', 'Başarılı'),
        ('warning', 'Uyarı'),
        ('error', 'Hata'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bildirimler")
    mesaj = models.TextField()
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES, default='info')
    okundu = models.BooleanField(default=False)
    olusturma_zamani = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mesaj[:50]}"

    class Meta:
        verbose_name_plural = "Bildirimler"
        ordering = ['-olusturma_zamani']

class BlogKategori(models.Model):
    isim = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    aciklama = models.TextField(blank=True)
    olusturma_zamani = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.isim)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.isim

    class Meta:
        verbose_name_plural = "Blog Kategorileri"

class BlogYazisi(models.Model):
    baslik = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    kategori = models.ForeignKey(BlogKategori, on_delete=models.CASCADE, related_name="yazilar")
    yazar = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_yazilari")
    ozet = models.TextField(max_length=300, help_text="SEO için kısa açıklama")
    icerik = models.TextField()
    kapak_resmi = models.URLField(blank=True, null=True)
    
    # SEO alanları
    meta_title = models.CharField(max_length=60, blank=True, help_text="SEO başlığı (60 karakter)")
    meta_description = models.CharField(max_length=160, blank=True, help_text="SEO açıklaması (160 karakter)")
    anahtar_kelimeler = models.CharField(max_length=200, blank=True, help_text="Virgülle ayrılmış anahtar kelimeler")
    
    # Durum ve tarihler
    yayinlandi = models.BooleanField(default=False)
    olusturma_zamani = models.DateTimeField(auto_now_add=True)
    guncelleme_zamani = models.DateTimeField(auto_now=True)
    yayin_tarihi = models.DateTimeField(null=True, blank=True)
    
    # İstatistikler
    goruntulenme_sayisi = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.baslik)
        if not self.meta_title:
            self.meta_title = self.baslik[:60]
        if not self.meta_description:
            self.meta_description = self.ozet[:160]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detay', kwargs={'slug': self.slug})

    def __str__(self):
        return self.baslik

    class Meta:
        verbose_name_plural = "Blog Yazıları"
        ordering = ['-yayin_tarihi', '-olusturma_zamani']

class BlogYorum(models.Model):
    yazi = models.ForeignKey(BlogYazisi, on_delete=models.CASCADE, related_name="yorumlar")
    isim = models.CharField(max_length=100)
    email = models.EmailField()
    icerik = models.TextField()
    onaylandi = models.BooleanField(default=False)
    olusturma_zamani = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.isim} - {self.yazi.baslik}"

    class Meta:
        verbose_name_plural = "Blog Yorumları"
        ordering = ['-olusturma_zamani']

class SSS(models.Model):
    soru = models.CharField(max_length=200)
    cevap = models.TextField()
    kategori = models.CharField(max_length=50, choices=[
        ('genel', 'Genel'),
        ('fiyat', 'Fiyat Takibi'),
        ('teknik', 'Teknik'),
        ('hesap', 'Hesap Yönetimi'),
    ], default='genel')
    sira = models.PositiveIntegerField(default=0)
    aktif = models.BooleanField(default=True)
    olusturma_zamani = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.soru

    class Meta:
        verbose_name_plural = "Sık Sorulan Sorular"
        ordering = ['kategori', 'sira']

