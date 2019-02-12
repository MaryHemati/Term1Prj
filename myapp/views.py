import os
import datetime

from random import randint
from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.core.files.storage import default_storage
from PIL import Image, ExifTags
from django.shortcuts import render_to_response



pic = None
# Create your views here.
def hello(request) :
    print (request.FILES)
    return render (request, 'view1.html',)


def upload(request) :
    global pic 
    date = str(datetime.datetime.now())
    pic = default_storage.save( date + 'file' + '.jpg',request.FILES['fileToUpload'])
    return redirect("/")


def Display(request) :
    context = {'image': pic }
    return render (request, 'upload.html', context)

#-------------------------------------------------------------------------------------------    
def blackwhite(request) :
    global pic
    color_image = Image.open('media/' + pic) 
    bw = color_image.convert('L')
    bw.save('media/' + pic) 
    context = {'image': pic }
    return render (request, 'upload.html', context)


def rotate(request) :
    global pic
    try:
        Img = Image.open('media/' + pic)
        rotated_Img = Img.rotate(int(request.POST.get('degree')), expand = 1)
        rotated_Img.save('media/' + pic)
        context = {'image': pic }
        return render (request, 'upload.html', context)
    except:
        return HttpResponse ('input error for rotate')  


def resize(request) :
    global pic
    try:
        length = request.POST['length']
        width = request.POST['width']
        photo = Image.open('media/' + pic)
        if ((int(length) == 0) or (int(width) == 0)) :
            new_size = photo.resize((int(length), int(width)))
            new_size.save('media/' + pic)
            context = {'image': pic }
            return render (request, 'upload.html', context)
    except:
        return HttpResponse('input error for resize')  


def crop(request) :
    global pic
    try:
        first = request.POST['first'] #first=x1,second=y1 , third=x2,forth=y2 --> x2>x1 , y2>y1
        second = request.POST['second']
        third = request.POST['third']
        forth = request.POST['forth']
        x1 = int(first)
        y1 = int(second)
        x2 = int(third)
        y2 = int(forth)

        if (x1 <= x2 or y1 <= y2) :
            photo = Image.open('media/' + pic)
            croped_pic = photo.crop((x1, y1, x2, y2))
            croped_pic.save('media/' + pic)
            context = {'image': pic }
            return render (request, 'upload.html', context)
        else:
            return HttpResponse('input error for crop' )  
    except:
        return HttpResponse('input error for crop')  


#--------------------

def shared(request) :
    edited_photo = Image.open('media/' + pic)
    edited_photo.save('shared/' + pic)
    context = {'image': pic }
    return render(request, 'upload.html', context)


def show_shared_photos(request) :
    path = '/home/maman_maryam/mysite/shared/'
    list_of_imgs = os.listdir(path)
    list_of_imgs.sort()
    return render_to_response ('share.html', {'images' : list_of_imgs})   


    






    
 