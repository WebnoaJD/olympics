from django.contrib import admin
from .models import AboutJO, Legal, Sport, Event, Offer
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import io
import urllib, base64
from django.urls import path
from django.http import HttpResponse


@admin.register(AboutJO)
class AboutJOAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Legal)
class LegalAdmin(admin.ModelAdmin):
    list_display = ('name', 'editor_name', 'editor_website', 'utilisation', 'active')

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('complete_name', 'sport', 'time', 'standard_price')
    exclude = ('complete_name',)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'sales_count_display')

    def sales_count_display(self, obj):
        return obj.count_sales()
    sales_count_display.short_description = 'Sales Count'

    def changelist_view(self, request, extra_context=None):
        # Récupérer toutes les offres
        offers = Offer.objects.all()
        
        # Vérifier si des offres existent
        if offers.exists():
            # Extraire les données des offres
            offer_data = [
                {
                    'name': offer.name,
                    'sales_count': offer.count_sales()
                }
                for offer in offers
            ]
            df = pd.DataFrame(offer_data)

            # Création du graphique avec Matplotlib
            plt.figure(figsize=(10, 6))
            df.plot(kind='bar', x='name', y='sales_count')
            plt.title('Histogramme des ventes par offre')
            plt.xlabel('Nom de l\'offre')
            plt.ylabel('Nombre de ventes')
            plt.xticks(rotation=45, ha='right')
            plt.yticks(range(0, 21, 1))
            plt.tight_layout()

            # Enregistrement du graphique dans une image PNG
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            string = base64.b64encode(buf.read())
            uri = 'data:image/png;base64,' + urllib.parse.quote(string)
            plt.close()  # Fermez la figure pour éviter les fuites de mémoire
            
            extra_context = extra_context or {}
            extra_context['chart'] = uri
        else:
            # Pas d'offres, vous pouvez ajouter un message ou une valeur par défaut
            extra_context = extra_context or {}
            extra_context['chart'] = None  # ou un message indiquant qu'il n'y a pas de données

        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('sales_chart/', self.admin_site.admin_view(self.changelist_view), name='sales_chart'),
        ]
        return custom_urls + urls