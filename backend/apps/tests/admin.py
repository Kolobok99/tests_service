import nested_admin
from django.contrib import admin

from .forms import OptionInlineFormset
from .models import Option, Question, Test


class OptionInline(nested_admin.NestedStackedInline):
    model = Option
    formset = OptionInlineFormset
    extra = 1


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    inlines = [OptionInline]
    extra = 1


class TestAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Test, TestAdmin)
admin.site.register(Question)
admin.site.register(Option)