from django.contrib import admin
from .models import Blog,Category
from django.utils.safestring import mark_safe

class BlogAdmin(admin.ModelAdmin): ## Ekstra özellikler eklenecek
  ##list_display=("title","is_active","is_home","slug",) 32 videoda çoklu kategori listeleme işleminde değştirdik.
    list_display=("title","is_active","is_home","slug","selected_categories",)
    list_editable=("is_active","is_home",)
    search_fields=("title","description",)
    readonly_fields=("slug",)
   ## list_filter=("category","is_active","is_home")     31 manytoone değişince burası değişti.                                                )
    # readonly_fields=("description") istenen alanı sadece okunabilir yapıyoruz.
    list_filter=("is_active","is_home")

    def selected_categories(self,obj):
        html="<ul>"

        for category in obj.categories.all():
            html+="<li>"+category.name+" "+"</li>"

        html+="</ul>"
        return mark_safe(html) # 32 videoda çoklu kategori işlemleri
    
class CategoryAdmin(admin.ModelAdmin):
    list_display=("name","slug",)
    readonly_fields=("slug",)
    search_fields=("name",)


admin.site.register(Blog,BlogAdmin)## Genişlemeden sonra buraya kullanacağımız model için sınıf adını çağırıyoruz.
admin.site.register(Category,CategoryAdmin)

# Register your models here.
