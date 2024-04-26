from django.shortcuts import render

# Create your views here.
from app.forms import StudentForm

def Std_info(request):
    form=StudentForm()
    d={'form':form}
    return render(request,'result.html',d)