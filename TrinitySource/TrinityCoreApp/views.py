from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from sympy import Symbol, Derivative
from sympy.core.symbol import Str
import TrinityCoreApp
# x+(3*y*z)

x=Symbol('x')
y=Symbol('y')
z=Symbol('z')
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def version(request):
    return render(request,'version.html')

def text(request):
    return render(request,'text.html')

def submitquery(request):

    expression=request.GET['expression']
    price=request.GET['price']
    String=''
    String+=str("level :0 "+str(expression.split(' ')))
    list=expression.split('+')
    String+=str("level :1 "+str(list))
    sample=[]
    for j in range(1,(len(expression)-len(list))):
        sample=[]
        for i in list:
            dfx= Derivative(i, x).doit()
            dfy= Derivative(i, y).doit()
            dfz= Derivative(i, z).doit()
            if dfx!=0:
                sample.append(dfx)
            if dfy!=0:
                sample.append(dfy)
            if dfz!=0:
                sample.append(dfz)
        list=sample    
        String+=str("level :"+str(j+1)+" "+str(sample))
    # html = "<html><body>%s</body></html>" % String
    # return HttpResponse(html)
    context={"value":String}
    return render(request,'calculation.html',context)