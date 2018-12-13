# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
import yaml


class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    artist_display_name =  models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'artist'
        ordering = ['artist_display_name']
        verbose_name = 'Artist Name'
        verbose_name_plural = 'Artist Names'

    def __str__(self):
        return self.artist_display_name   


class ArtistRole(models.Model):
    artist_role_id = models.AutoField(primary_key=True)
    artist_role =  models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'artist_role'
        ordering = ['artist_role']
        verbose_name = 'Artist Role'
        verbose_name_plural = 'Artists Roles'

    def __str__(self):
        return self.artist_role 


class ArtworkAttribution(models.Model):
    artwork_attribution_id = models.AutoField(primary_key=True)
    artwork_attribution =  models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'artwork_attribution'
        ordering = ['artwork_attribution']
        verbose_name = 'Artwork Attribution'
        verbose_name_plural = 'Artwork Attributions'

    def __str__(self):
        return self.artwork_attribution 


class ArtworkArtist(models.Model):
    artwork_artist_id = models.AutoField(primary_key=True)
    artwork = models.ForeignKey('Artwork', on_delete=models.CASCADE, blank=True, null=True)
    artwork_attribution = models.ForeignKey('ArtworkAttribution', models.DO_NOTHING, blank=True, null=True)
    artwork_artist_index = models.IntegerField()
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, blank=True, null=True)
    artist_role = models.ForeignKey('ArtistRole', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artwork_artist'
        ordering = ['artwork', 'artist']
        verbose_name = 'Artwork Artist'
        verbose_name_plural = 'Artwork Artists'



class Artwork(models.Model):
    artwork_id = models.AutoField(primary_key=True)
    accession_number = models.CharField(max_length=75)
    is_public_domain = models.CharField(max_length=5)
    department = models.ForeignKey('Department', on_delete=models.PROTECT)
    classification = models.ForeignKey('Classification', on_delete=models.PROTECT, blank=True, null=True)
    artwork_type = models.ForeignKey('ArtworkType', on_delete=models.PROTECT, blank=True, null=True)
    title = models.CharField(max_length=500)
    year_begin_end = models.CharField(max_length=255, blank=True, null=True)
    year_begin = models.IntegerField(blank=True, null=True)
    year_end = models.IntegerField(blank=True, null=True)
    medium = models.CharField(max_length=500, blank=True, null=True)
    dimensions = models.CharField(max_length=750, blank=True, null=True)
    acquired_from = models.CharField(max_length=1000, blank=True, null=True)
    city = models.ForeignKey('City', on_delete=models.PROTECT, blank=True, null=True)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, blank=True, null=True)
    region = models.ForeignKey('Region', on_delete=models.PROTECT, blank=True, null=True)
    resource_link = models.CharField(max_length=255, blank=True, null=True)
    rights_and_reproduction = models.CharField(max_length=255, blank=True, null=True)
    repository = models.ForeignKey('Repository', on_delete=models.PROTECT, blank=True, null=True)

    artist = models.ManyToManyField(Artist, through = 'ArtworkArtist')

    class Meta:
        managed = False
        db_table = 'artwork'
        ordering = ['title']
        verbose_name = 'MET Artwork'
        verbose_name_plural = 'MET Artwork'

    def __str__(self):
        return '{} {}'.format(self.title, self.accession_number)

    
    def get_absolute_url(self):
        return reverse('art_detail', kwargs={'pk': self.pk})

    def artist_display(self):
        """Create a string for country_area. This is required to display in the Admin view."""
        return ', '.join(
            artist.artist_display_name for artist in self.artist.all()[:25])

    artist_display.short_description = 'Artist'


    @property
    def region_names(self):
        """
        Returns a list of UNSD regions (names only) associated with a Heritage Site.
            Note that not all Heritage Sites are associated with a region. In such cases the
            Queryset will return as <QuerySet [None]> and the list will need to be checked for
            None or a TypeError (sequence item 0: expected str instance, NoneType found) runtime
            error will be thrown.
            :return: string
        """

        # Add code that uses self to retrieve a QuerySet composed of regions, then loops over it
        # building a list of region names, before returning a comma-delimited string of names.
        artwork = self.artwork.all().order_by('region__region_name')


        regions = []
        for each in artwork:
            region = each.region.region_name
            if region is None:
                continue
            if region not in regions:
                regions.append(region) 


        return ', '.join(regions)

    @property
    def country_names(self):
        """
        Returns a list of UNSD subregions (names only) associated with a Heritage Site.
        Note that not all Heritage Sites are associated with a subregion. In such cases the
        Queryset will return as <QuerySet [None]> and the list will need to be checked for
        None or a TypeError (sequence item 0: expected str instance, NoneType found) runtime
        error will be thrown.
        :return: string
        """

        # Add code that uses self to retrieve a QuerySet, then loops over it building a list of
        # sub region names, before returning a comma-delimited string of names using the string
        # join method.
        
        artwork = self.artwork.all().order_by('country__country_name')

        countries = []

        for each in artwork:
            country = each.country.country_name
            if country is None:
                continue
            if country not in countries:
                countries.append(country) 

        return ', '.join(countries)
        


    @property
    def city_names(self):
        """
        Returns a list of UNSD intermediate regions (names only) associated with a Heritage Site.
        Note that not all Heritage Sites are associated with an intermediate region. In such
        cases the Queryset will return as <QuerySet [None]> and the list will need to be
        checked for None or a TypeError (sequence item 0: expected str instance, NoneType found)
        runtime error will be thrown.
        :return: string
        """

        # Add code that uses self to retrieve a QuerySet, then loops over it building a list of
        # intermediate region names, before returning a comma-delimited string of names using the
        # string join method.
        artwork = self.artwork.all().order_by('city__city_name')

        cities = []
        
        try:
            for each in artwork:
                city = each.city.city_name
                if city is None:
                    continue
                if city not in cities:
                    cities.append(city) 

            return ', '.join(cities)
        
        except:
            pass 

    @property
    def artist_names(self):
        """
        Returns a list of artists associated with a piece of artwork.
        Note that not all Artworks are  associated with an artist. In such cases the
        Queryset will return as <QuerySet [None]> and the list will need to be checked for
        None or a TypeError (sequence item 0: expected str instance, NoneType found) runtime
        error will be thrown.
        :return: string
        """
        #IN FUTURE ADD SO THAT DISPLAYS ARTIST (ROLE)
        
        artwork = self.artist.all().order_by('artist_display_name')

        artists = []

        for each in artwork:
            artist = each.artist_display_name
            if artist is None:
                continue
            if artist not in artists:
                artists.append(artist) 

        return ', '.join(artists)


        # x = ArtworkArtist.objects.select_related('artist_role').values('artist__artist_display_name', 'artist_role__artist_role').order_by('artist__artist_display_name')
        # art = []
        # for each in x:
        #     artist = each.artist.artist_display_name
        #     if artist is None:
        #         continue
        #     role = each.artist_role

        #     artist_and_role = ''.join([artist, ' (', role, ')'])
        #     if artist_and_role not in art:
        #         art.append(artist_and_role)

        # return ', '.join(art)    








