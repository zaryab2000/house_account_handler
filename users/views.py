from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
from django.db.models import Sum
from blog.models import Post


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request, person_id):
    detail = Post.objects.filter(person_id=person_id)
    total_price = Post.objects.filter(person_id=person_id).aggregate(Sum('price'))
    context={
        "details": detail,
        "total_price": total_price['price__sum']
    }
    return render(request, 'users/profile.html',context)

@login_required
def profileupdate(request):
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, f'YOUR ACCOUNT IS NOW UPDATED SUCCESSFULLY')
            return redirect('blog-home')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context={
        'user_form':user_form,
        'profile_form':profile_form,
    }

    return render(request, 'users/profileupdate.html',context)


















