from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from sympy import Symbol, Derivative,degree_list
from sympy.core.symbol import Str
import bnlearn as bn
import pandas as pd
import os
import re
import TrinityCoreApp
import json
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

def pretify(str,arr):
    final = """{i}(0): {val1} ||  {i}(1): {val2}""".format(i=str,val1=arr[0],val2=arr[1])
    return final

def submitquery(request):
    df = pd.read_excel('static/sample.xlsx',sheet_name='DataSet1')
    edges = [('WAC Price Change', 'Direct Sale Variance'),
    ('Contract Boundary Reached', 'Direct Sale Variance'),
    ('Price Program Boundary Reached', 'Direct Sale Variance')
    ]

    DAG = bn.make_DAG(edges)
    # bn.print_CPD(DAG)
    DAG1 = bn.parameter_learning.fit(DAG, df, methodtype='maximumlikelihood')

    predict_WAC_wrt_DirectSales1 = bn.inference.fit(DAG1, variables=['WAC Price Change'],
    evidence={'Direct Sale Variance':1})

    predict_ContractBoundary_wrt_DirectSales1 = bn.inference.fit(DAG1, variables=['Contract Boundary Reached'],
    evidence={'Direct Sale Variance':1})

    predict_PriceProgram_wrt_DirectSales1 = bn.inference.fit(DAG1, variables=['Price Program Boundary Reached'],
    evidence={'Direct Sale Variance':1})

    expression=request.GET['expression']
    price=request.GET['price']
    String=''
    String+=str("level :0  "+str(expression.split(' ')))  + '|' 
    lis=expression.split('+')
    String+=str("level :1  "+str(lis))  + '|' 
    sample=[]
    # sum(list(map(sum, list(degree_list(expression)))))
    level=sum(list(degree_list(expression)))
    for j in range(1,level):
        sample=[]
        for i in lis:
            dfx= Derivative(i, x).doit()
            dfy= Derivative(i, y).doit()
            dfz= Derivative(i, z).doit()
            if dfx!=0:
                sample.append(dfx)
            if dfy!=0:
                sample.append(dfy)
            if dfz!=0:
                sample.append(dfz)
        lis=sample
        String+=str("level :"+str(j+1)+"  "+str(sample)) + '|'  
    
    max_probability_value=max(predict_WAC_wrt_DirectSales1.values[1],predict_ContractBoundary_wrt_DirectSales1.values[1],predict_PriceProgram_wrt_DirectSales1.values[1])
    probString=''

    predict_WAC_wrt_DirectSales1_values =[ '%.2f' % elem for elem in predict_WAC_wrt_DirectSales1.values]
    predict_ContractBoundary_wrt_DirectSales1_values = [ '%.2f' % elem for elem in predict_ContractBoundary_wrt_DirectSales1.values]
    predict_PriceProgram_wrt_DirectSales1_values = [ '%.2f' % elem for elem in predict_PriceProgram_wrt_DirectSales1.values]
    max_probability_value_temp = format(max_probability_value,".2f")

    if max_probability_value_temp in predict_WAC_wrt_DirectSales1_values:
        probString="WAC Price Change"
    if max_probability_value_temp in predict_ContractBoundary_wrt_DirectSales1_values:
        probString="Contract Boundary"
    if max_probability_value_temp in predict_PriceProgram_wrt_DirectSales1_values:
        probString="Price Program Boundary"

    path=os.getcwd()
    final_path=path+"\static\{i} table.csv".format(i=probString)
    df = pd.read_csv(final_path,usecols =['Contract_ID','Program_ID','Start_Date','End_Date'])
    df_final=df
    filtered_df = df_final[(df_final['End_Date']=="Jun-21")]
    json_record=filtered_df.to_json(orient ='records')
    data = []
    data = json.loads(json_record)

    context={"value":String,
    "WAC":pretify("WAC Price Change",predict_WAC_wrt_DirectSales1.values),
    "Contract":pretify("Contract Boundary",predict_ContractBoundary_wrt_DirectSales1.values),
    "PriceProgram":pretify("Price Program Boundary",predict_PriceProgram_wrt_DirectSales1.values),
    "maxProbabilityList":probString,
    "maxProbability":format(max_probability_value*100,".3f"),
    'd': data
    }
    return render(request,'calculation.html',context)  
    

def PlotDiagram(request):
    df = pd.read_excel('static/sample.xlsx',sheet_name='DataSet1')
    edges = [('WAC Price Change', 'Direct Sale Variance'),
    ('Contract Boundary Reached', 'Direct Sale Variance'),
    ('Price Program Boundary Reached', 'Direct Sale Variance')
    ]

    DAG = bn.make_DAG(edges)
    # bn.print_CPD(DAG)
    DAG1 = bn.parameter_learning.fit(DAG, df, methodtype='maximumlikelihood')
    bn.plot(DAG1)
    return render(request,'home.html')  

