from django.shortcuts import render_to_response
from django.http import HttpResponse
import time
import insweb
import insmys
import lunch
import ssh

def show(request):
        return render_to_response("MyCloud3.html","a") 
def transf(request):
        info = request.GET.get('info')
        dia = request.GET.get('dia')
        li = request.GET.get('li')
        apa = request.GET.get('apa')
        ubu = request.GET.get('ubu')
        mys = request.GET.get('mys')
        if(dia is not None):
            dias = dia.split("and")
        ip = ""
        temp=1
        print(info)
        print(type(li))
        print(type(mys))
        if(info=="aws"):
                linux=lunch.lunch()
                ip=linux.ip_adress
                if((li =="linux1") and (apa =="apache1") and (mys =="mysql1")):
                    print('aaaaaaaaaaaaaaaaaaaaa')
                    if((ip !='') or (ip is not None)):
                        aa=ssh.sshop(ip)
                    if(not aa):
                        return HttpResponse('error')
                elif((li=="linux1" ) and (apa=="apache1")):
                    print('bbbbbbbbbbbbbbbbbb')
                    if((ip !='') or (ip is not None)):
                        bb=insweb.sshop(ip)
                    if(not bb):
                        return HttpResponse('error')
                elif(li=="linux1" and mys=="mysql1"):
                    print('cccccccccccccc')
                    if((ip !='') or (ip is not None)):
                        cc=insmys.sshop(ip)
                    if(not cc):
                        return HttpResponse('error')
                    print('mysql start') 
        return HttpResponse('ok the instance start')

