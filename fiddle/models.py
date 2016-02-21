from django.db import models


class Fiddle(models.Model):
    context = models.TextField(blank=False, null=False)
    template = models.TextField(blank=False, null=False)

    def __str__(self):
        return 'Fiddle: id={}'.format(self.id)
