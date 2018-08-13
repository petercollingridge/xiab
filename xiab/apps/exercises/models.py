from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel


class Question(models.Model):
    question = RichTextField()
    answer = models.CharField(max_length=255)

    panels = [
        FieldPanel('question'),
        FieldPanel('answer'),
    ]

    class Meta:
        abstract = True


class ExercisePageQuestions(Orderable, Question):
    page = ParentalKey('ExercisePage', on_delete=models.CASCADE, related_name='questions')


class ExercisePage(Page):
    summary = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('summary'),
        InlinePanel('questions', label="Questions"),
    ]

    def get_context(self, request):
        context = super(ExercisePage, self).get_context(request)
        context["prev_lesson"] = self.get_prev_siblings().live().first()
        context["next_lesson"] = self.get_next_siblings().live().first()
        print(context)
        return context
