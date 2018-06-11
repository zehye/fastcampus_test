from django.shortcuts import render
from .models import School, Student


def school_list(request):
    school = School.objects.all()
    context = {
        'school': school,
    }

    return render(request, 'education/school_list.html', context)


def school_detail(request, school_id):
    schools = School.objects.get(id=school_id)

    context = {
        'schools': schools,
    }
    return render(request, 'education/school_detail.html', context)


def student_list(request):
    student = Student.objects.all()
    context = {
        'student': student,
    }

    return render(request, 'education/student_list.html', context)


def student_detail(request, student_id):
    students = Student.objects.get(id=student_id)
    context = {
        'students': students
    }

    return render(request, 'education/student_detail.html', context)
