from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

class Post(models.Model):
	author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField( blank=True, null=True)
	def publish(self):
		self.published_date=timezone.now()
		self.save()
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse(
				'blog:post_detail',
				args=[
					self.published_date.year,
					self.published_date.strftime('%m'),
					self.published_date.strftime('%d'),
					self.title
				])

class Comment(models.Model):
	post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	name=models.CharField(max_length=80)
	email=models.EmailField()
	body=models.TextField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	active=models.BooleanField(default=True)

	class Meta:
		ordering= ('created', )
	
	def __str__(self):
	 		return 'Comment by {} on {}'.format(self.name, self.post)
