import pxssh

def sshop(userip,pwd,mydb,user,ip):
    try:
        ssh=pxssh.pxssh()
        host=userip
        name='ubuntu'
        ssh.login(host,name,ssh_key='/home/gq/mykey.pem')

        ssh.sendline('sudo apt-get update -y')
        ssh.prompt()
        print(ssh.before)

        ssh.sendline('sudo apt-get install -y mysql-server')
        

        ssh.sendline('sudo service mysql start')
        ssh.prompt()
        print ssh.before

        ssh.sendline('mysqladmin -u root password '+pwd)
        ssh.prompt()
        print ssh.before

        ssh.sendline('mysqladmin -u root -p'+pwd+' create '+mydb)
        ssh.prompt()
        print ssh.before

        ssh.sendline('mysql -uroot -p'+pwd+' -e CREATE USER '+user+'@'+ip+" IDENTIFY BY "+pwd)
        ssh.prompt()
        print ssh.before

        ssh.sendline('mysql -uroot -p'+pwd+' -e GRANT ALL ON '+mydb+'.* to '+user+'@'+ip)

        sh.logout()

    except pxssh.ExceptionPxssh, e:
        print('fail in operating!')
        print(str(e))
        return False
    return True
