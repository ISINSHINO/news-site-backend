from rest_framework import serializers
from news_app.models import User

class ReadWriteSerializerMethodField(serializers.SerializerMethodField):

    def __init__(self, method_name=None, **kwargs): 
        self.method_name = method_name 
        kwargs['source'] = '*' 
        super(serializers.SerializerMethodField, self).__init__(**kwargs) 

    def to_internal_value(self, data): 
        return {self.field_name: User.objects.get(id=data)} 