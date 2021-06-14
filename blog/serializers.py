from rest_framework import serializers


class SingleArticleSerializer(serializers.Serializer):
	title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=28)
	cover = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)
	content = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2048)
	created_at = serializers.DateTimeField(required=True, allow_null=False)


class SubmitArticleSerializer(serializers.Serializer):
	title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=200)
	cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)
	content = serializers.CharField(required=True,allow_null=False, allow_blank=False, max_length=3000)
	category_id = serializers.IntegerField(required=True, allow_null=False)
	author_id = serializers.IntegerField(required=True, allow_null=False)
	promote = serializers.BooleanField(required=True, allow_null=False)