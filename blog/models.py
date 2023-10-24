from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name=models.CharField(max_length=150)
    category_img=models.ImageField(null=True,upload_to='category')
    slug=models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False) # db_index alanı hız , performans açısından önemli

    def __str__(self):
        return f"{self.name}"

    def save(self,*args, **kwargs)  : ## ana model dosyasındaki save fonksiyonu ezildi.8-11 dakika arası incelendi. (ders 22) 
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

# dosya yolu için (upload_to) blogs/1.jpeg 
class Blog(models.Model):
    title=models.CharField(max_length=200)
    ##image=models.CharField(max_length=50)  öncelikle sadece ismi saklıyoruz
    ## dilersek FileUpload ile istediğimiz uzantıda dosya saklayabilirz.
    # Şimdilik image saklayacağız.
    image=models.ImageField(upload_to="blogs")
   # descriptions=models.TextField(null=True) ## RichTextField
    descriptions=RichTextField()
    is_active=models.BooleanField(default=False)
    is_home=models.BooleanField(default=False)
    slug=models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False) # db_index alanı hız , performans açısından önemli
    ## category=models.ForeignKey(Category,default=1,on_delete=models.CASCADE) --> many to one 
    categories=models.ManyToManyField(Category,blank=True)
    # tüm kayıtlar için öncelikle giriş ve kayıt işlemi yaptık. 

    def __str__(self):
        return f"{self.title}" # listelenen kayıtlar liste şeklindeydi biz o kayıtların title ile listelenmesini sağladık.
    # kayıtları silme işlemi yapılabilir ancak default ingilizce geliyor. Türkçe için blogapp setting.ps düzeltilebilir.

    def save(self,*args, **kwargs)  : ## ana model dosyasındaki save fonksiyonu ezildi.8-11 dakika arası incelendi. (ders 22) 
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)



# abc.com/category/beyaz-esya kategorisi bu olanları getir gibi

