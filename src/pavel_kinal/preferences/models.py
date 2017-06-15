from django.conf import settings
from django.db import models


class LanguageModelManager(models.Manager):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def get_queryset(self):
        query = {
            "{}translation__language".format(self.name): Language.current
        }
        return super().get_queryset().filter(**query)


class Languages(models.Model):
    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class LanguageManager(models.Manager):
    def all_for_page(self, request):
        languages = []
        language_codes = self.values_list("country_code", flat=True)

        for language in self.all():
            filtered_path = request.path

            if filtered_path[1:3] in language_codes:
                filtered_path = filtered_path[3:]

            if language.country_code == settings.DEFAULT_LANGUAGE:
                language.permalink = filtered_path
            else:
                language.permalink = "/%s%s" % (language.country_code, filtered_path)

            print(language.permalink)
            languages.append(language)

        return languages


class Language(models.Model):
    current = None

    languages = models.ForeignKey(Languages)
    country_code = models.CharField("Код страны", max_length=4, primary_key=True)
    country_name = models.CharField("Название", max_length=255, default="")

    objects = LanguageManager()

    def __str__(self):
        return self.country_name

    @property
    def is_active(self):
        if Language.current is None:
            return False

        return Language.current.country_code == self.country_code


class MultiLanguageModelMixin(object):
    translations_set = "translations"

    def translation(self):
        manager = getattr(self, self.translations_set)
        return manager.filter(language=Language.current).first()


class Preferences(MultiLanguageModelMixin, models.Model):
    translations_set = "preferencestranslation_set"

    youtube_url = models.URLField(verbose_name="YouTube", blank=True)
    vk_url = models.URLField(verbose_name="VK", blank=True)
    fb_url = models.URLField(verbose_name="Facebook", blank=True)
    instagram_url = models.URLField(verbose_name="Instagram", blank=True)
    twitter_url = models.URLField(verbose_name="Twitter", blank=True)
    twitch_url = models.URLField(verbose_name="Twitch", blank=True)
    soundcloud_url = models.URLField(verbose_name="Soundcloud", blank=True)


class PreferencesTranslation(models.Model):
    preferences = models.ForeignKey(Preferences)
    language = models.ForeignKey(Language, verbose_name="Язык", null=True, blank=True)
