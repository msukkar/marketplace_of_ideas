from django.db import models

class User(models.Model):
	username = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	# password

class Transaction(models.Model):
	time = models.DateTimeField()
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)

class Post(models.Model):
	title = models.TextField()
