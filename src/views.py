from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse


class LayoutView(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=[response_kwargs.get("template")],
            context=context,
            using=self.template_engine,
        )

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        template = "layout/{}.html".format(kwargs.get("template"))
        return self.render_to_response(context, template=template)
