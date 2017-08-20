import pxssh

def sshop(userip,pwd,mydb,user,ip):
    try:
        ssh=pxssh.pxssh()
        host=userip
        name='ec2-user'
        ssh.login(host,name,ssh_key='/home/gq/AkaciaKey.pem')

        ssh.sendline('sudo yum update -y')
        ssh.prompt()
        print(ssh.before)

        ssh.sendline('sudo yum install -y mysql-server')
        ssh.prompt()
        print(ssh.before)

        ssh.sendline('sudo chkconfig mysqld on')
        ssh.prompt()
        print ssh.before

        ssh.sendline('sudo service mysqld start')
        ssh.prompt()
        print ssh.before

        ssh.sendline('mysqladmin -u root password '+pwd)
        ssh.prompt()
        print ssh.before
 
        ssh.sendline('mysqladmin -u root -p"'+pwd+'" create '+mydb)
        ssh.prompt()
        print ssh.before

#       ssh.sendline('mysql -uroot -p"'+pwd+'" -e"CREATE USER '+user+'@'+ip+" IDENTIFY BY "+pwd+'"')
 #       ssh.prompt()
#        print ssh.before

#        ssh.sendline('mysql -uroot -p"'+pwd+'" -e"GRANT ALL ON '+mydb+'.* to user@'+ip+'"')
#        ssh.prompt()
#        print ssh.before

        ssh.logout()


    except pxssh.ExceptionPxssh, e:
        print('fail in operating!')
        print(str(e))
        return False
    return True
