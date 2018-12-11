import django_filters
from met.models import Artwork, City, Country, Region, Department, ArtworkType, Classification


class ArtworkFilter(django_filters.FilterSet):
	title = django_filters.CharFilter(
		field_name='title',
		label='Artwork Title',
		lookup_expr='icontains'
	)

	art_type = django_filters.ModelChoiceFilter(
		field_name='artwork_type',
		label='Artwork Type',
		queryset = ArtworkType.objects.all().order_by('artwork_type_name'),
		lookup_expr='exact'
	) 

	region = django_filters.ModelChoiceFilter(
		field_name='region__region_name',
		label = 'Region',
		queryset = Region.objects.all().order_by('region_name'),
		lookup_expr='exact'
	)

	country = django_filters.ModelChoiceFilter(
		field_name='country__country_name',
		label = 'Country',
		queryset = Country.objects.all().order_by('country_name'),
		lookup_expr='exact'
	)

	city = django_filters.ModelChoiceFilter(
		field_name='city__city_name',
		label = 'City',
		queryset = City.objects.all().order_by('city_name'),
		lookup_expr='exact'
	)

	department = django_filters.ModelChoiceFilter(
		field_name='department__department_name',
		label = 'MET Department',
		queryset = Department.objects.all().order_by('department_name'),
		lookup_expr='exact'
	)


	pub_domain = django_filters.CharFilter(
		field_name='is_public_domain',
		label='Public Domain? \n' + str(True) + '= Yes / ' + str(False) + '= No',
		lookup_expr='icontains'
	)

	begin_date = django_filters.NumberFilter(
		field_name='year_begin',
		label='Begin Year',
		lookup_expr='icontains'
	)
	end_date = django_filters.NumberFilter(
		field_name='year_end',
		label='End Year',
		lookup_expr='icontains'
	)

	# category = django_filters.ModelChoiceFilter(
	# 	field_name='category_name',
	# 	label = 'Heritage Site Category',
	# 	queryset = HeritageSiteCategory.objects.all().order_by('category_name'),
	# 	lookup_expr='exact'
	# )

	# region = django_filters.ModelChoiceFilter(
	# 	field_name='country_area__location__region__region_name',
	# 	label = 'Region',
	# 	queryset = Region.objects.all().order_by('region_name'),
	# 	lookup_expr='exact'
	# )

	# sub_region = django_filters.ModelChoiceFilter(
	# 	field_name='country_area__location__sub_region__sub_region_name',
	# 	label = 'SubRegion',
	# 	queryset = SubRegion.objects.all().order_by('sub_region_name'),
	# 	lookup_expr='exact'
	# )

	# intermediate_region = django_filters.ModelChoiceFilter(
	# 	field_name='country_area__location__intermediate_region__intermediate_region_name',
	# 	label = 'IntermediateRegion',
	# 	queryset = IntermediateRegion.objects.all().order_by('intermediate_region_name'),
	# 	lookup_expr='exact'
	# )


#WILL NEED TO INCORPORATE THIS FOR ARTIST
	# country_area = django_filters.ModelChoiceFilter(
	# 	field_name='country_area',
	# 	label='Country/Area',
	# 	queryset=CountryArea.objects.all().order_by('country_area_name'),
	# 	lookup_expr='exact'
	# )

	# date_inscribed = django_filters.NumberFilter(
	# 	field_name = 'date_inscribed',
	# 	label = 'Date Inscribed',
	# 	lookup_expr = 'exact'
	# )



	class Meta:
		model = Artwork
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = []