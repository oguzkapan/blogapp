from django.urls    import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# http://127.0.0.1:8000/            index
# http://127.0.0.1:8000/index       index
# http://127.0.0.1:8000/blogs       blog
# http://127.0.0.1:8000/blogs/3     blog-details 

urlpatterns = [
    path("",views.index,name="home"),
    path("index",views.index),
    path("blogs",views.blogs,name="blogs"),
   #path("blogs/<int:id>",views.blog_details,name="blog_details"), #BU1 buraya kadardı. BU13 name eklendi.
   # çağrı isini slug ile yapacağımızdan bu satır açıklama satırı olup aşağıdaki şekle dönüştü.
    path("blogs/<slug:slug>",views.blog_details,name="blog_details"), #BU1 buraya kadardı. BU13 name eklendi.
    path("category/<slug:slug>",views.blogs_by_category,name="blogs_by_category"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # bu satır ile resimleri ulaşılabilir hale getiriyoruz.