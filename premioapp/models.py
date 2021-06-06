from django.db import models
from django.contrib.auth.models import User,AbstractUser


# class User(AbstractUser):
#     phone = models.CharField(null=True,max_length=20)

#     #REQUIRED_FIELDS = ['username']
#     #USENAME_FIELD = 'username'
    
#     def get_username(self):
#         return self.username
    
class Designation(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=20,blank=False,null=False, unique=True)
    code  = models.CharField(max_length=20,blank=False,null=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Designation"
        #managed = False
        db_table = 'designation'

class Department(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=20,blank=False,null=False, unique=True)
    code  = models.CharField(max_length=20,blank=False,null=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Department"
        #managed = False
        db_table = 'department'

class UserDetail(models.Model):
    id           = models.AutoField(primary_key=True)
    user         = models.OneToOneField(User,related_name="user_details",on_delete=models.CASCADE)
    department   = models.ForeignKey(Department,related_name="user_detail_department",on_delete=models.PROTECT)
    designation  = models.ForeignKey(Designation,related_name="user_detail_designation",on_delete=models.PROTECT)
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User Detail"
        db_table = 'user_detail'


class Region(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=20,blank=False,null=False, unique=True)
    code  = models.CharField(max_length=20,blank=False,null=False, unique=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Region"
        #managed = False
        db_table = 'region'
        


class Zone(models.Model):
    id    = models.AutoField(primary_key=True)
    region= models.ForeignKey(Region,related_name="zone_region",on_delete=models.PROTECT)
    name  = models.CharField(max_length=20,blank=False,null=False, unique=True)
    code  = models.CharField(max_length=20,blank=False,null=False, unique=True)

    def __str__(self):
        return self.name + '-' +self.code

    class Meta:
        verbose_name = "Zone"
        #managed = False
        db_table = 'zone'
        
        

class Base(models.Model):
    id    = models.AutoField(primary_key=True)
    zone  = models.ForeignKey(Zone,related_name="base_zone",on_delete=models.PROTECT)
    name  = models.CharField(max_length=20,blank=False,null=False, unique=True)
    code  = models.CharField(max_length=20,blank=False,null=False, unique=True)

    def __str__(self):
        return self.code + '-' + self.name 
    
    @property
    def routes(self):
        return self.route_set.all()

    class Meta:
        verbose_name = "Base"
        #managed = False
        db_table = 'base'
        
        
class RouteDay(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=20,blank=False,null=False, unique=True)
    

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Route Day"
        #managed = False
        db_table = 'route_day'
        
        
class Route(models.Model):
    id        = models.AutoField(primary_key=True)
    base      = models.ForeignKey(Base,related_name="base_routes",on_delete=models.PROTECT)
    route_day = models.ForeignKey(RouteDay,related_name="route_day_routes",on_delete=models.PROTECT)
    name      = models.CharField(max_length=70,blank=False,null=False,unique=True)

    def __str__(self):
        return self.base.code +'-'+ self.name +'-'+ self.route_day.name
    
    @property
    def markets(self):
        return self.market_set.all()

    class Meta:
        verbose_name = "Route"
        unique_together =  ('base','name','route_day')
        #managed = False
        db_table = 'route'

class Category(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=20,blank=False,null=False, unique=True)
    code  = models.CharField(max_length=20,blank=False,null=False, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        #managed = False
        db_table = 'category'      


class Market(models.Model):
    id        = models.AutoField(primary_key=True)
    route     = models.ForeignKey(Route,related_name="route_markets",on_delete=models.PROTECT)
    name      = models.CharField(max_length=100,blank=False,null=False, unique=True)
    category  = models.ForeignKey(Category,related_name="market_category",on_delete=models.PROTECT)
    lng       = models.DecimalField(max_digits=9, decimal_places=6,blank=False,null=False)
    lat       = models.DecimalField(max_digits=9, decimal_places=6,blank=False,null=False)
    creator   = models.ForeignKey(User,related_name="market_creator",on_delete=models.PROTECT)

    @property
    def base(self):
        return self.route.base
    
    def __str__(self):
        #return self.name
        return self.name +'-'+ self.route.name +'-'+self.route.route_day.name

    class Meta:
        verbose_name = "Market"
        #managed = False
        db_table = 'market'
        

class OutletType(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=100,blank=False,null=False, unique=True)
    code  = models.CharField(max_length=100,blank=False,null=False, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Outlet Type"
        #managed = False
        db_table = 'outlet_type'
        
        





class Outlet(models.Model):
    id       = models.AutoField(primary_key=True)
    market   = models.ForeignKey(Market,related_name="outlet_market",on_delete=models.PROTECT)
    outlet_type = models.ForeignKey(OutletType,related_name="outlet_outlet_type",on_delete=models.PROTECT)
    category = models.ForeignKey(Category,related_name="outlet_category",on_delete=models.PROTECT)
    name     = models.CharField(max_length=100,blank=False,null=False)
    propritor_name = models.CharField(max_length=100,blank=False,null=False,unique=False)
    mobile   = models.CharField(max_length=20,blank=False,null=False)
    lng      = models.DecimalField(max_digits=9, decimal_places=6,blank=False,null=False)
    lat      = models.DecimalField(max_digits=9, decimal_places=6,blank=False,null=False)
    creator  = models.ForeignKey(User,related_name="outlet_creator",on_delete=models.PROTECT)
    
    
    def __str__(self):
        return self.name
    
    @property
    def route(self):
        return self.market.route
            
    class Meta:
        verbose_name = "Outlet"
        #managed = False 
        unique_together = ['name','propritor_name','mobile']
        db_table = 'outlet'
        
        
class UserBase(models.Model):
    id    = models.AutoField(primary_key=True)
    #user = models.OneToMany(User,related_name="user_base_user",on_delete=models.CASCADE)
    user  = models.ForeignKey(User,related_name="user_base_user",on_delete=models.PROTECT)
    base  = models.ForeignKey(Base,related_name="user_base_base",on_delete=models.PROTECT)
    
    def __str__(self):
        return self.user.username + ' '+ self.base.name

    class Meta:
        verbose_name = "User Base"
        #managed = False
        unique_together = ['user','base']
        db_table = 'user_base'


class ApkVersion(models.Model):
    id           = models.AutoField(primary_key=True)
    name         = models.CharField(max_length=100,blank=False,null=False,unique=True)
    version      = models.IntegerField(blank=False,null=False)
    version_text = models.CharField(max_length=10,blank=False,null=False)
    link         = models.TextField(blank=False,null=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Apk Version"
        db_table = 'apk_version'
        


class LiveLocation(models.Model):
    id          = models.AutoField(primary_key=True)
    user        = models.ForeignKey(User,related_name="live_location_user",on_delete=models.PROTECT)
    username    = models.CharField(max_length=10,blank=False,null=False)
    lng         = models.DecimalField(max_digits=9, decimal_places=6,blank=False,null=False)
    lat         = models.DecimalField(max_digits=9, decimal_places=6,blank=False,null=False)
    entry_time  = models.DateTimeField(blank=False,null=False)
    server_time = models.DateTimeField(auto_now_add=True,null=False)
    
    
    def __str__(self):
        return self.username
                
    class Meta:
        verbose_name = "Live Location"
        db_table = 'live_location'
        


