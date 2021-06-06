from premioapp.models import *
from premioapp.api.serializers import *
from rest_framework import generics,mixins
from django.http import HttpResponseRedirect,HttpResponse, JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

@api_view(('GET',))
def authenticated_user_info(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
    
class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class BaseList(generics.ListAPIView):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer
    
    def get_queryset(self):
        user_bases = list(UserBase.objects.filter(user=self.request.user).values_list('base_id', flat=True))
        return Base.objects.filter(id__in =user_bases)

class RouteDayList(generics.ListAPIView):
    queryset = RouteDay.objects.all().order_by('id')
    serializer_class = RouteDaySerializer


class BaseList(generics.ListAPIView):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer
    
    def get_queryset(self):
        user_bases = list(UserBase.objects.filter(user=self.request.user).values_list('base_id', flat=True))
        return Base.objects.filter(id__in =user_bases)


class RouteList(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerialiser
    
    def get_queryset(self):
        user_bases = list(UserBase.objects.filter(user=self.request.user).values_list('base_id', flat=True))
        return Route.objects.filter(base_id__in =user_bases)
    
    
# class MarketList(generics.ListCreateAPIView):
#     queryset = Market.objects.all()
#     serializer_class = MarketSerializer


class MarketList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    serializer_class = MarketSerializer

    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         return MarketParentSerializer
    #     return MarketSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
    
    def get_queryset(self):
        user_bases = list(UserBase.objects.filter(user=self.request.user).values_list('base_id', flat=True))
        routes     = list(Route.objects.filter(base_id__in =user_bases).values_list('id', flat=True))
        return Market.objects.filter(route_id__in =routes)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MarketListWithParent(mixins.ListModelMixin,
                generics.GenericAPIView):
    serializer_class = MarketParentSerializer
    
    def get_queryset(self):
        user_bases = list(UserBase.objects.filter(user=self.request.user).values_list('base_id', flat=True))
        routes     = list(Route.objects.filter(base_id__in =user_bases).values_list('id', flat=True))
        return Market.objects.filter(route_id__in =routes)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MarketDetail(mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    generics.GenericAPIView):
    #queryset = Market.objects.all()
    serializer_class = MarketSerializer

    def get_queryset(self):
        user_bases = list(UserBase.objects.filter(user=self.request.user).values_list('base_id', flat=True))
        routes     = list(Route.objects.filter(base_id__in =user_bases).values_list('id', flat=True))
        return Market.objects.filter(route_id__in =routes)
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)



@api_view(['GET'])
def get_markets_of_user(request,username):
    try:
        user = User.objects.get(username=username)
        user_bases = list(UserBase.objects.filter(user=self.request.user).values_list('base_id', flat=True))
        routes     = list(Route.objects.filter(base_id__in =user_bases).values_list('id', flat=True))
        markets    = Market.objects.filter(route_id__in = routes)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = MarketSerializer(markets,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_outlets_of_user(request,username):
    try:
        user = User.objects.get(username=username)
        outlets    = Outlet.objects.filter(creator =user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = OutletSerializer(outlets,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_outlet_from_user():
    serializer = OutletSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserOutletList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    
    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        return Outlet.objects.filter(creator = user)
    
    serializer_class = OutletSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        user = User.objects.get(username=self.kwargs['username'])
        serializer.save(creator=user)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class UserOutletDetail(mixins.RetrieveModelMixin,
                generics.GenericAPIView):
    
    serializer_class = OutletSerializer
    
    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        return Outlet.objects.filter(creator = user)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    


    
    
class OutletTypeList(generics.ListAPIView):
    queryset = OutletType.objects.all()
    serializer_class = OutletTypeSerializer
    
class OutletTypeDetail(generics.RetrieveAPIView):
    queryset = OutletType.objects.all()
    serializer_class = OutletTypeSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OutletList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    #queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
    
    def get_queryset(self):
        return Outlet.objects.filter(creator = self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OutletDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@permission_classes([AllowAny])
class ApkVersionDetail(generics.RetrieveAPIView):
    queryset = ApkVersion.objects.all()
    serializer_class = ApkVersionSerializer
    
    

class LiveLocationDetail(mixins.CreateModelMixin,
                        # mixins.RetrieveModelMixin,
                        generics.GenericAPIView):
    queryset = Outlet.objects.all()
    serializer_class = LiveLocationSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user,username=self.request.user.username)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)