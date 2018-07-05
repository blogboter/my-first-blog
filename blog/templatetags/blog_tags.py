from django import template
from django.db.models import Count

register=template.Library()

from ..models import Post

@register.simple_tag
def total_posts():	
	return  Post.objects.count()

@register.inclusion_tag('latest_posts.html')
def show_latest_posts(count):
	latest_posts=Post.objects.order_by('published_date')[:count]
	return {'latest_posts':latest_posts}

@register.simple_tag
def get_most_commented_posts(count):
	return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
