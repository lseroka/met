from django.shortcuts import render
from met.models import Artist, ArtworkArtist
from api.serializers import ArtistSerializer
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response


class ArtistViewSet(viewsets.ModelViewSet):
	"""
	This ViewSet provides both 'list' and 'detail' views.
	"""
	queryset = ArtworkArtist.objects.select_related('artist', 'artist_role', 'artwork', 'artwork_attribution').order_by('artist__artist_display_name')
	serializer_class = ArtistSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def delete(self, request, pk, format=None):
		artist = self.get_object(pk)
		self.perform_destroy(self, artist)

		return Response(status=status.HTTP_204_NO_CONTENT)

	def perform_destroy(self, instance):
		instance.delete()



class ArtistListAPIView(generics.ListCreateAPIView):
	queryset = ArtworkArtist.objects.select_related('artist', 'artist_role', 'artwork', 'artwork_attribution').order_by('artist__artist_display_name')
	serializer_class = ArtistSerializer
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class ArtistDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ArtworkArtist.objects.select_related('artist', 'artist_role', 'artwork', 'artwork_attribution').order_by('artist__artist_display_name')
	serializer_class = ArtistSerializer
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

