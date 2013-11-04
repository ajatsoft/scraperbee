# myapp/api.py
from tastypie.resources import ModelResource
from api.models import DetailPage
from serializers import CSVSerializer

# our basic scraped item is called an "Entry"
class EntryResource(ModelResource):
    class Meta:
        queryset = DetailPage.objects.all()
        resource_name = 'entry'
        max_limit = None  # this prevents the max limit 1000 so you can grab all the things
        serializer = CSVSerializer(formats=['json', 'csv'])

