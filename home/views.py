from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist, Artshow, Artwork, Style, Location, Contact, Customer
from .forms import NameForm
# Create your views here.
def index(request): 

    artists = Artist.objects.all()
    artshow = Artshow.objects.all()
    artwork = Artwork.objects.all()
    style = Style.objects.all()
    location = Location.objects.all()
    contact = Contact.objects.all()
    customer = Customer.objects.all()

    

    #return HttpResponse('Hello from home')
    return render(request, 'home/index.html')
    
#def get_title(request): 
#    if request.method == 'POST': 
#        form = NameForm(request.POST)
#        if form.is_valid():
#            myartists = Artist.objects.filter(name__exact=form.cleaned_data['search'])
#    context = {
#        'title' : 'Search Results',
#        'results' : myartists
#    }

#    return render(request, 'home/artists.html', context)

def artist(request): 
    artists = Artist.objects.all()

    if request.method =='POST':
        form = NameForm(request.POST)
        
        text = request.POST.get('title')
        
        if text != '':
            artists = Artist.objects.filter(artist__iexact=text)
        category = request.POST.get('category')
        sort = request.POST.get('sort')
        if category != '':
            if sort == 'ascending': 
                artists = artists.order_by(str(category))
            elif sort == 'descending': 
                artists = artists.order_by('-'+str(category))
    #artists = artists.order_by('artist')
        
    context = {
        'title' : 'Artist | Phone | Adress | Birthplace | Age | Style',
        'artists' : artists,
    }

    return render(request, 'home/artists.html', context)

def style(request): 
    styles = Style.objects.all()

    if request.method =='POST':
        form = NameForm(request.POST)
        #if form.is_valid():
        text = request.POST.get('title')
        if text != '':
            styles = Style.objects.filter(style__iexact=text)
        category = request.POST.get('category')
        sort = request.POST.get('sort')
        if category != '':
            if sort == 'ascending': 
                styles = styles.order_by(str(category))
            elif sort == 'descending': 
                styles = styles.order_by('-'+str(category))
    context = {
        'title' : 'Style | Popularity | Consultant',
        'styles' : styles
    }

    return render(request, 'home/styles.html', context)

def location(request): 
    locations = Location.objects.all()

    if request.method =='POST':
        form = NameForm(request.POST)
        #if form.is_valid():
        text = request.POST.get('title')
        if text != '':
            locations = Location.objects.filter(location__iexact=text)

        category = request.POST.get('category')
        sort = request.POST.get('sort')
        if category != '':
            if sort == 'ascending': 
                locations = locations.order_by(str(category))
            elif sort == 'descending': 
                locations = locations.order_by('-'+str(category))

    context = {
        'title' : 'Location | City | State',
        'locations' : locations
    }

    return render(request, 'home/locations.html', context)

def artwork(request): 
    artworks = Artwork.objects.all()

    if request.method =='POST':
        form = NameForm(request.POST)
        #if form.is_valid():
        text = request.POST.get('title')
        if text != '':
            artworks = Artwork.objects.filter(artwork__iexact=text)

        category = request.POST.get('category')
        sort = request.POST.get('sort')
        if category != '':
            if sort == 'ascending': 
                artworks = artworks.order_by(str(category))
            elif sort == 'descending': 
                artworks = artworks.order_by('-'+str(category))

    context = {
        'title' : 'Artwork | Artist | Created | Acquired | Price | Location',
        'artworks' : artworks
    }

    return render(request, 'home/artworks.html', context)

def contact(request): 
    contacts = Contact.objects.all()

    if request.method =='POST':
        form = NameForm(request.POST)
        #if form.is_valid():
        text = request.POST.get('title')
        if text != '':
            contacts = Contact.objects.filter(contact__iexact=text)

        category = request.POST.get('category')
        sort = request.POST.get('sort')
        if category != '':
            if sort == 'ascending': 
                contacts = contacts.order_by(str(category))
            elif sort == 'descending': 
                contacts = contacts.order_by('-'+str(category))

    context = {
        'title' : 'Contact | Phone | Email',
        'contacts' : contacts
    }

    return render(request, 'home/contacts.html', context)

def customer(request): 
    customers = Customer.objects.all()

    if request.method =='POST':
        form = NameForm(request.POST)
        #if form.is_valid():
        text = request.POST.get('title')
        if text != '':
            cutomers = Customer.objects.filter(customer__iexact=text)

        category = request.POST.get('category')
        sort = request.POST.get('sort')
        if category != '':
            if sort == 'ascending': 
                customers = customers.order_by(str(category))
            elif sort == 'descending': 
                customers = customers.order_by('-'+str(category))

    context = {
        'title' : 'Customer | Phone | Style',
        'customers' : customers
    }

    return render(request, 'home/customers.html', context)

def artshow(request): 
    artshows = Artshow.objects.all()

    if request.method =='POST':
        form = NameForm(request.POST)
        #if form.is_valid():
        text = request.POST.get('title')
        if text != '':
            artshows = Artshow.objects.filter(artshow__iexact=text)

        category = request.POST.get('category')
        sort = request.POST.get('sort')
        if category != '':
            if sort == 'ascending': 
                artshows = artshows.order_by(str(category))
            elif sort == 'descending': 
                artshows = artshows.order_by('-'+str(category))

    context = {
        'title' : 'Artshow | Artists | Artworks | Date/Time | Location | Contact | Customers',
        'artshows' : artshows
    }

    return render(request, 'home/artshows.html', context)