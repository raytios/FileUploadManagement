from rest_framework import generics
from upload.models import Collaborate_Files_A00, Module
from .serializers import FUMSerializer, ModuleSerializer,FileListSerializer, FileCreateSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Q

class FUMCreate(generics.CreateAPIView):
    queryset = Collaborate_Files_A00.objects.all()
    lookup_field = 'collaborate_files_a00_rec'
    serializer_class = FileCreateSerializer

    def get_queryset(self):
        check=Collaborate_Files_A00.objects.values_list('collaborate_files_a00_rec', 'file_name')
        print(check) #to be imported in a repository
        return Collaborate_Files_A00.objects.all()

class FUMRead(generics.RetrieveUpdateAPIView):
    lookup_field = 'collaborate_files_a00_rec'
    serializer_class = FUMSerializer

    def get_queryset(self):
        return Collaborate_Files_A00.objects.all()

class ModuleRead(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = ModuleSerializer

    def get_queryset(self):
        return Module.objects.all()

#class ContactRead(generics.RetrieveAPIView):
    #lookup_field = 'pk'
    #serializer_class = ContactSerializer

    #def get_queryset(self):
        #return Contact.objects.all()


class FileListAPIView(generics.ListAPIView):
    serializer_class = FileListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['category', 'file_name', 'date_timestamp', 'notes', 'module_used_id__module_name']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Collaborate_Files_A00.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(category__icontains=query)|
                Q(file_name__icontains=query)|
                Q(date_timestamp__icontains=query)|
                Q(notes__icontains=query)|
                Q(contact_id__last_name__icontains=query)|
                Q(module_used_id__module_name__icontains=query)
            ).distinct()
        return queryset_list