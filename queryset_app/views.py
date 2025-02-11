from django.shortcuts import render
from .models import Student,Teacher
# Create your views here.
 
# To retrive all query set object


def home(request):
    student_data=Student.objects.all()
    print("Return:",student_data)
    print("SQL Query:",student_data.query)
    return render(request,'home.html',{'stu':student_data})


#To retrive queryset object with filter

def home(request):
    student_data=Student.objects.filter(marks=70)
    print((student_data),"=============")
    print("SQL Query:",student_data.query)
    return render(request,'home.html',{'stu':student_data})

#To retrive queryset object with exclude

def home(request):
    student_data=Student.objects.exclude(marks=70)
    print("Return:",student_data)
    print("SQL Query:",student_data.query)
    return render(request,'home.html',{'stu':student_data})


#TO retrive queryset object using order-by

def home(request):
    student_data=Student.objects.order_by('marks')
    student_data=Student.objects.order_by('-marks')
    student_data=Student.objects.order_by('?')
    student_data=Student.objects.order_by('marks').reverse()[1:4]
    student_data=Student.objects.values('name','city')
    student_data=Student.objects.values()
    student_data=Student.objects.values_list('id','name','city',named=True)
    
    
    qs1=Student.objects.values_list('id','name',named=True)
    qs2=Teacher.objects.values_list('id','name',named=True)
    student_data=qs1.union(qs2)
    
    student_data=Student.objects.using('default')
    print("Return:",student_data)
    print("SQL Query:",student_data.query)
    return render(request,'home.html',{'stu':student_data})
   
    
    
    
    