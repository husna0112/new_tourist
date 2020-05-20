from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from attraction.models import TouristAttraction
from plan.models import Plan, PlanTouristAttraction
from django import forms
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


    
