from django.shortcuts import render , HttpResponse ,redirect
from .models import Complaint



def home(request):
    if request.method == "POST":
        name = request.POST['name']
        area = request.POST['area']
        desc = request.POST['desc']


        print("Name:",name)
        print("Area:",area)
        print("Coplaint:",desc)

        Complaint.objects.create(
            name = name,
            area = area,
            description = desc
        )
    data = Complaint.objects.all()
    return render(request, 'home.html',{'data':data})
  

def delete_complaint(request, id):
    data = Complaint.objects.get(id=id)
    data.delete()
    return redirect('/')


def edit_complaint(request, id):
    data = Complaint.objects.get(id=id)

    if request.method == "POST":
        data.name = request.POST['name']
        data.area = request.POST['area']
        data.description = request.POST['desc']
        data.status = request.POST['status']
        data.save()

    return redirect('/')