from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from .resources import (ZoneResource,BaseResource,RouteResource,
                        MarketResource,OutletResource,OutletResourceExport,
                        UserResource,UserBaseResource)
from .filters import(MarketFilter,RouteFilter,BaseFilter,ZoneFilter,UserFilter)

# Register your models here.
from .models import (Region,Zone,Base,Market,OutletType,
                    Category,Outlet,UserBase,ApkVersion,
                    RouteDay,Route,UserDetail,Department,
                    Designation,LiveLocation
                )

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id','name','code')
    list_display_links = ('id','name','code')
    search_fields = ['name','code']
    ordering = ['-id']
    list_per_page = 20
admin.site.register(Region,RegionAdmin)

class ZoneAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','code','region')
    list_display_links = ('id','name','code','region')
    search_fields = ['name','code']
    ordering = ['-id']
    list_per_page = 20
    resource_class = ZoneResource
admin.site.register(Zone,ZoneAdmin)

class BaseAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','code','zone')
    list_display_links = ('id','name','code')
    ordering = ['-id']
    list_per_page = 20
    search_fields = ['name','code']
    autocomplete_fields = ['zone']
    resource_class = BaseResource

    
    list_filter = (ZoneFilter,) 
    class Media:
        pass
    
admin.site.register(Base,BaseAdmin)



class RouteDayAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']
    list_per_page = 20
admin.site.register(RouteDay,RouteDayAdmin)

class RouteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','route_day','base')
    list_display_links = ('id','name')
    search_fields = ['name','route_day__name','base__code','base__name']
    #list_filter = ('base__code','route_day__name')
    ordering = ['-id']
    autocomplete_fields = ['base']
    list_per_page = 20
    resource_class = RouteResource
    
    list_filter = (BaseFilter,'route_day') 
    class Media:
        pass
admin.site.register(Route,RouteAdmin)



class MarketAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','route','base','category','creator')
    list_display_links = ('id','name','route')
    search_fields = ('name',)
    autocomplete_fields = ('route',)
    ordering = ['-id']
    exclude = ['creator',]
    list_per_page = 20
    

    list_filter = [RouteFilter]
    ## whith out meta this filter will not work
    class Media:
        pass
    
    resource_class = MarketResource

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set creator during the first save.
            obj.creator = request.user
            super().save_model(request, obj, form, change)
admin.site.register(Market,MarketAdmin)


class OutletTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name','code')
    list_display_links = ('name','code')
    ordering = ['-id']
    list_per_page = 20
admin.site.register(OutletType,OutletTypeAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','code')
    list_display_links = ('name','code')
    search_fields = ['name','code']
    ordering = ['-id']
    list_per_page = 20
admin.site.register(Category,CategoryAdmin)

    
class OutletAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','propritor_name','market','route','category','outlet_type','creator')
    list_display_links = ('name','propritor_name','market','category','outlet_type')
    search_fields = ['name','propritor_name','market__name','category']
    autocomplete_fields = ('market','category')
    #raw_id_fields = ("market",)
    ordering = ['-id']
    exclude = ['creator',]
    list_per_page = 20
    resource_class = OutletResource
    

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set creator during the first save.
            obj.creator = request.user
            super().save_model(request, obj, form, change)
    
    def get_export_resource_class(self):
        """
        Returns ResourceClass to use for export.
        """
        return OutletResourceExport

    list_filter = [MarketFilter,'outlet_type','category']
    ## whith out media this filter will not work
    class Media:
        pass
            
admin.site.register(Outlet,OutletAdmin)

class UserBaseAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','user','base',)
    list_display_links = ('user','base')
    ordering = ['-id']
    search_fields = ['base']
    autocomplete_fields = ['user','base']
    list_per_page = 20
    
    resource_class = UserBaseResource

admin.site.register(UserBase,UserBaseAdmin)


class DesignationAdmin(admin.ModelAdmin):
    list_display = ('id','name','code',)
    list_display_links = ('id','name','code',)
    ordering = ['-id']
    list_per_page = 20
admin.site.register(Designation,DesignationAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','name','code',)
    list_display_links = ('id','name','code',)
    ordering = ['-id']
    list_per_page = 20
    
admin.site.register(Department,DepartmentAdmin)


class LiveLocationAdmin(admin.ModelAdmin):
    list_display = ('id','user','username','entry_time','server_time')
    list_display_links = ('id','user','username','entry_time','server_time')
    ordering = ['-id']
    list_per_page = 20
    
    list_filter = [UserFilter]
    ## whith out media this filter will not work
    class Media:
        pass
admin.site.register(LiveLocation,LiveLocationAdmin)

    
class ApkVersionAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links =('id','name')
    list_per_page = 20
admin.site.register(ApkVersion,ApkVersionAdmin)



# User Manger register here
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserBaseInline(admin.StackedInline):
    model = UserBase
    autocomplete_fields = ['base']
    extra = 1
    #can_delete = False
    verbose_name_plural = 'User Base'

class UserDetailInline(admin.StackedInline):
    model = UserDetail
    #autocomplete_fields = ['username']
    can_delete = False
    verbose_name_plural = 'User Detail'

# Define a new User admin
class UserAdmin(ImportExportModelAdmin,BaseUserAdmin):
    resource_class = UserResource
    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    #     # Removing the permission part
    #     # (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions')}),
    #     (('Permissions'), {'fields': ('is_staff', 'is_active',)}),
        
    #     (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    #     # Keeping the group parts? Ok, but they shouldn't be able to define
    #     # their own groups, up to you...
    #     (('Groups'), {'fields': ('groups',)}),
    # )
    from django.utils.translation import ugettext as _
    staff_fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Groups'), {'fields': ('groups',)}),
    )
    
    
    def save_model(self, request, obj, form, change):
        if obj.pk is None:
        #if not change:
            obj.is_staff = True
            print ("save_model called for change")
        super().save_model(request, obj, form, change)
    
    
    def change_view(self, request, *args, **kwargs):
        # for non-superuser
        if not request.user.is_superuser:
            try:
                self.fieldsets = self.staff_fieldsets
                response = super(UserAdmin, self).change_view(request, *args, **kwargs)
            finally:
                # Reset fieldsets to its original value
                self.fieldsets = UserAdmin.fieldsets
            return response
        else:
            return super(UserAdmin, self).change_view(request, *args, **kwargs)
        
    inlines = (UserDetailInline,UserBaseInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


#lgo entry
from django.contrib.admin.models import LogEntry
from .log_admin import LogEntryAdmin
admin.site.register(LogEntry,LogEntryAdmin)



# to solve race condition 
#https://stackoverflow.com/questions/2297377/how-do-i-prevent-permission-escalation-in-django-admin-when-granting-user-chang
# staff_readonly_fields = ('username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined')

#     def get_fieldsets(self, request, obj=None):
#         if not request.user.is_superuser:
#             return self.staff_fieldsets
#         else:
#             return super(UserAdmin, self).get_fieldsets(request, obj)

#     def get_readonly_fields(self, request, obj=None):
#         if not request.user.is_superuser:
#             return self.staff_readonly_fields
#         else:
#             return super(UserAdmin, self).get_readonly_fields(request, obj)