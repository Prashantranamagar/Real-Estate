from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from .choices import state_choices,bedroom_choices, price_choices
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def listings(request):
	listings= Listing.objects.order_by('-list_date').filter(is_published=True)
	page = request.GET.get('page', 1)
	paginator = Paginator(listings, 3)

	try:
		lists = paginator.page(page)
	except PageNotAnInteger:
		lists = paginator.page(1)
	except EmptyPage:
		lists = paginator.page(paginator.num_pages)
 
	return render(request, 'listings.html', {'lists':lists, 'listings':listings})



	

def listing_detail(request, id): 
	listing = get_object_or_404(Listing, pk=id)

	return render(request, 'listings_detail.html', {'listing':listing})

def search(request):
	lists = Listing.objects.order_by('-list_date')

	# Keywords
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			lists = lists.filter(desdription__icontains=keywords)

	 # City
	if 'city' in request.GET:
		city = request.GET['city']
		if city:
	  		lists = lists.filter(city__iexact=city)

	  # State
	if 'state' in request.GET:
		state = request.GET['state']
		if state:
	  		lists = lists.filter(state__iexact=state)

	  # Bedrooms
	if 'bedrooms' in request.GET:
	  	bedrooms = request.GET['bedrooms']
	  	if bedrooms:
	  		lists = lists.filter(bedrooms__lte=bedrooms)

	  # Price
	if 'price' in request.GET:
	  	price = request.GET['price']
	  	if price:
	  		lists = lists.filter(price__lte=price)

	context = {
	'state_choices': state_choices,
	'bedroom_choices': bedroom_choices,
	'price_choices': price_choices,
	'lists': lists,
	'values': request.GET
	}	


	return render(request, 'search.html', context)