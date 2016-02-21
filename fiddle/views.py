from django.views.generic import TemplateView

# Create your views here.
class FiddleView(TemplateView):
    template_name = 'base.html'


fiddle_view = FiddleView.as_view()
