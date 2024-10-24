from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from users.models import Order
from django.utils import timezone


class AboutJO(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Nom de l'article")
    text = models.TextField(max_length=200, blank=True, verbose_name="Paragraphe")
    image = models.ImageField(upload_to="about/", blank=True, null=True, verbose_name="Image")
    image_description = models.CharField(max_length=100, blank=True, verbose_name="Description de l'image")
    image_credit = models.CharField(max_length=100, blank=True, default="Image générée par l'IA", verbose_name="Crédit")

    class Meta:
        verbose_name = ("À propos des JO")
        verbose_name_plural = ("À propos des JO")
        
    def __str__(self):
        return self.name

class Legal(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name="Nom de la version")
    editor_name = models.CharField(max_length=255, blank=True, default="", verbose_name="Nom de l'éditeur")
    editor_website = models.URLField(max_length=200, blank=True, default="", verbose_name="Site web de l'éditeur")
    utilisation = models.CharField(max_length=255, blank=True, default="", verbose_name="Utilisation")
    host_name = models.CharField(max_length=255, blank=True, default="", verbose_name="Nom de l'hébergeur")
    host_address = models.TextField(blank=True, null=True, default="", verbose_name="Adresse de l'hébergeur")
    host_website = models.URLField(max_length=200, blank=True, verbose_name="Site hébergeur")
    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.active:
            # Définir tous les autres enregistrements comme non actifs
            Legal.objects.filter(active=True).update(active=False)
            # Note: Ce code désactivera toutes les autres instances, y compris celle qui était précédemment active.
        super(Legal, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = ("Mentions légales")
        verbose_name_plural = ("Mentions légales")
        
    def __str__(self):
        return self.name 

class Sport(models.Model):
    name = models.CharField(max_length=100, verbose_name="Intitulé")
    
    class Meta:
        verbose_name = "Sport"
    
    def __str__(self):
        return self.name  
         
class Event(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name="Nom de l'épreuve")
    CHOICES = [
        ('a', ''),
        ('b', 'féminin'),
        ('c', 'masculin'),
    ]
    genre = models.CharField(max_length=10, choices=CHOICES, default='a', verbose_name="Genre")
    complete_name = models.CharField(max_length=200, blank=True, verbose_name="Épreuve")
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='events', verbose_name="Sport")
    time = models.DateTimeField(default=timezone.now, verbose_name="Date et horaire de début")
    LOCATION_CHOICES = [
        ('a', 'Arena Champs de Mars'),
        ('b', 'Invalides '),
        ('c', 'Hôtel de Ville de Paris'),
        ('d', 'La Concorde'),
    ]
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES, default='a', verbose_name="Lieu")
    standard_price = models.PositiveIntegerField(default=15, verbose_name="prix standard en €")
    
    class Meta:
        verbose_name = "Épreuve"
        
    def save(self, *args, **kwargs):
        self.complete_name = f"{self.name} {self.get_genre_display()}".strip()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.complete_name
    
    
    
class Offer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Intitulé")
    description = models.TextField(blank=True, verbose_name="Description de l'offre")
    ticket_nb = models.IntegerField(default=0, verbose_name="Nombre de billets auquel l'offre ouvre droit")
    discount = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        blank=True, 
        null=True, 
        verbose_name="Remise sur le billet unitaire (%)",
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
        
    class Meta:
        verbose_name = "Offre"
    
    def __str__(self):
        return self.name
    
    def count_sales(self):
        return Order.objects.filter(offer_name=self.name, payment_key='HAS_PAID').count()
