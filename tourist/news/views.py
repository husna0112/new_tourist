from django.shortcuts import render, get_object_or_404
from .models import News
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import TestForm
from django.views.generic import FormView, TemplateView


def listNews(request):
    allnews = News.objects.order_by('-updated')#[:3]
    paginator = Paginator(allnews, 6) # Show 21 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj
        }
    return render(request, 'news/news.html', context)

def news_detail(request, news_id):
    detail = get_object_or_404(News, id=news_id)
    #detail = TouristAttraction.objects.get(id=id)
    return render(request, 'news/news_detail.html', context={'detail': detail})


class AjaxTemplateMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)

class TestFormView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'news/test_form.html'
    form_class = TestForm
    success_url = reverse_lazy('home')
    success_message = "Way to go!"