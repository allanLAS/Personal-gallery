import datetime as dt
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from . models import Image, Location, Category

# Create your views here.
def home(request):
    location = Location.objects.all()
    category = Category.objects.all()
    images=Image.objects.all()
    return render(request,'home.html',{"images":images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

# def pics_today(request):
#     date = dt.date.today()

    
#     return render(request, 'images.html', {"date":date,})


# def past_days_pics(request,past_date):

#     try:
#         # converts data from the string url
        
#         date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

#     except ValueError:
#         # raise 404 error when ValuError is thrown
#         raise Http404()
#         assert False

#     if date == dt.date.today():
#         return redirect(pics_today)

#     return render(request, 'images.html', {"date": date})
     