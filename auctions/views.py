from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing


def index(request):
    listings = Listing.objects.all()
    for listing in listings:
        print(listing.title)
        print(listing.description)
        print(listing.starting_bid)
        print(listing.is_closed)
        print(listing.url_image)
        print(listing.title)
        print(listing.user.username)
    return render(request, "auctions/index.html", {"listings": listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create_listing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST["starting-bid"]
        url_image = request.POST["url-image"]
        category = request.POST["category"]

        listing = Listing(title=title, description=description, starting_bid=starting_bid, url_image=url_image, category=category, user=request.user)
        listing.save()
        print(f'title: {title}\ndescription: {description}\nstarting bid: {starting_bid}\nurl image: {url_image}\ncategory: {category}\n')
        return render(request, "auctions/create_listing.html")
    else:
        listings = Listing.objects.all()
        print(f'Resultado del select: {listings[0].url_image}')
        return render(request, "auctions/create_listing.html")