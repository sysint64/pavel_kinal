from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from pavel_kinal.preferences.models import Language


class LanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        lang_code = request.path.lstrip("/")[:2]
        Language.current = Language.objects.filter(country_code=lang_code).first()
        Language.current = Language.current or Language.objects.filter(country_code=settings.DEFAULT_LANGUAGE).first()
        request.language = Language.current
        print(lang_code)
