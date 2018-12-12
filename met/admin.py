from django.contrib import admin

# Register your models here.
from django.contrib import admin

import met.models as models


@admin.register(models.Artwork)
class ArtworkAdmin(admin.ModelAdmin):
	fields = [
		'accession_number',
		'is_public_domain',
		'department',
		'classification',
		'artwork_type',
		'title',
		'year_begin_end',
		'year_begin',
		'year_end',
		'medium',
		'dimensions',
		'acquired_from',
		'city',
		'country',
		'region',
		'resource_link',
		'rights_and_reproduction',
		'repository'
	]

	list_display = [
		'accession_number',
		'is_public_domain',
		'department',
		'classification',
		'artwork_type',
		'title',
		'year_begin_end',
		'year_begin',
		'year_end',
		'medium',
		'dimensions',
		'acquired_from',
		'city',
		'country',
		'region',
		'resource_link',
		'rights_and_reproduction',
		'repository'
	]

	list_filter = ['city', 'country', 'region', 'artwork_type', 'department', 'classification', 'repository']


@admin.register(models.ArtworkType)
class ArtworkTypeAdmin(admin.ModelAdmin):
	fields = ['artwork_type_name']
	list_display = ['artwork_type_name']
	ordering = ['artwork_type_name']



@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
	fields = ['city_name', 'country']
	list_display = ['city_name', 'country']
	ordering = ['city_name']


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
	fields = ['country_name']
	list_display = ['country_name']
	ordering = ['country_name']


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
	fields = ['region_name', 'country']
	list_display = ['region_name', 'country']
	ordering = ['region_name']



@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
	fields = ['department_name']
	list_display = ['department_name']
	ordering = ['department_name']


@admin.register(models.Classification)
class DepartmentAdmin(admin.ModelAdmin):
	fields = ['classification_name']
	list_display = ['classification_name']
	ordering = ['classification_name']


@admin.register(models.Repository)
class RepositoryAdmin(admin.ModelAdmin):
	fields = ['repository_name']
	list_display = ['repository_name']
	ordering = ['repository_name']


@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
	fields = ['artist_display_name']
	list_display = ['artist_display_name']
	ordering = ['artist_display_name']


@admin.register(models.ArtistRole)
class ArtistRoleAdmin(admin.ModelAdmin):
	fields = ['artist_role']
	list_display = ['artist_role']
	ordering = ['artist_role']


@admin.register(models.ArtworkAttribution)
class ArtworkAttributionAdmin(admin.ModelAdmin):
	fields = ['artwork_attribution']
	list_display = ['artwork_attribution']
	ordering = ['artwork_attribution']