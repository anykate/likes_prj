from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'core/index.html', {})


class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['andya'] = 'sanjeevani'
        return context

    def post(self, request):
        cnt = request.POST.get('button_text')
        response_text = f"{cnt}"
        if request.is_ajax():
            return JsonResponse({'response_text': response_text}, status=200)
