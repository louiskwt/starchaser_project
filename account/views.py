from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Member
from django.urls import reverse
from .forms import LoginForm, UserRegistrationForm, MemberForm
from django.contrib import messages
from django.shortcuts import get_object_or_404

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, '歡迎回來👏')
                    return HttpResponseRedirect(reverse('case'))
                else:
                    messages.error(request, '用户名/密碼不正確')
            else:
                messages.error(request, '用户名/密碼不正確')
    else:
        form = LoginForm()
    
    return render(request, 'registration/login.html', {'form': form}) 

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Member.objects.create(user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse('setup'))
        else:
            return render(request, 'registration/register.html', {'form': user_form})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': user_form})


@login_required
def setup(request):
    radio_fields = ['gender', 'subject', 'active', 'role', 'referral']
    if request.method == "POST":
        set_up_form = MemberForm(instance=request.user.member, data=request.POST)
        if set_up_form.is_valid():
            set_up_form.save(commit=True)
            messages.success(request, '註冊完成，歡迎你加入 StarChaser')
            return HttpResponseRedirect(reverse('case'))
    else:
        set_up_form = MemberForm()

    return render(request, 'registration/register_profile.html', {
        "form": set_up_form,
        "radio_fields": radio_fields
    })

@login_required
def edit(request):
    if request.method == "POST":
        profile_form = MemberForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(reverse('case'))
    else:
        profile_form = MemberForm()
    
    
    return render(request, 'registration/register_profile.html.html')



def logout_user(request):
    logout(request)
    messages.success(request, '登出成功~希望好快會再見👋')
    return HttpResponseRedirect(reverse('home'))


def case_list(request):
    cases = Member.objects.all().filter(active='Y')
    print(cases)

    context = {
        'cases': cases
    }

    return render(request, 'case.html', context=context)


def case_detail_view(request, slug):
    case = get_object_or_404(Member, id=slug)
    context = {"case": case}
    return render(request, "case_detail.html", context)