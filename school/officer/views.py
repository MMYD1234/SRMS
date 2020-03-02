from django.shortcuts import render
from .forms import RegisterForm
from teacher.forms import RegisterTeacherForm
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

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request, 'teacher_register_page.html', {'teacher_form': teacher_form})