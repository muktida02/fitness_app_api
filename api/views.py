from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
import pytz
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer


@api_view(["GET"])
def get_classes(request):
    tz = request.GET.get("timezone", "Asia/Kolkata")
    try:
        target_tz = pytz.timezone(tz)
    except Exception:
        return Response({"error": "Invalid timezone"}, status=status.HTTP_400_BAD_REQUEST)

    classes = FitnessClass.objects.all()
    data = []
    for cls in classes:
        # Convert datetime to requested timezone
        dt = timezone.localtime(cls.datetime, target_tz)
        formatted_datetime = dt.strftime("%Y-%m-%d %H:%M:%S %Z")

        data.append({
            "id": cls.id,
            "name": cls.name,
            "datetime": formatted_datetime,
            "instructor": cls.instructor,
            "available_slots": cls.available_slots,
        })

    return Response(data)



@api_view(["POST"])
def book_class(request):
    class_id = request.data.get("class_id")
    name = request.data.get("client_name")
    email = request.data.get("client_email")

    if not all([class_id, name, email]):
        return Response({"error": "Missing fields"}, status=400)

    try:
        fitness_class = FitnessClass.objects.get(id=class_id)
    except FitnessClass.DoesNotExist:
        return Response({"error": "Class not found"}, status=404)

    if fitness_class.available_slots <= 0:
        return Response({"error": "No slots available"}, status=400)

    booking = Booking.objects.create(
        fitness_class=fitness_class,
        client_name=name,
        client_email=email,
    )

    fitness_class.available_slots -= 1
    fitness_class.save()

    return Response(BookingSerializer(booking).data, status=201)


@api_view(["GET"])
def get_bookings(request):
    email = request.GET.get("email")
    if not email:
        return Response({"error": "Email is required"}, status=400)

    bookings = Booking.objects.filter(client_email=email)
    if not bookings:
        return Response({"error": "No bookings found"}, status=404)

    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

#adding a new class dynamically instead of only via seed data
@api_view(["POST"])
def add_class(request):
    serializer = FitnessClassSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

#Lets admin update slot count
@api_view(["PATCH"])
def update_slots(request, class_id):
    try:
        fitness_class = FitnessClass.objects.get(id=class_id)
    except FitnessClass.DoesNotExist:
        return Response({"error": "Class not found"}, status=404)

    slots = request.data.get("available_slots")
    if slots is None or int(slots) < 0:
        return Response({"error": "Invalid slots"}, status=400)

    fitness_class.available_slots = slots
    fitness_class.save()
    return Response(FitnessClassSerializer(fitness_class).data)


@api_view(["DELETE"])
def cancel_booking(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        return Response({"error": "Booking not found"}, status=404)

    # Restore slot
    booking.fitness_class.available_slots += 1
    booking.fitness_class.save()

    booking.delete()
    return Response({"message": "Booking cancelled successfully"})

#delete a Class 
@api_view(["DELETE"])
def delete_class(request, class_id):
    try:
        fitness_class = FitnessClass.objects.get(id=class_id)
    except FitnessClass.DoesNotExist:
        return Response({"error": "Class not found"}, status=404)

    fitness_class.delete()
    return Response({"message": "Class deleted successfully"})

#instructors/admin to view who booked their session of perticular class.
@api_view(["GET"])
def class_bookings(request, class_id):
    try:
        fitness_class = FitnessClass.objects.get(id=class_id)
    except FitnessClass.DoesNotExist:
        return Response({"error": "Class not found"}, status=404)

    bookings = Booking.objects.filter(fitness_class=fitness_class)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

