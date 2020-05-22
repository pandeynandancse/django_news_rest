from news.models import News
from rest_framework import serializers



# for no of columns
class NewsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = News
		fields = "__all__"
