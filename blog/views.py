from django.shortcuts import render, HttpResponse, get_object_or_404
from django.utils import timezone
from.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm

# Create your views here.

def post_list(request):
	object_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	paginator=Paginator(object_list, 2)
	page=request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request,
	'post_list.html',
	{'page': page,
	'posts': posts,
	'num':range(paginator.num_pages)})

def post_detail(request, year, month, day, title):
	posts=get_object_or_404(Post, title=title, published_date__year=year, published_date__month=month, published_date__day=day)
	return render(request, 'post_detail.html', {'post':posts})

def post_share(request, post_id):
	post=get_object_or_404(Post, pk=post_id)

	if method=='POST':
		form=EmailPostForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
	else:
		form=EmailPostForm()
	return render(request, 'share.html',  {'post':post, 'form':form})