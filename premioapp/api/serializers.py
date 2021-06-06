from ..models import *
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ('__all__')
        depth=2

class RouteDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteDay
        fields = ('__all__')
        
class RouteSerialiser(serializers.ModelSerializer):
    
    #display_name = serializers.CharField(read_only=True, source="route")
    display_name = serializers.SerializerMethodField(read_only=True) 
    def get_display_name(self, obj):
        return '{} - {}'.format(obj.route_day.name,obj.name, ) 
    
    class Meta:
        model = Route
        fields = ('id','name','base','route_day','display_name',)
        #fields = ('__all__')
        #depth = 1
        
class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        # fields = ['name','base']
        read_only_fields = ('id', 'creator')
        fields = ('__all__')

class MarketParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ('__all__')
        depth = 2


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')
        
class OutletTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutletType
        fields = ('__all__')
        
class OutletSerializer(serializers.ModelSerializer):
    #creator = serializers.ReadOnlyField(source='creator.username')
    #id = serializers.IntegerField(required=False)
    class Meta:
        model = Outlet
        fields=('__all__')
        read_only_fields = ('id', 'creator')
        #fields = ('market','outlet_type','category','name','propritor_name','mobile','lat','lng','creator')
        #depth = 1
    
    # def create(self,validated_data):
    #     User.objects.create(**validated_data)


# class RecursiveSerializer(serializers.Serializer):
#     def to_representation(self, value):
#         serializer = self.parent.parent.__class__(value, context=self.context)
#         return serializer.data



## manual data 
class OutletRelatedField(serializers.RelatedField):
    def get_queryset(self):
        return Outlet.objects.all()

    def to_representation(self, value):
        #count = Outlet.objects.filter(creator=value.pk).count()
        topic = Outlet.objects.get(pk=value.pk)
        return{'pk': value.pk,'name': topic.name}


class UserSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(many=True, queryset=Outlet.objects.all())
    #user = RecursiveSerializer(many=True, read_only=True)
    
    #outlet_creator = OutletRelatedField(read_only=True, many=True)
    
    # outlets = OutletSerializer(many=True)
    
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name']
        


class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBase
        fields = ('__all__')
        
class ApkVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApkVersion
        fields = ('__all__')
        
        
class LiveLocationSerializer(serializers.ModelSerializer):
    entry_time=serializers.DateTimeField(format=None,input_formats=None)
    class Meta:
        model = LiveLocation
        fields = ['lat','lng','entry_time']




from django.contrib.auth import password_validation
from django.utils.translation import ugettext as _
class ChangePasswordSerializer(serializers.Serializer):
    old_password      = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                _('Your old password was entered incorrectly. Please enter it again.')
            )
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': _("The two password fields didn't match.")})
        password_validation.validate_password(data['new_password1'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user




