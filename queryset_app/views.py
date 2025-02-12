from django.shortcuts import render
from .models import Student,Teacher
# Create your views here.
 
# To retrive all query set object


# def home(request):
#     student_data=Student.objects.all()
#     print("Return:",student_data)
#     print("SQL Query:",student_data.query)
#     return render(request,'home.html',{'stu':student_data})


#To retrive queryset object with filter

# def home(request):
#     student_data=Student.objects.filter(marks=70)
#     print((student_data),"=============")
#     print("SQL Query:",student_data.query)
#     return render(request,'home.html',{'stu':student_data})

#To retrive queryset object with exclude

# def home(request):
#     student_data=Student.objects.exclude(marks=70)
#     print("Return:",student_data)
#     print("SQL Query:",student_data.query)
#     return render(request,'home.html',{'stu':student_data})
 

#TO retrive queryset object using order-by

# def home(request):
    # student_data=Student.objects.order_by('marks')
    # student_data=Student.objects.order_by('-marks')
    # student_data=Student.objects.order_by('?')
    # student_data=Student.objects.order_by('marks').reverse()[1:4]
    # student_data=Student.objects.values('name','city')
    # student_data=Student.objects.values()
    # student_data=Student.objects.values_list('id','name','city',named=True)
    # student_data=Student.objects.using('default')
    
    # qs1=Student.objects.values_list('name',named=True)
    # qs2=Teacher.objects.values_list('name',named=True)
    # student_data=qs1.union(qs2)
    # student_data=qs1.intersection(qs2)
    

    # print("Return:",student_data)
    # print("SQL Query:",student_data.query)
    # return render(request,'home.html',{'stu':student_data})
   
   
def about(request):
    student_data=Student.objects.last()
    
    student_data=Student.objects.get(pk=1)
    
    student_data=Student.objects.first()
    
    student_data=Student.objects.latest('pass_date')
    
    student_data=Student.objects.earliest('pass_date')
    
    student_data=Student.objects.all()
    print(student_data.exists())
    
    student_data=Student.objects.all()
    one_data=Student.objects.get(pk=1)
    print(student_data.filter(pk=one_data.pk).exists())
    
    student_data,created=Student.objects.get_or_create(name='Mansi',roll=106,city='bokaro',marks=70,pass_date='2020-5-4')
    print(created)
    

    student_data=Student.objects.create(name='Mansi',roll=106,city='bokaro',marks=70,pass_date='2020-5-4')
    
    student_data=Student.objects.filter(id=5).update(name='kabir',marks=80)
    
    student_data,created=Student.objects.update_or_create(id=3,name='nihal',defaults={'name':'prince'})
    print(created)
    
    
    objs=[
        Student(name='sanskriti',roll=107,city='sitapur',marks=75,pass_date='2020-5-6'),
        Student(name='kriti',roll=108,city='rampur',marks=92,pass_date='2020-6-6'),
        Student(name='sans',roll=109,city='lucknow',marks=72,pass_date='2020-2-6'),
        Student(name='sameer',roll=110,city='lakhimpur',marks=74,pass_date='2020-5-9'),
    ]
    student_data=Student.objects.bulk_create(objs)
    
    student_data=Student.objects.in_bulk([1,2])
    print(student_data[2].name)
    
    student_data=Student.objects.in_bulk([])
    
    student_data=Student.objects.in_bulk()
    
    student_data=Student.objects.get(pk=7).delete()
    student_data=Student.objects.filter(marks=70).delete()
    student_data=Student.objects.all().delete()
    
    
    student_data=Student.objects.all()
    print(student_data.count())
    

    student_data=Student.objects.all()
    print(Student.objects.all().explain())
    
    
    print("Return",student_data)
    return render(request,'about.html',{'student':student_data})
    
    
def about_student(request):
    student_data = Student.objects.all()
    
    student_data = Student.objects.filter(name__exact='ajay')  # Case-insensitive search
    
    student_data=Student.objects.filter(name__icontains='m')
    
    student_data=Student.objects.filter(id__in=[1,2,5])
    
    student_data = Student.objects.filter(marks__in=[72])
    
    student_data = Student.objects.filter(marks__gt=80)
    print("Return:", student_data)
    print("SQL Query:", student_data.query)
    return render(request, 'about.html', {'students': student_data})
