from django.shortcuts import render
from .forms import RegisterForm
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