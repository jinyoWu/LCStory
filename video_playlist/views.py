from django.shortcuts import render
from django.http import HttpResponse

from .models import voluntary_video, mandatory_video
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os

# Create your views here.
NUMBER_IN_ONE_PAGE = 4



def homepage(request):
    return render(request, 'playlist/homepage.html')


def voluntary_playlist(request):
    query_voluntary_objs = voluntary_video.objects.all()
    
    titles,poster_img,videos = [],[],[]
    for voluntary_obj in query_voluntary_objs : 
        titles.append(voluntary_obj.title)
        poster_img.append(voluntary_obj.cover_img)
        video_name = (voluntary_obj.video.url).split("/")[-1]
        videos.append(video_name)


    data = list(zip(poster_img, titles, videos))
    page = request.GET.get('page', 1)
    paginator = Paginator(data, NUMBER_IN_ONE_PAGE)
    try:
        data_in_page = paginator.page(page)
    except PageNotAnInteger:
        data_in_page = paginator.page(1)
    except EmptyPage:
        data_in_page = paginator.page(paginator.num_pages)

    content = {
        'video_data': data_in_page,
    }

    return render(request, 'playlist/voluntary_playlist.html', content)


def mandatory_playlist(request):
    query_mandatory_objs = mandatory_video.objects.all()
    
    titles,poster_img,videos = [],[],[]
    for mandatory_obj in query_mandatory_objs : 
        titles.append(mandatory_obj.title)
        poster_img.append(mandatory_obj.cover_img)
        tail = (mandatory_obj.video.url).split("/")[-1]
        videos.append(tail)


    data = list(zip(poster_img, titles, videos))
    page = request.GET.get('page', 1)
    paginator = Paginator(data, NUMBER_IN_ONE_PAGE)
    try:
        data_in_page = paginator.page(page)
    except PageNotAnInteger:
        data_in_page = paginator.page(1)
    except EmptyPage:
        data_in_page = paginator.page(paginator.num_pages)

    content = {
        'video_data': data_in_page,
    }
    return render(request, 'playlist/mandatory_playlist.html', content)


def video_view(request, video):
    content = {'video_src': "/media/videos/"+video,}
    return render(request, 'playlist/video_view.html', content)

