from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':10000,'b':5000,'c':1000}
    return render(request,'jinja.html',context=d)