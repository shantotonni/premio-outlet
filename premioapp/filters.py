
#for filter
from admin_auto_filters.filters import AutocompleteFilter

class MarketFilter(AutocompleteFilter):
    title = 'Market' # display title
    field_name = 'market' # name of the foreign key field
    
class RouteFilter(AutocompleteFilter):
    title = 'Route' # display title
    field_name = 'route' # name of the foreign key field


class BaseFilter(AutocompleteFilter):
    title = 'Base' # display title
    field_name = 'base' # name of the foreign key field
    
class ZoneFilter(AutocompleteFilter):
    title = 'Zone' # display title
    field_name = 'zone' # name of the foreign key field

class UserFilter(AutocompleteFilter):
    title = 'User' # display title
    field_name = 'user' # name of the foreign key field