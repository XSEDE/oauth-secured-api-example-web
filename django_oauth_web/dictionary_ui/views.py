from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from dictionary_db.models import *

# Create your views here.
class Home_Page(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request):
        uuid = None
        access_token = None
        refresh_token = None
        if request.user.is_authenticated:
            uuid = request.user.social_auth.get(provider='globus').uid
            social = request.user.social_auth
            access_token = social.get(provider='globus').extra_data['access_token']
            refresh_token = social.get(provider='globus').extra_data['refresh_token']
        return render(request,
                      'home.html',
                      {'uuid': uuid,
                      'access_token': access_token,
                      'refresh_token': refresh_token})

class Dictionary_Add(APIView):
#    permission_classes = (IsAuthenticatedOrReadOnly,)
    permission_classes = (AllowAny,)
    renderer_classes = (TemplateHTMLRenderer,)
    def get(self, request):
        return render(request, 'add.html', {})
    def post(self, request):
        if request.data.get('action', '') == 'Cancel':
            return Response({ 'message': 'Word not added' },
                status=status.HTTP_200_OK,
                template_name='home.html'
            )

        # For action = Save
        serializer = Dictionary_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'Word added "{}"'.format(request.data['word']) },
                        status=status.HTTP_200_OK,
                        template_name='home.html'
            )
        else:
            return Response({ 'message': 'ERROR adding word "{}" {}'.format(request.data['word'], serializer._errors ) },
                        status=status.HTTP_400_BAD_REQUEST,
                        template_name='home.html'
            )

class Dictionary_Update(APIView):
#    permission_classes = (IsAuthenticatedOrReadOnly,)
    permission_classes = (AllowAny,)
    renderer_classes = (TemplateHTMLRenderer,)
    def get(self, request, format=None, **kwargs):
#        import pdb
#        pdb.set_trace()
        try:
            object = Dictionary.objects.get(pk=self.kwargs['word'])
        except Dictionary.DoesNotExist:
            return Response({ 'message': 'Word not found "{}"'.format(self.kwargs['word']) },
                        status=status.HTTP_404_NOT_FOUND,
                        template_name='home.html'
            )
        serializer = Dictionary_Serializer(object)
        return Response( serializer.data, template_name='update.html')

    def post(self, request, **kwargs):
#        import pdb
#        pdb.set_trace()
        if request.data.get('action', '') == 'Cancel':
            return Response({ 'message': 'Update cancelled' },
                        status=status.HTTP_200_OK,
                        template_name='home.html'
            )
            
        if request.data.get('action', '') == 'Delete':
            try:
                object = Dictionary.objects.get(pk=self.kwargs['word']).delete()
                return Response({ 'message': 'Deleted word "{}"'.format(self.kwargs['word']) },
                            status=status.HTTP_200_OK,
                            template_name='home.html'
                )
            except:
                return Response({ 'message': 'ERROR deleting word "{}"'.format(self.kwargs['word']) },
                            status=status.HTTP_400_BAD_REQUEST,
                            template_name='home.html'
                )

        # For action = Update
        object = Dictionary.objects.get(pk=self.kwargs['word'])
        serializer = Dictionary_Serializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'Updated word "{}"'.format(self.kwargs['word']) },
                        status=status.HTTP_200_OK,
                        template_name='home.html'
            )
        else:
            return Response({ 'message': 'ERROR updating word "{}" {}'.format(self.kwargs['word'], serializer._errors ) },
                        status=status.HTTP_400_BAD_REQUEST,
                        template_name='home.html'
            )

class Dictionary_List(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (TemplateHTMLRenderer,)
    def get(self, request):
        try:
            objects = Dictionary.objects.all().order_by('word')
        except Dictionary.DoesNotExist:
            return Response({ 'message': 'ERROR listing dictionary' },
                        status=status.HTTP_400_BAD_REQUEST,
                        template_name='home.html'
            )
        serializer = Dictionary_Serializer(objects, many=True)
        response_obj = {'results': serializer.data }
        return Response(response_obj, template_name='list.html')
