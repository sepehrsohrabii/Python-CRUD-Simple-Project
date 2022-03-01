from django.shortcuts import render
from .models import Student
from .forms import StudentsForm


def main_page(request):
    student = Student.objects.all()
    context = {}
    form = StudentsForm(request.POST or None)
    context['form'] = form
    context["datalist"] = Student.objects.all()
    print(request.POST)

    for student.student_number in student:
        this_student = student.student_number

        if '{}delete'.format(this_student) in request.POST:
            Student.objects.filter(student_number=this_student).delete()

        if '{}edit'.format(this_student) in request.POST:
            student = Student.objects.filter(student_number=this_student).get()
            name = student.name
            this = Student(name=name, student_number=this_student)
            form = StudentsForm(instance=this)
            context['form'] = form
            Student.objects.filter(student_number=this_student).delete()

    if 'save' in request.POST and not Student.objects.filter(student_number=request.POST['student_number']).exists():
        if form.is_valid():
            form.save()

    return render(request, "main_page.html", context)
