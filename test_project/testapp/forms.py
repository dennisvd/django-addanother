from django import forms

try:
	from django.core.urlresolvers import reverse_lazy
except ImportError:
	from django.urls import reverse_lazy

from django_addanother.widgets import AddAnotherWidgetWrapper, AddAnotherEditSelectedWidgetWrapper

from .models import Player


class PlayerForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PlayerForm, self).__init__(*args, **kwargs)
		self.fields['current_team'].widget.attrs['hidden'] = True

	class Meta:
		model = Player
		fields = ['name', 'current_team', 'future_team', 'previous_teams']
		widgets = {
			'current_team': AddAnotherWidgetWrapper(
				forms.Select(),
				reverse_lazy('add_team'),
			),
			'future_team': AddAnotherEditSelectedWidgetWrapper(
				forms.Select,
				reverse_lazy('add_team'),
				reverse_lazy('edit_team', args=['__fk__']),
			),
			'previous_teams': AddAnotherWidgetWrapper(
				forms.SelectMultiple,
				reverse_lazy('add_team'),
			)
		}
