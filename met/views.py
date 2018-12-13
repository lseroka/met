from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy, resolve
from django_filters.views import FilterView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from .models import Artwork, ArtworkArtist
from .forms import ArtworkForm
from .filters import ArtworkFilter

# Create your views here.
def index(request):
   return HttpResponse("Welcome to the MET.")

class AboutPageView(generic.TemplateView):
	template_name = 'met/about.html'


class HomePageView(generic.TemplateView):
	template_name = 'met/home.html'


@method_decorator(login_required, name='dispatch')
class ArtListView(generic.ListView):
	model = Artwork
	context_object_name = 'arts'
	template_name = "met/art.html"
	paginate_by = 20

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Artwork.objects.all().order_by('title')



@method_decorator(login_required, name='dispatch')
class ArtDetailView(generic.DetailView):
	model = Artwork
	context_object_name = 'art'
	template_name = 'met/art_detail.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_object(self):
		artwork = super().get_object()
		return artwork







@method_decorator(login_required, name='dispatch')
class ArtCreateView(generic.View):
	model = Artwork
	form_class = ArtworkForm
	success_message = "Artwork created successfully"
	template_name = 'met/art_new.html'
	# fields = '__all__' <-- superseded by form_class
	# success_url = reverse_lazy('heritagesites/site_list')

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def post(self, request):
		form = ArtworkForm(request.POST)
		if form.is_valid():
			art = form.save(commit=False)
			art.save()
			# for country in form.cleaned_data['country_area']:
			# 	HeritageSiteJurisdiction.objects.create(heritage_site=site, country_area=country)
			return redirect(art) # shortcut to object's get_absolute_url()
			# return HttpResponseRedirect(site.get_absolute_url())
		return render(request, 'met/art_new.html', {'form': form})

	def get(self, request):
		form = ArtworkForm()
		return render(request, 'met/art_new.html', {'form': form})



@method_decorator(login_required, name='dispatch')
class ArtUpdateView(generic.UpdateView):
	model = Artwork
	form_class = ArtworkForm
	# fields = '__all__' <-- superseded by form_class
	context_object_name = 'art'
	# pk_url_kwarg = 'site_pk'
	success_message = "Artwork updated successfully"
	template_name = 'met/art_update.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		art = form.save(commit=False)
		# site.updated_by = self.request.user
		# site.date_updated = timezone.now()
		art.save()

		# If any existing country/areas are not in updated list, delete them
		new_ids = []
		old_ids = ArtworkArtist.objects\
			.values_list('artist_id', flat=True)\
			.filter(artwork_id=art.artwork_id)

		# New artist list
		new_artists = form.cleaned_data['artists']

		# Insert new unmatched country entries
		for artist in new_artists:
			new_id = artist.artist_id
			new_ids.append(new_id)
			if new_id in old_ids:
				continue
			else:
				ArtworkArtist.objects \
					.create(artwork=art, artist=artist)

		# Delete old unmatched country entries
		for old_id in old_ids:
			if old_id in new_ids:
				continue
			else:
				ArtworkArtist.objects \
					.filter(artwork_id=art.artwork_id, artist_id=old_id) \
					.delete()

		return HttpResponseRedirect(art.get_absolute_url())
		# return redirect('heritagesites/site_detail', pk=site.pk)

@method_decorator(login_required, name='dispatch')
class ArtDeleteView(generic.DeleteView):
	model = Artwork
	success_message = "Artwork deleted successfully"
	success_url = reverse_lazy('art')
	context_object_name = 'art'
	template_name = 'met/art_delete.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()

		# Delete HeritageSiteJurisdiction entries
		# HeritageSiteJurisdiction.objects \
		# 	.filter(heritage_site_id=self.object.heritage_site_id) \
		# 	.delete()
		ArtworkArtist.objects.filter(artwork_id = self.object.artwork_id).delete()

		self.object.delete()

		return HttpResponseRedirect(self.get_success_url())		








class PaginatedFilterView(generic.View):
	"""
	Creates a view mixin, which separates out default 'page' keyword and returns the
	remaining querystring as a new template context variable.
	https://stackoverflow.com/questions/51389848/how-can-i-use-pagination-with-django-filter
	"""
	def get_context_data(self, **kwargs):
		context = super(PaginatedFilterView, self).get_context_data(**kwargs)
		if self.request.GET:
			querystring = self.request.GET.copy()
			if self.request.GET.get('page'):
				del querystring['page']
			context['querystring'] = querystring.urlencode()
		return context	



class ArtFilterView(PaginatedFilterView, FilterView):
	filterset_class = ArtworkFilter
	template_name = 'met/art_filter.html'
	paginate_by = 20