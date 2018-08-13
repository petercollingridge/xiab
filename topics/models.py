from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class TopicPage(Page):
    summary = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('summary'),
    ]

    def get_context(self, request):
        # Update context to include only published posts
        context = super().get_context(request)
        context['children'] = self.get_children().live()
        return context
