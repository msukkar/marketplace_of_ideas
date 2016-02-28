from django.db import models

class User(models.Model):
	username = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	followed_people = models.ManyToManyField('self', related_name='follows', symmetrical=False)

class BlogPost(models.Model):
	title = models.TextField()
	body = models.TextField()
	author = models.ForeignKey(User)

class Transaction(models.Model):
	time = models.DateTimeField(
		auto_now_add=True
	)
	payer = models.ForeignKey(User, related_name='payee')
	receiver = models.ForeignKey(User, related_name='receivee')
	blog_post = models.ForeignKey(BlogPost)
	amount = models.DecimalField(max_digits=10, decimal_places=2)

class Comment(models.Model):
	blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()