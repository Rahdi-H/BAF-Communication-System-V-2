from django.shortcuts import render, redirect
from .models import LOS, Acknowledgement, CRPT
from .admin import LOSResouce, CRPTResouce
from .forms import LoginForm, LOSForm, CRPTForm
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
import datetime
from django.db.models import Q

# Create your views here.

@login_required(login_url='/login/')
def home(request):
    if request.method == 'POST':
        if 'download_report' in request.POST:
            month = request.POST['month']
            type = request.POST['type']
            if type == 'IN LOS':
                messages = LOS.objects.filter(Q(datetime_of_action__icontains=month) & Q(receiver_unit = request.user.id)).order_by('-id')
                dateset = LOSResouce().export(messages)
            elif type == 'OUT LOS':
                messages = LOS.objects.filter(Q(datetime_of_action__icontains=month) & Q(sender = request.user.id)).order_by('-id')
                dateset = LOSResouce().export(messages)
            elif type == "IN CRPT":
                messages = CRPT.objects.filter(Q(datetime_of_action__icontains=month) & Q(receiver_unit = request.user.id)).order_by('-id')
                dateset = CRPTResouce().export(messages)
            elif type == 'OUT CRPT':
                messages = CRPT.objects.filter(Q(datetime_of_action__icontains=month) & Q(sender = request.user.id)).order_by('-id')
                dateset = CRPTResouce().export(messages)
            
            ds = dateset.xls
            response = HttpResponse(ds, content_type="xls")
            response['Content-Disposition'] = "attachment; filename=msg.xls"
            return response
    context= {

    }
    return render(request, 'unit/home.html', context)

def loginn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        messages.warning(request, "Username or Password didn't matched")
        return render(request, 'unit/login.html')
    else:
        form = LoginForm()
        return render(request, 'unit/login.html', {'form':form})

