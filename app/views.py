from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':1000, 'b':200, 'c':100}
    return render(request,'condition.html',context=d)