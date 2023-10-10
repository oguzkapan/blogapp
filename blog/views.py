from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog,Category
# Create your views here.

## def index(request):
##    return HttpResponse("Ana sayfa") # bu aşamada bu satırlar değiştirilip render metodu ile view yollandı.

data={
     "blogs":[
          {
               "id":1,
               "title":"web geliştirme",
               "image":"1.jpg",
               "is_active":True,
               "is_home":True,
               "description":"Kendi web uygulamanızı geliştirin"
          },
          {
               "id":2,
               "title":"python geliştirme",
               "image":"2.jpg",
               "is_active":True,
               "is_home":True,
               "description":"Kendi python uygulamanızı geliştirin"
          },
          {
               "id":3,
               "title":"mobil uygulama",
               "image":"3.jpg",
               "is_active":False,
               "is_home":False,
               "description":"Kendi mobil uygulamanızı geliştirin"
          }
     ]
}


# artık listeden değil veritabanından almaya başlıyoruz. 19. bölüm 

def index(request):
    context={
         ## "blogs":data["blogs"]
         "blogs":Blog.objects.filter(is_active=True,is_home=True),
         "categories":Category.objects.all()
    }
    return render(request,"blog/index.html",context)

def blogs(request):
     context={
         # "blogs":data["blogs"]
         "blogs":Blog.objects.filter(is_active=True), ## all dersek tümü geliyor
         "categories":Category.objects.all()
          }
     return render(request,"blog/blogs.html",context)

# url değişti slug bilgisi ile çağrım yapıyoruz. o bakımdan blog_details fnk parametlerinde id yerine slug kullandık.
def blog_details(request,slug):
     '''
     blogs=data["blogs"]
     selectedBlog=None

     for blog in blogs:
          if blog["id"]==id:
               selectedBlog=blog
      
     blogs=data["blogs"]
     selectedBlog=[blog for blog in blogs if blog["id"]==id][0]      
  
     blog=Blog.objects.get(id=id)

     return render(request,"blog/blog_details.html",{
          "blog":blog
     })
     '''

     blog=Blog.objects.get(slug=slug)

     return render(request,"blog/blog_details.html",{
          "blog":blog
     })
'''
def blog_details(request,id):
    return HttpResponse("Blog Detayları : "+str(id)) #BU3 
'''

def blogs_by_category(request,slug):
     
     context={
         # "blogs":data["blogs"]
         # "blogs":Blog.objects.filter(is_active=True,category__slug=slug), ## all dersek tümü geliyor 32.videoda değişti
         "blogs":Category.objects.get(slug=slug).blog_set.filter(is_active=True),        
         "categories":Category.objects.all(),
         "selected_category":slug
          }
     return render(request,"blog/blogs.html",context)