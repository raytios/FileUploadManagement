from django.db import models
from django.conf import settings
#from file_upload.models import Document

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)


    def __str__(self):
        return str(self.last_name)


class Module(models.Model):
    module_name = models.CharField(max_length=250)


    def __str__(self):
        return str(self.module_name)


class Collaborate_Files_A00(models.Model):
    collaborate_files_a00_rec = models.AutoField(primary_key=True)
    module_used_id = models.ForeignKey(Module, on_delete=models.CASCADE)
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)

    IMG = "IMAGE"
    AUDIO = "AUDIO"
    VID = "VIDEO"
    DOC = "DOCUMENT"

    CATEGORY_TYPE_CHOICES = [
        (IMG, 'Image'),
        (AUDIO, 'Audio'),
        (VID, 'Video'),
        (DOC, 'Document'),

    ]
    category = models.CharField(max_length=20, choices=CATEGORY_TYPE_CHOICES)
    file_name = models.CharField(max_length=250)
    date_timestamp = models.DateTimeField(auto_now=True, auto_created=True)
    notes = models.TextField()
    #upload = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.module_used_id) + '  ' + str(self.file_name) + ' - ' + str(self.contact_id.last_name) + ',' + str(self.contact_id.first_name)

    #def __str__(self):
       # return f'{self.category}'





