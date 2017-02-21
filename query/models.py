from django.db import models
from django.conf import settings


class Query(models.Model):
    user_posted = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    query_text = models.TextField(help_text='query here...')
    written = models.DateTimeField()
    disease = models.CharField(max_length=40,blank=True,null=True)
    soln_num = models.IntegerField(default = 0)

    def __str__(self):
        return self.query_text[:20]

class Solutions(models.Model):
    user_posted = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    query = models.ForeignKey(Query, on_delete=models.CASCADE )
    soln_text = models.TextField()
    soln_score = models.IntegerField(blank=True, null=True)
    written = models.DateTimeField()
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.soln_text[:30]


class Comments(models.Model):
    user_posted = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    soln = models.ForeignKey(Solutions, on_delete=models.CASCADE )
    comment_text = models.TextField()
    written = models.DateTimeField()

    def __str__(self):
        return self.comment_text

class Upvote(models.Model):
    solution = models.ForeignKey(Solutions, on_delete=models.CASCADE )
    voted_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

class Downvote(models.Model):
    solution = models.ForeignKey(Solutions, on_delete=models.CASCADE )
    voted_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)