class ArtworkType(models.Model):
    artwork_type_id = models.AutoField(primary_key=True)
    artwork_type_name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'artwork_type'
        ordering = ['artwork_type_name']
        verbose_name = 'MET Artwork Type'
        verbose_name_plural = 'MET Artwork Types'

    def __str__(self):
        return self.artwork_type_name



class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(unique=True, max_length=255)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'
        ordering = ['city_name']
        verbose_name = 'MET Artwork City'
        verbose_name_plural = 'MET Artwork Cities'

    def __str__(self):
        return self.city_name


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'country'
        ordering = ['country_name']
        verbose_name = 'MET Artwork Country'
        verbose_name_plural = 'MET Artwork Countries'

    def __str__(self):
        return self.country_name


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'department'
        ordering = ['department_name']
        verbose_name = 'MET Artwork Department'
        verbose_name_plural = 'MET Artwork Departments'

    def __str__(self):
        return self.department_name


class Classification(models.Model):
    classification_id = models.AutoField(primary_key=True)
    classification_name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'classification'
        ordering = ['classification_name']
        verbose_name = 'MET Artwork Classification'
        verbose_name_plural = 'MET Artwork Classifications'

    def __str__(self):
        return self.classification_name


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_name = models.CharField(unique=True, max_length=255)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'
        ordering = ['region_name']
        verbose_name = 'MET Artwork Region'
        verbose_name_plural = 'MET Artwork Regions'

    def __str__(self):
        return self.region_name


class Repository(models.Model):
    repository_id = models.AutoField(primary_key=True)
    repository_name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'repository'
        ordering = ['repository_name']
        verbose_name = 'MET Artwork Repository'
        verbose_name_plural = 'MET Artwork Repositories'


    def __str__(self):
        return self.repository_name









#NEED TO ADD DECORATORS. ADD ARTISTS TO TO EACH TITLE; WILL BE COMMA SEPARATED WITH THEIR ROLE AND NATIONALITY IN ()S) 





















