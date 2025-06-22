from django.urls import path
from .views import (
    home_view, register, login_view, logout_view, 
    fiyat_cek, profile, settings_view, bildirim_merkezi,
    blog_liste, blog_detay, blog_kategori, sss_view
)

urlpatterns = [
    path("", home_view, name="home"),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("fiyat-cek/", fiyat_cek, name="fiyat_cek"),
    path("ayarlar/", settings_view, name="settings"),
    path("profile/", profile, name="profile"),
    path("bildirimler/", bildirim_merkezi, name="bildirimler"),
    
    # Blog URL'leri
    path("blog/", blog_liste, name="blog_liste"),
    path("blog/kategori/<slug:kategori_slug>/", blog_kategori, name="blog_kategori"),
    path("blog/<slug:slug>/", blog_detay, name="blog_detay"),
    
    # Diğer sayfalar
    path("sss/", sss_view, name="sss"),
]

