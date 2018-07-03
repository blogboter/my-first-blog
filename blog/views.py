from django.shortcuts import render, HttpResponse, get_object_or_404
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentForm
from taggit.models import Tag
from django.db.models import Count

# Create your views here.

def post_list(request, tag_slug=None):
	object_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	tag=None

	if tag_slug:
		tag=get_object_or_404(Tag, slug=tag_slug)
		object_list=object_list.filter(tags__in=[tag])

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
	'num':range(paginator.num_pages),
	'tag':tag})

def post_detail(request, year, month, day, title):
	post=get_object_or_404(Post, title=title, published_date__year=year, published_date__month=month, published_date__day=day)
	comments = post.comments.filter(active=True)

	if request.method=='POST':
		comment_form=CommentForm(request.POST)
		if comment_form.is_valid():
			new_comment=comment_form.save(commit=False)
			new_comment.post=post
			new_comment.save()
	else:
		comment_form=CommentForm()

	post_tags_ids=post.tags.values_list('id', flat=True)
	similar_posts=Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
	similar_posts=similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-published_date')[:4]

	return render(request, 'post_detail.html', {
		'post':post,
		'comments':comments,
		'comment_form':comment_form,
		'similar_posts':similar_posts
		})

	

def post_share(request, post_id):
	post=get_object_or_404(Post, pk=post_id)

	if method=='POST':
		form=EmailPostForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
	else:
		form=EmailPostForm()
	return render(request, 'share.html',  {'post':post, 'form':form})