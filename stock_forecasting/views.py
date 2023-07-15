import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from src.pipelines.prediction_pipeline import predict
import pandas as pd 
import os

@csrf_protect
def home(request):
    if request.method=="POST":
        company=request.POST.get('company')
        select=request.POST.get("select")
        key=company.split("(")[0]
        key=key.strip()
        obj=predict(key,select)
        test,pred,next=obj.make_prediction()
        df=pd.read_csv(os.path.join("artifacts",'stcoks.csv'))
        labels=list(df['Unnamed: 0'])[70:]
        data=json.dumps({"pred":pred,"labels":labels,"actual":test})
        return render(request,'index.html',{"arr":data,"next":next[0],"company":company})
    return render(request,"index.html",{"arr":{"pred":[],"labels":[],"actual":[]}})

