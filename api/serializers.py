from met.models import Artist
from rest_framework import response, serializers, status



class ArtistSerializer(serializers.ModelSerializer):
    artist_display_name = serializers.CharField(
        allow_blank=False,
        max_length = 225)


    class Meta:
        model = Artist
        fields = ('artist_id', 'artist_display_name')


    def create(self, validated_data):        
        artist = Artist.objects.create(**validated_data)        
        return artist
        

    def update(self, instance, validated_data):
        # site_id = validated_data.pop('heritage_site_id')
        artist_id = instance.artist_id
        
        instance.artist_display_name = validated_data.get(
            'artist_display_name',
            instance.artist_display_name
        )

        instance.save()

     


    

