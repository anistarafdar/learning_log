from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """A topic the client is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns the text attribute of the Topic model as a string"""
        return self.text

class Entry(models.Model):
    """Something specific learned about a certain Topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns the text attribute of the Entry model as a string,
        showing only the first 50 characters"""
        if len(self.text) <= 50:
            return f"{self.text}"
        else:
            return f"{self.text[:50]}..."
