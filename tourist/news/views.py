from django.shortcuts import render, get_object_or_404
from .models import News
from attraction.models import Rank
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin



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
    rank = Rank.objects.filter(rank_type="ระดับประเทศ")[:6]
    #detail = TouristAttraction.objects.get(id=id)
    context = {
        'detail': detail,
        'rank':rank
        }
    return render(request, 'news/news_detail.html', context)
