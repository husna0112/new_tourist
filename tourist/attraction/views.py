#from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# from news.models import News
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.context_processors import request
from django.template.loader import render_to_string
from django.utils import timezone
from attraction.models import TouristAttraction, Province, Category
from news.models import News
from plan.models import Plan, PlanTouristAttraction
from django.contrib import messages
from django.views.generic import TemplateView
# Create your views here.

def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    attractions_list = TouristAttraction.objects.all()
    province = Province.objects.all()
    category = Category.objects.all()
    
    
    province = request.GET.get('province')
    if is_valid_queryparam(province) and province != 'จังหวัด':
        attractions_list = attractions_list.filter(province__name=province)

    category = request.GET.get('category')
    if is_valid_queryparam(category) and category != 'ประเภท':
        attractions_list = attractions_list.filter(category__name=category)

    query = request.GET.get('q')
    if query:
        attractions_list = attractions_list.filter(
            Q(name__icontains=query)|
            Q(detail__icontains=query)|
            Q(address__icontains=query)).distinct()

    return attractions_list

def Home(request):
    allnews = News.objects.order_by('-updated')[:4]
    context = {'allNews': allnews}
    return render(request, 'attraction/home.html', context)



def listAttraction(request):
    attractions_list = filter(request)

    paginator = Paginator(attractions_list, 20) # Show 21 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': Category.objects.all(),
        'province': Province.objects.all()
        }

    return render(request, 'attraction/attractions.html', context)


def attraction_detail(request, attraction_id):
    detail = get_object_or_404(TouristAttraction, id=attraction_id)
    #detail = TouristAttraction.objects.get(id=id)
    context = {
        'detail': detail,
        }
    return render(request, 'attraction/detail.html', context)

def add_to_plan(request, attraction_id):
    touristattraction = get_object_or_404(TouristAttraction, id=attraction_id)
    plan_touristattraction, created = PlanTouristAttraction.objects.get_or_create(
        touristattraction=touristattraction,
        user=request.user,
        planed=False
    )
    plan_qs = Plan.objects.filter(user=request.user, planed=False)

    

    if plan_qs.exists():
        plan = plan_qs[0]
        #check if the order item is in the order
        if plan.touristattractions.filter(touristattraction__id=touristattraction.id).exists():
            plan_touristattraction.quantity += 1
            plan_touristattraction.save()
            messages.info(request, "quantity was updated")
            return redirect("detail", attraction_id=attraction_id)
        else:
            #ถ้ามี plan อยู่แล้วจะเข้าอันนี้ โดยเข้าไปที่ plan แรกของเรา
            plan.touristattractions.add(plan_touristattraction)
            messages.info(request, "was added to your plan")
            return redirect("detail", attraction_id=attraction_id)
    else:
        #เพิ่มไปยังplanที่ยังไม่ได้สร้าง
        planed_date = timezone.now()
        plan = Plan.objects.create(
            user=request.user, planed_date=planed_date)
        plan.touristattractions.add(plan_touristattraction)
        messages.info(request, "was added to your plan2")




    
    return redirect("detail", attraction_id=attraction_id)


class RatingScore(TemplateView):
    template_name = 'attraction/rating_score.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'PWPK'
        return context