from django.forms import ModelForm

from .models import Photo, House

class PhotoForm(ModelForm):
	class Meta:
		model = House
		fields = "__all__"
