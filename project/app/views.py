from django.shortcuts import render, redirect, get_object_or_404
from .forms import OfferForm, EventFilterForm
from .models import AboutJO, Legal, Event, Offer, Sport
from django.http import JsonResponse
from django.template.loader import render_to_string



def home_view(request):
    events = Event.objects.all().order_by('time')
    abouts = AboutJO.objects.all()
    return render(request, 'app/home.html',  {
        'title': 'Jeux Olympiques de Paris 2024',
        'events' : events,
        'abouts' : abouts,
    }
)
    
def offers_view(request):
    form = EventFilterForm(request.GET)
    events = Event.objects.select_related('sport')
    offers = Offer.objects.all()
    sports = Sport.objects.distinct()
    
    if form.is_valid():
        city = form.cleaned_data.get('city')
        sport = form.cleaned_data.get('sport')
        if city:
            events = events.filter(location__city=city)
        if sport:
            events = events.filter(sport=sport)       
    if not form.is_valid():
        print(form.errors)  
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_to_string('app/event-list.html', {'events': events}, request=request)
        return JsonResponse({'html': html})

    context = {
        'form': form,
        'events': events,
        'title': 'Offres',
        'offers': offers,
        'sports': sports,
        'events': events,
        'form': form,  
    }
    return render(request, 'app/offers.html', context)

def event_offers_view(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    offers = Offer.objects.all()
    form = OfferForm(request.POST or None)
        
    return render(request, 'app/event-offers.html', {
        'title': "Billeterie",
        'event': event,
        'offers': offers,
        'form': form,
    })
    
    
def add_to_cart(request):
    if request.method == 'POST':
        event = request.POST.get('event_id')
        offer = request.POST.get('offer_id')
        ticket_nb = request.POST.get('offer_ticket_nb')

        cart = request.session.get('cart', [])
        cart.append({
            'event': event,
            'offer': offer,
            'ticket_nb': ticket_nb,
        })
        request.session['cart'] = cart
        return redirect('cart_view')


def calculate_discounted_price(price, discount):
    if price is None:
        raise ValueError("Le prix ne peut pas être None")
    if discount is None or not (0 <= discount <= 100):
        raise ValueError("La remise doit être comprise entre 0 et 100")
    return price * (1 - discount / 100)


def cart_view(request):
    cart = request.session.get('cart', [])
    detailed_cart = []
    total_price = 0

    for item in cart:
        try:
            event = Event.objects.get(id=item['event'])
            offer = Offer.objects.get(id=item['offer'])
        except Event.DoesNotExist:
            return render(request, 'error_page.html', {'error_message': f"L'événement avec ID {item['event']} n'existe pas."})
        except Offer.DoesNotExist:
            return render(request, 'error_page.html', {'error_message': f"L'offre avec ID {item['offer']} n'existe pas."})

        standard_price = event.standard_price
        discount = offer.discount
        ticket_nb = offer.ticket_nb

        try:
            by_ticket_price = calculate_discounted_price(standard_price, discount)
        except ValueError as e:
            return render(request, 'error_page.html', {'error_message': str(e)})

        offer_price = ticket_nb * by_ticket_price
        total_price += offer_price

        detailed_cart.append({
            'event_time': event.time,
            'event_complete_name': event.complete_name,
            'event_location': event.get_location_display(),
            'event_sport': event.sport,
            'offer_name': offer.name,
            'offer_ticket_nb': offer.ticket_nb,
            'offer_price': offer_price
        })

    request.session['total_price'] = float(total_price)
    formatted_total_price = format(total_price, '.2f')

    return render(request, 'app/cart.html', {
        'cart': detailed_cart,
        'title': 'Panier',
        'total_price': formatted_total_price
    })


    
def remove_from_cart(request):
    if request.method == 'POST':
        item_index = int(request.POST.get('item_index'))
        cart = request.session.get('cart', [])
        if 0 <= item_index < len(cart):
            del cart[item_index]
            request.session['cart'] = cart
        return redirect('cart_view')
    return redirect('cart_view')

def about_view(request):
    abouts = AboutJO.objects.all()
    return render(
        request, 
        'app/about.html',
        {
            'title': 'Jeux Olympiques',
            'about': abouts,
        }
)



def legal_view(request):
    legal = Legal.objects.filter(active=True)
    return render(
        request, 
        'app/legal_mentions.html',
        {
            'title': 'Mentions légales',
            'legal': legal,
        }
)
