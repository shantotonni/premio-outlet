from import_export import resources,fields
from django.contrib.auth.hashers import make_password
from import_export.widgets import ManyToManyWidget
from django.contrib.auth.models import User,Group
from import_export.widgets import ForeignKeyWidget
from .models import (Region,Zone,Base,Market,OutletType,
                    Category,Outlet,UserBase,ApkVersion,
                    RouteDay,Route 
                )

class UserResource(resources.ModelResource):
    groups = fields.Field(
           column_name='group_name',
           attribute='groups',
           widget=ManyToManyWidget(Group, ',','name')
       )

    def before_import_row(self,row, **kwargs):
           value = row['password']
           row['password'] = make_password(value)

    class Meta:
        model = User
        import_id_fields = ('id',)
        fields = ['id', 'username','password', 'first_name', 'groups','is_staff']
            
class UserBaseResource(resources.ModelResource):
    user = fields.Field(column_name='username',attribute='user',widget=ForeignKeyWidget(User, 'username'))
    base = fields.Field(column_name='base_code',attribute='base',widget=ForeignKeyWidget(Base, 'code'))
    class Meta:
        skip_unchanged = True
        report_skipped = True
        model = UserBase         


class ZoneResource(resources.ModelResource):
    region = fields.Field(column_name='region_code',attribute='region',widget=ForeignKeyWidget(Region, 'code'))
    class Meta:
        model = Zone
        
        
class BaseResource(resources.ModelResource):
    zone = fields.Field(column_name='zone_code',attribute='zone',widget=ForeignKeyWidget(Zone, 'code'))
    class Meta:
        #fields = ('id', 'name', 'author', 'price',)
        #export_order = ('id', 'price', 'author', 'name')
        skip_unchanged = True
        report_skipped = True
        model = Base
        

class RouteResource(resources.ModelResource):
    base      = fields.Field(column_name='base_code',attribute='base',widget=ForeignKeyWidget(Base, 'code'))
    route_day = fields.Field(column_name='route_day_name',attribute='route_day',widget=ForeignKeyWidget(RouteDay, 'name'))
    class Meta:
        model = Route
        
class MarketResource(resources.ModelResource):
    route    = fields.Field(column_name='route_name',attribute='route',widget=ForeignKeyWidget(Route, 'name'))
    category    = fields.Field(column_name='category_code',attribute='category',widget=ForeignKeyWidget(Category, 'code'))
    class Meta:
        #fields = ('name','route')
        model = Market

class OutletResource(resources.ModelResource):
    market      = fields.Field(column_name='market_name',attribute='market',widget=ForeignKeyWidget(Market, 'name'))
    category    = fields.Field(column_name='category_code',attribute='category',widget=ForeignKeyWidget(Category, 'code'))
    outlet_type = fields.Field(column_name='outlet_type_code',attribute='outlet_type',widget=ForeignKeyWidget(OutletType, 'code'))
    
    class Meta:
        model = Outlet


class OutletResourceExport(resources.ModelResource):
    region_name   = fields.Field()
    region_code   = fields.Field()
    zone_name   = fields.Field()
    zone_code   = fields.Field()
    base_name   = fields.Field()
    base_code   = fields.Field()
    route_day   = fields.Field()
    route_name  = fields.Field()
    market      = fields.Field(column_name='market_name',attribute='market',widget=ForeignKeyWidget(Market, 'name'))
    market_category  = fields.Field()
    category    = fields.Field(column_name='category_code',attribute='category',widget=ForeignKeyWidget(Category, 'code'))
    outlet_type = fields.Field(column_name='outlet_type_code',attribute='outlet_type',widget=ForeignKeyWidget(OutletType, 'code'))
    
    class Meta:
        model = Outlet
    
    
    def dehydrate_route_day(self, outlet):
        return outlet.market.route.route_day.name
    def dehydrate_route_name(self, outlet):
        return outlet.market.route.name
    def dehydrate_base_code(self, outlet):
        return outlet.market.base.code
    def dehydrate_base_name(self, outlet):
        return outlet.market.base.name
    def dehydrate_zone_code(self, outlet):
        return outlet.market.base.zone.code
    def dehydrate_zone_name(self, outlet):
        return outlet.market.base.zone.name
    def dehydrate_region_code(self, outlet):
        return outlet.market.base.zone.region.code
    def dehydrate_region_name(self, outlet):
        return outlet.market.base.zone.region.name
    def dehydrate_market_category(self, outlet):
        return outlet.market.category.name