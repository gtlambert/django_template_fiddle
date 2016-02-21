import json

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.template import Context, Template
from django.views.generic import CreateView, UpdateView

from .models import Fiddle
from .forms import FiddleForm


class FiddleView(UpdateView):
    fiddle = None
    template_name = 'base.html'
    form_class = FiddleForm
    model = Fiddle
    pk_url_kwarg = 'fiddle_id'

    def get_success_url(self):
        return reverse('fiddle-view', kwargs={'fiddle_id': self.object.id})

    def get_fiddle(self):
        if not self.fiddle:
            self.fiddle = get_object_or_404(Fiddle, pk=self.kwargs['fiddle_id'])
        return self.fiddle

    def get_context_data(self, **kwargs):
        context = super(FiddleView, self).get_context_data(**kwargs)
        fiddle = self.get_fiddle()
        fiddle_template = Template(fiddle.template)
        fiddle_context = Context(json.loads(fiddle.context))
        fiddle_template = fiddle_template.render(fiddle_context)
        context['fiddle_template'] = fiddle_template
        return context


fiddle_view = FiddleView.as_view()
