from django.shortcuts import render, HttpResponse
from listings.models import Listing
from listings.choices import state_choices, bedroom_choices, price_choices
from realtor.models import Realtor


def home(request):
	listing = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
	context = {

		'listing':listing,
		'state_choices':state_choices,
		'bedroom_choices':bedroom_choices,
		'price_choices':price_choices,
		


	}


	return render(request, 'index.html', context)


def about(request):
	realtor = Realtor.objects.order_by('-hire_date')
	mvp_realtor = Realtor.objects.all().filter(is_mvp=True)
	return render(request, 'about.html', {'realtor':realtor, 'mvp_realtor':mvp_realtor})


