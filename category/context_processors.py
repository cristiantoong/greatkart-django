from .models import Category

def menu_links(request):
  links = Category.objects.all()
  #convert object to dictionary
  print(dict(links=links))
  
  return dict(links=links)#{'links': <QuerySet [<Category: Shirts>, <Category: T Shirt>, <Category: Shoes>, <Category: Pants>, <Category: Jacket>]>}