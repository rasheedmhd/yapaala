from django.forms import ModelForm

from .models import Photo, House

class RoomListingForm(ModelForm):
	class Meta:
		model = House
		#fields = "__all__"
		exclude = ('slug', 'options',)
