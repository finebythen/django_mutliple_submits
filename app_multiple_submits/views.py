from django.shortcuts import render, redirect

from .forms import CarForm, PersonForm
from .models import Car, Person


def main(request):
    # database-querys
    car_db = Car.objects.all()
    person_db = Person.objects.all()

    # form one
    form_car = CarForm()

    # form two
    form_person = PersonForm()

    # request form one
    if request.method == 'POST':
        form_car = CarForm(request.POST, request.FILES)
        form_person = PersonForm(request.POST, request.FILES)
        if form_car.is_valid():
            form_car.save()
            return redirect("Main")
        elif form_person.is_valid():
            form_person.save()
            return redirect("Main")
        else:
            pass

    context = {'car_db': car_db, 'person_db': person_db, 'form_car': form_car, 'form_person': form_person}
    return render(request, 'app_multiple_submits/main.html', context)
