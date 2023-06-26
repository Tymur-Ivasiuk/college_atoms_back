from rest_framework import serializers


class ScoreAPI(serializers.Serializer):
    status = serializers.IntegerField()
    students = serializers.ListField()



