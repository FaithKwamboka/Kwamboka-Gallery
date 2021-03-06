from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    images = Image.objects.all()
    location = Location.objects.all()
    category = categories.objects.all()

    if 'location' in request.GET and request.GET['location']:
        location = request.GET.get('location')
        images = Image.view_location(location)

    elif 'category' in request.GET and request.GET['category']:
        cate = request.GET.get('categories')
        images = Image.view_category(category)
        return render(request, 'all-gallery/all-pics.html', {"location":location,"images":images,"cate":cate })

    return render(request,"all-gallery/all-pics.html",{"images":images,"location":location,"category":category})

def search_results(request):

    if 'categories' in request.GET and request.GET['categories']:
        search_images = request.GET.get("categories")
        searched_images = Image.search_by_category(search_images)
        message = f"{search_images}"

        return render(request, 'all-gallery/search.html',{"message":message,"images": searched_images})

    else:
        message = ""
        return render(request, 'all-gallery/search.html',{"message":message})

def get_image_by_id(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-gallery/pics.html", {"image":image})
