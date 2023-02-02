from rest_framework import viewsets
from .serializers import PostSerializer
from blog.models import Post
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from django_filters.rest_framework import OrderingFilter
from rest_framework import generics



class PostModeViewset(viewsets.ModelViewSet):
   
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle,AnonRateThrottle]
    #ilter_backends = [OrderingFilter]
    #ordering_fields =  ['title'] 