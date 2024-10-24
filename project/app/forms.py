from django import forms
from .models import Offer, Event, Sport

class OfferForm(forms.Form):
    offer = forms.ModelChoiceField(
        queryset=Offer.objects.all(),
        required=False, 
        label="Sélectionner une offre",
    )
                            
    number = forms.IntegerField(
        widget=forms.Select(choices=[(i, i) for i in range(1, 11)]),
        required=False, 
        label="Nombre d'offre")

    def __init__(self, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        self.fields['offer'].queryset = Offer.objects.all()
        self.fields['number'].widget.attrs.update({'class': 'form-control'}) 

class EventFilterForm(forms.Form):
    sport = forms.ModelChoiceField(
        queryset=Sport.objects.filter(
            id__in=Event.objects.values_list('sport_id', flat=True).distinct()
        ),
        required=False, 
        empty_label="Indifférent"
    )