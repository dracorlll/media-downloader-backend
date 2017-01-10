from rest_framework import serializers
from youtube_dl import YoutubeDL


class YoutubeSerializer(serializers.Serializer):
    class Meta:
        fields = 'url'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        ydl = YoutubeDL()
        r = ydl.extract_info(validated_data, download=False)
        return r

