
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopeHome"),
    path("aboutus/",views.about, name="AboutUs"),
    path("contactus/",views.contact, name="ContactUs"),
    path("tracker/",views.tracker, name="TrackingStatus"),
    path("search/",views.search, name="Search"),
    path("productview/",views.productView, name="Product"),
    path("checkout/",views.checkout, name="Checkout"),
]
