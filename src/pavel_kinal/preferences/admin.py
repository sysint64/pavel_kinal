from django import forms
from django.contrib import admin
from django.utils.html import format_html
from singlemodeladmin import SingleModelAdmin

from pavel_kinal.preferences.forms import LanguagesSelectInput, LanguageInput, \
    MultiLanguageAdminForm
from pavel_kinal.preferences.models import Preferences, Languages, Language, PreferencesTranslation


# Languages
class StackedLanguageInline(admin.StackedInline):
    template = "admin/widgets/language_tabular_inline.html"


class TabularLanguageInline(admin.TabularInline):
    template = "admin/widgets/language_tabular_inline.html"


class SingleLanguageInline(admin.TabularInline):
    template = "admin/widgets/language_single_inline.html"


class LanguageInline(admin.TabularInline):
    model = Language
    fields = ('country_code', 'country_name',)
    extra = 1


class LanguagesAdmin(SingleModelAdmin):
    inlines = [LanguageInline]


class LanguageListDisplayMixin:
    form = MultiLanguageAdminForm

    def languages(self, item):
        exist_language_style = """
            background: #e3e3e3;
            color: #555;
            display: inline-block;
            padding: 6px 7px;
            margin: 3px;
            border-radius: 10px;
        """

        empty_language_style = exist_language_style + """
            opacity: 0.5;
        """

        languages_html = ""

        for language in Language.objects.all():
            style = empty_language_style

            if item.translations.filter(language=language).count() > 0:
                style = exist_language_style

            languages_html += "<div class='lang' style='" + style + "'>" + \
                              language.country_code.upper() + \
                              "</div>"

        return format_html(languages_html)

    languages.allow_html = True
    languages.short_description = "Языки"


# Preferences
class PreferencesAdminForm(forms.ModelForm):
    class Meta:
        model = Preferences
        fields = '__all__'

    lang = forms.ModelChoiceField(Language.objects.all(), label="Язык",
                                  required=False, widget=LanguagesSelectInput)


class PreferencesAdminTranslationForm(forms.ModelForm):
    class Meta:
        model = PreferencesTranslation
        fields = '__all__'

    language = forms.ModelChoiceField(Language.objects.all(), label="Язык",
                                      required=True, widget=LanguageInput)


class TranslationInline(SingleLanguageInline):
    model = PreferencesTranslation
    extra = 0
    form  = PreferencesAdminTranslationForm
    max_num = 999


class PreferencesAdmin(SingleModelAdmin):
    # list_display = ('title', 'sport',)
    # list_filter = ['sport',]
    inlines = [TranslationInline]
    form = PreferencesAdminForm


admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Preferences, PreferencesAdmin)
