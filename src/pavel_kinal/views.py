from django.shortcuts import render_to_response
from django.core.urlresolvers import resolve

from pavel_kinal.music.models import Album


def main_context(request, context=None):
    if context is None:
        context = {}

    menu_items = [
        {"name": "Music", "url_name": "music"},
        {"name": "Video", "url_name": "video"},
        {"name": "Gear", "url_name": "gear"},
        {"name": "Tab", "url_name": "tab"},
        {"name": "Bio", "url_name": "bio"},
        {"name": "Photo", "url_name": "photo"},
        {"name": "Merch", "url_name": "merch"},
        {"name": "Tuning", "url_name": "tuning"},
        {"name": "Contact", "url_name": "contact"},
    ]
    context.update({
        "menu_items": menu_items,
        "current_url_name": resolve(request.path_info).url_name
    })
    return context


def layout(request, template):
    return render_to_response("layout/{}.html".format(template), context=main_context(request))


def index(request):
    return render_to_response("index.html", context=main_context(request))


def music(request):
    context = {
        "albums": Album.objects.all().order_by("-datetime")
    }
    return render_to_response("music.html", context=main_context(request, context))


def empty(request):
    return render_to_response("empty.html", context=main_context(request))
