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

