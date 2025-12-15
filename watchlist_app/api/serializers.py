from rest_framework import serializers

# First type of serializer: Serializer
class MovieSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  name = serializers.CharField()
  description = serializers.CharField()
  active = serializers.BooleanField()