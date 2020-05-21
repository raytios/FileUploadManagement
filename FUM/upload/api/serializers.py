from rest_framework import serializers

from upload.models import Collaborate_Files_A00, Module




class FUMSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collaborate_Files_A00

        fields = [
            'collaborate_files_a00_rec',
            'module_used_id',
            'contact_id',
            'category',
            'file_name',
            'date_timestamp',
            'notes',
        ]

class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module

        fields = [
            'pk',
            'module_name',
        ]
#class ContactSerializer(serializers.ModelSerializer):

    #class Meta:
        #model = Contact

        #fields = [
            #'pk',
            #'first_name',
            #'last_name',
            #'address',
            #]
class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborate_Files_A00

        fields = [
            'module_used_id',
            'contact_id',
            'category',
            'file_name',
            'date_timestamp',
            'notes',
        ]



class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborate_Files_A00

        fields = [
            'module_used_id',
            'contact_id',
            'category',
            'file_name',
            'date_timestamp',
            'notes',
        ]
