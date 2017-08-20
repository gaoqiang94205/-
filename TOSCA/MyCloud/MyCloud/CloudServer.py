from django.shortcuts import render_to_response
from django.http import HttpResponse
import re
import os
import filemoud
import GetIp
import time
import GetPointIp

def show(request):
        return render_to_response("MyCloud3.html","a") 
def transf(request):
        info = request.GET.get('info')
        dia = request.GET.get('dia1')
        li = request.GET.get('li')
        apa = request.GET.get('apa')
        ubu = request.GET.get('ubu')
        mys = request.GET.get('mys')
        if(dia is not None):
            dias = dia.split("and")
        ip = ""
        temp=1
        flag=''
        print(info)
        print(dias[0])
        print(dias[0]=='gq')
        print(mys)
        print(ubu=='')



        if(info=="aws"):
                if((li=='linux1') and (apa=='apache1') and (mys=='mysql1')):
                   flag='one'
                   os.system('aws cloudformation create-stack --stack-name awsstack --template-body file:///study/project/MyCloud/MyCloud/templates/meng.template')
              
                elif((li=='linux1') and (apa=='apache1')):
                        os.system('aws cloudformation create-stack --stack-name awswebstack --template-body file:///study/project/MyCloud/MyCloud/templates/myweb.template')
                        flag='two' 
                        print('bbbbbbbbbbbbbbbbbbbbbb')
                elif((li=='linux1') and (mys=='mysql1')):
                        tt=1
                        ip=GetIp.getip()
                        print(ip)
                        print(temp)
                        while(ip=="can't get ip"):
                            print(ip)
                            time.sleep(8)
                            tt+=1
                            if(tt>3):
                                return HttpResponse('error')
                        if(ip != "can't get ip"):
                            print('mysql start') 
                            filemoud.filt(ip,dias[0],dias[1],dias[2])
                            os.system('aws cloudformation create-stack --stack-name awssqlstack --template-body file:///study/project/MyCloud/MyCloud/templates/mengsql.template')
                        else:
                            return HttpResponse('the ip is null,you should create webserver first!')

        def check(flag):
                testip=GetPointIp.getip(flag)
                test=1
                while(testip=="can't get ip"):
                    if(test<5):
                        testip=GetPointIp.getip(flag)
                        test+=1
                        time.sleep(10)
                if(testip=="can't get ip"):
                    return HttpResponse("<html><head>Sorry fail in lunching !</head><body><h1>there is something wrong during lunch,please check your web!<b1><br><br><a href='/show'>try it again,click here.</a></html>")      
        if(flag=='one'):
                check('awsstack')
        if(flag=='two'):
                check('awswebstack')
        return HttpResponse('successfuly')

        
