from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Teacher
from .forms import RegisterForm, CreateGradeForm, CreateCourseForm, RegisterTeacherForm, AssignTeacherForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):

    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request, 'registeration_page.html', {'form': form})




def registerTeacher(request):

    teacher_form = RegisterTeacherForm()

    if request.method == "POST":
        teacher_form = RegisterTeacherForm(request.POST)

        if teacher_form.is_valid():
            teacher_form.save(commit=True)
            return index(request)
    return render(request, 'teacher_register_page.html', {'teacher_form': teacher_form})

def createGrade(request):

    grade_form = CreateGradeForm()

    if request.method == 'POST':
        grade_form = CreateGradeForm(request.POST)

        if grade_form.is_valid():
            grade_form.save(commit=True)
            return index(request)
    return render(request, 'create_grade.html', {'grade_form' : grade_form})


def createCourse(request):

    course_form = CreateCourseForm()

    if request.method == 'POST':
        course_form = CreateCourseForm(request.POST)

        if course_form.is_valid():
            course_form.save(commit=True)
            return index(request)
    return render(request, 'create_course.html', {'course_form' : course_form})

#class AssignTeacherView(ListView):
  #  model = Teacher
   # template_name = 'assign_teacher.html'

def assignTeacher(request):
    assign_teacher_form = AssignTeacherForm()
    if request.method == "POST":
        assign_teacher_form = AssignTeacherForm(request.POST)
        if assign_teacher_form.is_valid():
            assign_teacher_form.save(commit=True)
            return index(request)
    return render(request, 'assign_teacher.html', {'assign_teacher_form': assign_teacher_form})
    

    
    
