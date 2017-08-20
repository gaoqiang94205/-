import os
import re

def filt(setip,dbname,user,pwd):
    patt1=re.compile('@Setip')
    patt2=re.compile('Setname')
    patt3=re.compile('Setuser')
    patt4=re.compile('Setpassword')
    patt5=re.compile('Setroot')

    temp=''
    file=open('/study/project/MyCloud/MyCloud/templates/mengsql.template')
    for line in file.readlines():
	    find1=patt1.search(line)
	    find2=patt2.search(line)
	    find3=patt3.search(line)
	    find4=patt4.search(line)
	    find5=patt5.search(line)
	
	    if(find1 is not None):
		    line=line.replace('@Setip','@'+setip)
		    print(line)
	    if(find2 is not None):
	            line=line.replace('Setname',dbname)
                    
	    if(find3 is not None):
	 	    line=line.replace('Setuser',user)
		    
	    if(find4 is not None):
		    line=line.replace('Setpassword',pwd)
		
	    if(find5 is not None):
		    line=line.replace('Setroot',pwd)
		    print(line)	
	    temp += line
	
    file.close();

    file=open('/study/project/MyCloud/MyCloud/mengsql.template','w')
    file.write(temp)
    file.close()
   
