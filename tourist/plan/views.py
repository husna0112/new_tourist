from os.path import exists

from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from attraction.models import TouristAttraction
from plan.models import Plan, PlanTouristAttraction

from .forms import CreatePlanForm

# Create your views here.

@login_required(login_url='/login/')
def plan_list_view(request):
    # User = get_user_model()
    # j = User.objects.first()
    qs = Plan.objects.filter(user=request.user).order_by('-planed_date').values()

    #allPlans = Plan.objects.all()
    context = {'allPlan': qs}
    return render(request, 'plan/plan_list.html', context)

@login_required(login_url='/login/')
def plan_detail_view(request, plan_id):
    detail = get_object_or_404(Plan, id=plan_id)
    attractions_list = TouristAttraction.objects.all()
    plan = Plan.objects.get(pk=plan_id)


    attractions = plan.touristattractions.all()
  
    context = {
        'plan': plan,
        'attractions': attractions,
        'detail': detail,
    }
    
    return render(request, 'plan/plan_detail.html', context)

@login_required(login_url='/login/')
def plan_create_view(request):
    title = "Create"
    form = CreatePlanForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = CreatePlanForm()
        messages.success(request, 'สร้างแผนท่องเที่ยวสำเร็จ')
        return redirect('/plan')

    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'plan/plan_create.html', context)



@login_required(login_url='/login/')
def plan_update_view(request, plan_id):
    obj = get_object_or_404(Plan, id=plan_id)
    form = CreatePlanForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'อัพเดทแผนท่องเที่ยวสำเร็จ')
        return redirect("plan_detail", plan_id=plan_id)
    context = {
        'form': form,
        }
    return render(request, 'plan/plan_update.html', context)

@login_required(login_url='/login/')
def plan_delete_view(request, plan_id):
    obj = get_object_or_404(Plan, id=plan_id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'ลบแผนท่องเที่ยวสำเร็จ')
        return redirect('/plan')
    
    context = {"object": obj}
    return render(request, 'plan/plan_delete.html', context)

@login_required(login_url='/login/')
def place_delete(request, plan_id, place_id):
    plan_qs = Plan.objects.filter(id=plan_id)

    if plan_qs.exists():
        for plan in plan_qs:
            plan.touristattractions.remove(place_id)
            messages.success(request, 'ลบสถานที่ท่องเที่ยวสำเร็จ')
            return redirect("plan_detail", plan_id=plan_id)

    return redirect("plan_detail", plan_id=plan_id)


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    attractions_list = TouristAttraction.objects.all()

    query = request.GET.get('q')
    if query:
        attractions_list = attractions_list.filter(
            Q(name__icontains=query)|
            Q(address__icontains=query)).distinct()


    return attractions_list
    
def plan_add_attraction(request, plan_id):
    queryset_list = TouristAttraction.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(name__icontains=query)|
            Q(address__icontains=query)).distinct()
    paginator = Paginator(queryset_list, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'queryset': queryset_list,
        'page_obj': page_obj,
        'plan_id': plan_id
    }

    print(request.method)

    return render(request, 'plan/search_attraction.html', context)


