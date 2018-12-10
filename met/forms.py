from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from met.models import Artwork

class ArtworkForm(forms.ModelForm):
	class Meta:
		model = Artwork
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'submit'))