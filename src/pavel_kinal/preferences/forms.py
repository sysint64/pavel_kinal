from django.template import loader

from pavel_kinal.preferences.models import Language
from django import forms
from django.db import models


class LanguagesSelectInput(forms.Widget):
    class Media:
        css = {
            'all': (
                'admin/css/flags.css',
                'admin/css/widgets.css',
            )
        }

    def render(self, name, value, attrs=None):
        context = {
            "languages": Language.objects.all(),
            "active_code": "ru",
            "blanks": [],
        }

        template = loader.get_template('admin/widgets/language_select_input.html')
        return template.render(context)


class LanguageInput(forms.Widget):
    class Media:
        css = {
            'all': (
                'admin/css/flags.css',
                'admin/css/widgets.css',
            )
        }

        js = ('admin/js/languages.js',)

    def render(self, name, value, attrs=None):
        if value is None:
            language = ""
        else:
            language = value

        context = {
            "name": name,
            "value": value,
            "language": language,
        }

        template = loader.get_template('admin/widgets/language_input.html')
        return template.render(context)


class LanguageChoiceField(forms.ModelChoiceField):
    def __init__(self, **kwargs):
        kwargs.update({"widget": LanguageInput})
        super().__init__(**kwargs)


class LanguageField(models.ForeignKey):
    description = "LanguageField"

    def formfield(self, **kwargs):
        kwargs.update({'form_class': LanguageChoiceField})
        return super().formfield(**kwargs)


class MultiLanguageAdminForm(forms.ModelForm):
    lang = forms.ModelChoiceField(Language.objects.all(), label="Язык",
                                  required=False, widget=LanguagesSelectInput)
