from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect

from .forms import CustomerUserCreationForm
from .models import Notice


def home(request):
    return render(request, 'main.html')


def signup(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')
    else:
        form = CustomerUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def signup_success(request):
    return render(request, 'accounts/signup_success.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get('next') or 'home'
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('home')


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')


@login_required
def password_change_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
            return redirect('profile')
        messages.error(request, '입력 정보를 다시 한 번 확인해 주세요.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/passowrd_change.html', {'form': form})


@login_required
def session_info_view(request):
    context = {
        'session_key': request.session.session_key,
        'expiry_age': request.session.get_expiry_age(),
        'expiry_date': request.session.get_expiry_date(),
        'session_data': dict(request.session.items()),
    }
    return render(request, 'accounts/session_info.html', context)


@login_required
def notice_list_view(request):
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'accounts/notice_list.html', {'notices': notices})


@login_required
@permission_required('accounts.can_publish_notice', raise_exception=True)
def notice_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        if title and content:
            Notice.objects.create(title=title, content=content)
            messages.success(request, '공지사항이 등록되었습니다.')
            return redirect('notice_list')
        messages.error(request, '제목과 내용을 모두 입력해 주세요.')
    return render(request, 'accounts/notice_create.html')
