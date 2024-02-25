from django.db import models



class Todo(models.Model):
    title = models.CharField(verbose_name="Title",max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name="Deadline",auto_now_add=True, null=False, blank=False)
    deadline = models.DateTimeField(null=False, blank=True)
    finished_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
