from django.db import models

# Create your models here.
def blog_image_url(instance, filename):
    return './image/%s' % (filename)

class Program(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class Picture(models.Model):
    url = models.ImageField(upload_to=blog_image_url)
    related_program = models.ForeignKey(Program)

    def __unicode__(self):
        return "id: " + str(self.id) + ", program: " + self.related_program.title