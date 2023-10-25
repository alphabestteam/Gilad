from django.db import models
from django.contrib.auth.models import User


class File:
    upload_date = models.DateField()
    file_writer = models.ForeignKey(User, related_name='file_writer', on_delete=models.CASCADE)
    file = models.FileField()

    def create(self, validated_data):
        return File(**validated_data)
    

    def update_variables(self, instance, *args):
        """
        function that get an instance of an object and tuple of parameters.
        the function change all the parameters in the instance
        """ 
        for parameter in args:
            instance.parameter = parameter
        return instance

    def update(self, instance):
        new_file = File
        upload_date = instance.data.upload_date
        file_writer = instance.data.file_writer
        file = instance.data.file
        new_file = self.update_variables(instance, (upload_date, file_writer, file))
        new_file.save()