from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import mixins, generics
from .models import Article
from .serializers import ArticleSerializer


# # csrf_exempt
# def article_list(request):
#     """
#     article retrive, article create by postman
#     """
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializers = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializers.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parser(request)
#         serializers = ArticleSerializer(data=data)
#         if serializers.is_valid():
#             serializers.save()
#             return JsonResponse(serializers.data, status=201)
#         return JsonResponse(serializers.errors, status=400)
#
#
#
# # @csrf_exempt
# def article_detail(request, pk):
#     """
#     article retrive, update, delete
#     """
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parser(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)


# @api_view(['GET', 'POST'])
# def article_list(request):
#     """
#     article retrive, article create by postman
#     """
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializers = ArticleSerializer(articles, many=True)
#         return Response(serializers.data)
#
#     elif request.method == 'POST':
#         serializers = ArticleSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk):
#     """
#     article retrive, update, delete
#     """
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class base view
# class ArticleList(APIView):
#     """
#     This is class base view, will inherit from generic APIView.
#     This will retrive Article model objects or create one.
#     """
#     def get(self, request, format=None):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# class ArticleDetail(APIView):
#     """
#     This class will retrive Article objects, Update, Delete
#     """
#     # def get_object(self, pk):
#     #     try:
#     #         article = Article.objects.get(pk=pk)
#     #     except Article.DoesNotExist:
#     #         return Http404
#
#     def get(self, request, pk, format=None):
#         try:
#             article = Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             return HttpResponse("Object Not Found!")
#         # article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         article = Article.objects.get(pk=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ArticleListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#
# class ArticleDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class ArticleListView(generics.ListCreateAPIView, generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#
# class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     # authentication_classes = [SessionAuthentication]
#     # permission_classes = [IsAuthenticated]

class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
