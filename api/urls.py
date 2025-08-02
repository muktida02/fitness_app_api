from django.urls import path
from . import views

urlpatterns = [
    path("classes/", views.get_classes),
    path("book/", views.book_class),
    path("bookings/", views.get_bookings),

    path("classes/add/", views.add_class),
    path("classes/<int:class_id>/update-slots/", views.update_slots),
    path("classes/<int:class_id>/bookings/", views.class_bookings),
    path("classes/<int:class_id>/delete/", views.delete_class),

    path("bookings/<int:booking_id>/cancel/", views.cancel_booking),
]
