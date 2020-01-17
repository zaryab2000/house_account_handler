from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages



@login_required
def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date')
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

@login_required
def data_entry_form(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, f'Item Added To The DataBase')
		return redirect('total_expanse')

	context={
		'form':form
	}

	return render(request, 'blog/forms.html', context)
@login_required
def total_expanse(request):
	data = Post.objects.all().order_by('-date')
	total = Post.objects.all().aggregate(Sum('price'))
	context={
		'datas':data,
		'total':total['price__sum']
	}

	return render(request, 'users/total_expanse.html', context)

@login_required
def delete_record(request, post_id):
	post = Post.objects.get(pk = post_id)
	post.delete()
	messages.info(request, f'Selected Record has been Deleted')
	return redirect('total_expanse')


