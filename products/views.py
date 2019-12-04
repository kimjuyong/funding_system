from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Car
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "cars"


class CarDetail(DetailView):

    """ CarDetail Definition """

    model = models.Car


class SearchView(View):

    """ SearchView Definition """

    def get(self, request):

        country = request.GET.get("manufactureCountry")

        if country:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                car_model = form.cleaned_data.get("car_model")
                country = form.cleaned_data.get("manufactureCountry")
                car_type = form.cleaned_data.get("car_type")
                guests = form.cleaned_data.get("guests")
                seats = form.cleaned_data.get("seats")
                efficiency = form.cleaned_data.get("efficiency")
                instant_book = form.cleaned_data.get("instant_book")
                facility = form.cleaned_data.get("facility")

                filter_args = {}

                if car_model != "Anything":
                    filter_args["car_model__startswith"] = car_model

                filter_args["manufactureCountry"] = country

                if car_type is not None:
                    filter_args["car_type"] = car_type

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if seats is not None:
                    filter_args["seats__gte"] = seats

                if efficiency is not None:
                    filter_args["efficiency__gte"] = efficiency

                if instant_book is True:
                    filter_args["instant_book"] = True

                for f in facility:
                    filter_args["facility"] = f

                qs = models.Car.objects.filter(**filter_args).order_by("created")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                cars = paginator.get_page(page)

                return render(
                    request, "products/search.html", {"form": form, "cars": cars}
                )
        else:
            form = forms.SearchForm()

        return render(request, "products/search.html", {"form": form})

