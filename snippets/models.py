from django.db import models

# Create your models here.
class Snippet(models.Model):
    # the title; the language the snippet is in; the snippet itself; and a brief description
    title = models.CharField(max_length=256, blank=False, null=False)
    language = models.CharField(max_length=256, blank=False, null=False)
    snippet = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        """ Sensible string representation of a snippet."""
        return "Title: {0} \n Language: {1} \n Snippet: {2} \n Description: {3}".format(self.title, self.language, self.snippet, self.description)

