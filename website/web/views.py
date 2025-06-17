from django.shortcuts import render,redirect
from .models import Student
def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        age=request.POST['age']
        s=Student.objects.create(name=name,age=age)
        s.save()
        return redirect('viewst')
    return render(request, 'web/register.html')
def viewst(request):
    students=Student.objects.all()
    return render(request, 'web/viewst.html',{'students':students})
# Create your views here.
def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('viewst')
def edit(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.save()
        return redirect('viewst')
    return render(request, 'web/register.html', {'student': student})
