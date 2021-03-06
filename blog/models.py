from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	ARTICLE_TYPE = (('ds','Data strcture'), ('pd', 'Parallel computing & distributed computing'), ('kg', 'Kaggles'), ('os','Others'),)
	type = models.CharField(max_length=10, choices=ARTICLE_TYPE, default = 'Others')
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	summary = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)

class Comment(models.Model):
	post = models.ForeignKey('blog.Post', related_name='comments', on_delete = models.CASCADE)
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text