@login_required(login_url='/login/') 
def logoutt(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login/')
def in_los(request):
    if request.method == 'POST':
        if 'received_ack' in request.POST:
            time = request.POST.get('time_of_rec')
            date = request.POST.get('date_of_rec')
            ref = request.POST.get('ref')
            user = request.user
            ack = Acknowledgement(date=date, time=time, ref=ref, user=user)
            ack.save()
            los = LOS.objects.get(ref=ref)
            los.received_by.add(ack)
            los.save()
        if 'dispa' in request.POST:
            dispathced = request.POST.get('dispatched')
            id = request.POST.get('id')
            los = LOS.objects.get(id = id)
            los.dispatched = True
            los.save()
    if request.method == 'GET':
        if 'month' in request.GET:
            month = request.GET.get('month')
            print('This is Month : ', month)
            messages = LOS.objects.filter(Q(datetime_of_action__icontains=month) & Q(receiver_unit = request.user.id)).order_by('-id')
            lenn = len(messages)
            context = {
                'messages' : messages,
                'lenn' : lenn,
                'month' : month
            }
            return render(request, 'unit/in_los.html', context)
        
    current_month = datetime.datetime.now().strftime('%Y-%m')
    print(current_month)
    messages = LOS.objects.filter(Q(datetime_of_action__icontains=current_month) & Q(receiver_unit = request.user.id)).order_by('-id')
    lenn = len(messages)
    context = {
        'messages' : messages,
        'lenn' : lenn,
        'month' : current_month,
        }
    return render(request, 'unit/in_los.html', context)

@login_required(login_url='/login/')
def in_crpt(request):
    if request.method == 'POST':
        if 'received_ack' in request.POST:
            time = request.POST.get('time_of_rec')
            date = request.POST.get('date_of_rec')
            ref = request.POST.get('ref')
            user = request.user
            ack = Acknowledgement(date=date, time=time, ref=ref, user=user)
            ack.save()
            los = CRPT.objects.get(ref=ref)
            los.received_by.add(ack)
            los.save()
        if 'dispa' in request.POST:
            dispathced = request.POST.get('dispatched')
            id = request.POST.get('id')
            los = CRPT.objects.get(id = id)
            los.dispatched = True
            los.save()
    if request.method == 'GET':
        if 'month' in request.GET:
            month = request.GET.get('month')
            print('This is Month : ', month)
            messages = CRPT.objects.filter(Q(datetime_of_action__icontains=month) & Q(receiver_unit = request.user.id)).order_by('-id')
            lenn = len(messages)
            context = {
                'messages' : messages,
                'lenn' : lenn,
                'month' : month
            }
            return render(request, 'unit/in_crpt.html', context)

    current_month = datetime.datetime.now().strftime('%Y-%m')
    messages = CRPT.objects.filter(Q(datetime_of_action__icontains=current_month) & Q(receiver_unit = request.user.id)).order_by('-id')
    lenn = len(messages)
    context = {
        'messages' : messages,
        'lenn' : lenn,
        'month' : current_month
    }
    return render(request, 'unit/in_crpt.html', context)

@login_required(login_url='/login/')
def out_los(request):
    if request.method == 'GET':
        if 'month' in request.GET:
            month = request.GET.get('month')
            print('This is Month : ', month)
            messages = LOS.objects.filter(Q(datetime_of_action__icontains=month) & Q(sender = request.user.id)).order_by('-id')
            lenn = len(messages)
            context = {
                'messages' : messages,
                'lenn' : lenn,
                'month' : month
            }
            return render(request, 'unit/out_los.html', context)
    current_month = datetime.datetime.now().strftime('%Y-%m')
    messages = LOS.objects.filter(Q(datetime_of_action__icontains=current_month) & Q(sender = request.user.id)).order_by('-id')
    context = {
        'messages':messages,
        'month' : current_month
    }
    return render(request, 'unit/out_los.html', context)

@login_required(login_url='/login/')
def out_crpt(request):
    if request.method == 'GET':
        if 'month' in request.GET:
            month = request.GET.get('month')
            print('This is Month : ', month)
            messages = CRPT.objects.filter(Q(datetime_of_action__icontains=month) & Q(sender = request.user.id)).order_by('-id')
            lenn = len(messages)
            context = {
                'messages' : messages,
                'lenn' : lenn,
                'month' : month
            }
            return render(request, 'unit/out_crpt.html', context)
    current_month = datetime.datetime.now().strftime('%Y-%m')
    messages = CRPT.objects.filter(Q(datetime_of_action__icontains=current_month) & Q(sender = request.user.id)).order_by('-id')
    context = {
        'messages':messages,
        'month' : current_month
    }
    return render(request, 'unit/out_crpt.html', context)

# @login_required(login_url='/login/')
# def los_add(request):
#     if request.method == 'POST':
#         form = LOSForm(request.POST)
#         if form.is_valid:
#             instance = form.save(commit=False)
#             instance.sender = request.user
#             instance.save()
#             messages.success(request, 'Successfully saved & sent the message')
#             return redirect('los-add')
#         else:
#             messages.warning(request, 'Something went wrong please try again')
#             return redirect('los-add')
#     else:
#         form = LOSForm()
#         context = {
#             'form':form,
#         }
#         return render(request, 'unit/los_add.html', context)

class LosCreateView(CreateView):
    model = LOS
    form_class = LOSForm
    template_name = 'unit/los_add.html'
    success_url = '/out-los/add'   

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.sender = self.request.user
        instance.save()
        return super().form_valid(form)

class CrptCreateView(CreateView):
    model = CRPT
    form_class = CRPTForm
    template_name = 'unit/crpt_add.html'
    success_url = '/out-crpt/add'   

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.sender = self.request.user
        instance.save()
        return super().form_valid(form)
    
class LosUpdateView(UpdateView):
    model = LOS
    form_class = LOSForm
    template_name = 'unit/los_update.html'
    success_url = '/out-los/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.sender = self.request.user
        instance.save()
        return super().form_valid(form)

class CrptUpdateView(UpdateView):
    model = CRPT
    form_class = CRPTForm
    template_name = 'unit/crpt_update.html'
    success_url = '/out-crpt/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.sender = self.request.user
        instance.save()
        return super().form_valid(form)