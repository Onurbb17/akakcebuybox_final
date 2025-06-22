from django.contrib import admin
from .models import UserProfile, Kategori, Eslesme, BlogYazisi, BlogKategori

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "default_category_id", "created_at", "updated_at")
    search_fields = ("user__username", "user__email")
    list_filter = ("created_at",)
    ordering = ("user",)
    readonly_fields = ("created_at", "updated_at")

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ("isim", "user")
    search_fields = ("isim", "user__username")
    list_filter = ("user",)
    ordering = ("isim",)

@admin.register(Eslesme)
class EslesmeAdmin(admin.ModelAdmin):
    list_display = ("kategori", "akakce_link", "site_link", "olusturma_zamani")
    search_fields = ("akakce_link", "site_link", "kategori__isim")
    list_filter = ("kategori",)
    ordering = ("-olusturma_zamani",)
    date_hierarchy = "olusturma_zamani"
    actions = ["kopyala_linkleri"]

    def kopyala_linkleri(self, request, queryset):
        self.message_user(request, f"{queryset.count()} eşleşmenin linkleri kopyalandı!")
    kopyala_linkleri.short_description = "Seçilen eşleşmelerin linklerini kopyala"

@admin.register(BlogYazisi)
class BlogYazisiAdmin(admin.ModelAdmin):
    list_display = ("baslik", "yayin_tarihi", "yayinlandi")
    search_fields = ("baslik", "ozet")
    list_filter = ("yayinlandi", "yayin_tarihi")
    prepopulated_fields = {"slug": ("baslik",)}

@admin.register(BlogKategori)
class BlogKategoriAdmin(admin.ModelAdmin):
    list_display = ("isim",)
    prepopulated_fields = {"slug": ("isim",)}