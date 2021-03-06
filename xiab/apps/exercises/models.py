from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel


class MultipleChoiceQuestionBlock(blocks.StructBlock):
    """ A multiple choice question. """

    question = blocks.RichTextBlock()
    answers = blocks.ListBlock(blocks.CharBlock(label="Answer choice"))
    correct_answer = blocks.IntegerBlock(required=True, help_text="Index of the correct answer (starting at 0)")

    class Meta:
        icon = 'list-ul'
        label = 'Multiple choice'


class NumericQuestionBlock(blocks.StructBlock):
    """ A question that expects an numeric answer. """
    
    question = blocks.RichTextBlock()
    answer = blocks.FloatBlock()

    class Meta:
        icon = 'help'
        label = 'Numeric'


class ExercisePage(Page):
    """Uses a streamfield to build a series of questions."""

    summary = RichTextField(blank=True)

    questions = StreamField([
        ('numeric', NumericQuestionBlock()),
        ('multiple_choice', MultipleChoiceQuestionBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('summary'),
        StreamFieldPanel('questions'),
    ]

    def get_context(self, request):
        context = super(ExercisePage, self).get_context(request)
        context["prev_lesson"] = self.get_prev_siblings().live().first()
        context["next_lesson"] = self.get_next_siblings().live().first()
        return context
