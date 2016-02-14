from django.db import models

class User(models.Model):
	username = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

class Relationship(models.Model):
	follower = models.OneToOneField(User)
	following = models.OneToOneField(User)

class Transaction(models.Model):
	time = models.DateTimeField()
	payer = models.ForeignKey(User)
	receiver = models.ForeignKey(User)
	blog_post = models.ForeignKey(BlogPost)
	amount = models.DecimalField(max_digits=10, decimal_places=2)

class BlogPost(models.Model):
	title = models.TextField()
	body = models.TextField()
	authors = models.ManyToManyField(User)

class Comment(models.Model):
	blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()


