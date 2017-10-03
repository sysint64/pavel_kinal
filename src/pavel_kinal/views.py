from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import resolve
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

from pavel_kinal.gear.models import Gear
from pavel_kinal.music.models import Album
from pavel_kinal.preferences.models import Language, Preferences
from pavel_kinal.video.models import Video


def main_context(request, lang_code=None, context=None):
    if context is None:
        context = {}

    lang_code = lang_code or settings.DEFAULT_LANGUAGE
    get_object_or_404(Language, pk=lang_code)

    translation.activate(lang_code)

    menu_items = [
        {"name": _("Music"), "url_name": "music"},
        {"name": _("Video"), "url_name": "video"},
        {"name": _("Gear"), "url_name": "gear"},
        {"name": _("Tab"), "url_name": "tab"},
        {"name": _("Bio"), "url_name": "bio"},
        {"name": _("Photo"), "url_name": "photo"},
        {"name": _("Merch"), "url_name": "merch"},
        {"name": _("Tuning"), "url_name": "tuning"},
        {"name": _("Contact"), "url_name": "contact"},
    ]
    context.update({
        "menu_items": menu_items,
        "current_url_name": resolve(request.path_info).url_name,
        "languages": Language.objects.all_for_page(request),
        "preferences": Preferences.objects.all().first(),
    })
    return context


def layout(request, template):
    return render_to_response("layout/{}.html".format(template), context=main_context(request))


def index(request):
    return render_to_response("index.html", context=main_context(request))


def music(request, lang_code=None):
    context = {
        "albums": Album.objects.all().order_by("-datetime")
    }
    return render_to_response("music.html", context=main_context(request, lang_code, context))


def video(request, lang_code=None):
    context = {
        "videos": Video.objects.all()
    }
    return render_to_response("video.html", context=main_context(request, lang_code, context))


def gear(request, lang_code=None):
    context = {
        "gears": Gear.objects.all()
    }
    return render_to_response("gear.html", context=main_context(request, lang_code, context))


def empty(request):
    return render_to_response("empty.html", context=main_context(request))
