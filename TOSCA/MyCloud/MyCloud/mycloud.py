from django.shortcuts import render_to_response
import os

def show(request):
	return render_to_response("MyCloud3.html",'a') 
def transf(request):
	info = request.GET.get('info')
        dia = request.GET.get('dia')
        li = request.GET.get('li')
        apa = request>GET.get('apa')
        ubu = request.GET.get('ubu')
        mys = request.GET.get('mys')
        info = dia.split("and")

        if(info=="aws"):
        	if(li!="" and apa!="" and mys!=""):
                	os.system('aws cloudformation create-stack --stack-name awsstack --template-body file://meng.template')

                elif(li!="" and apa!=""):
     	        	os.system('aws cloudformation create-stack --stack-name awsstack --template-body file://mengweb.template')

                elif(li!="" and mys!=null):
                	os.system('aws cloudformation create-stack --stack-name awsstack --template-body file://mengsql.template')



