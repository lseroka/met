from django.shortcuts import render
from met.models import Artist 
from api.serializers import ArtistSerializer
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response


class ArtistViewSet(viewsets.ModelViewSet):
	"""
	This ViewSet provides both 'list' and 'detail' views.
	"""
	queryset = Artist.objects.all().order_by('artist_display_name')
	serializer_class = ArtistSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def delete(self, request, pk, format=None):
		artist = self.get_object(pk)
		self.perform_destroy(self, artist)

		return Response(status=status.HTTP_204_NO_CONTENT)

	def perform_destroy(self, instance):
		instance.delete()



class ArtistListAPIView(generics.ListCreateAPIView):
	queryset = Artist.objects.all().order_by('artist_display_name')
	serializer_class = ArtistSerializer
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class ArtistDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Artist.objects.all().order_by('artist_display_name')
	serializer_class = ArtistSerializer
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

