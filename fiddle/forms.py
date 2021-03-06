from django import forms

from crispy_forms_foundation.forms import FoundationModelForm

from .models import Fiddle


class FiddleForm(FoundationModelForm):

    class Meta:
        model = Fiddle
        fields = ('context', 'template',)
