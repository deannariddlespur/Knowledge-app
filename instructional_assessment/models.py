from django.db import models
from django.contrib.auth.models import User


class Content(models.Model):
    title = models.CharField(max_length=512, unique=True)
    source = models.CharField(max_length=512)
    body = models.TextField()

    def __unicode__(self):
        return u"{title}".format(title=self.title)

    def get_absolute_url(self):
        return "/{id}/".format(id=str(self.id))


class Question(models.Model):
    content = models.ForeignKey(Content)
    question_content = models.TextField()
    answer = models.BooleanField(help_text="""If it is unchecked the answer is False if it is checked the answer is True.""")

    def __unicode__(self):
        return u"{content}".format(content=self.content)


class Result(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    result = models.NullBooleanField(help_text="""If it is unchecked the answer is False if it is checked the answer is True.""")

    def __unicode__(self):
        return u"{result}".format(result=self.result)
