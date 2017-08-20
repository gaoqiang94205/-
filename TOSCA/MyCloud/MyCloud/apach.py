import pxssh

def sshop(userip):
    try:
        ssh=pxssh.pxssh()
        host=userip
        name='ec2-user'
        ssh.login(host,name,ssh_key='/home/gq/MyKey1.pem')

        ssh.sendline('sudo yum update -y')
        ssh.prompt()
        print(ssh.before)

        ssh.sendline('sudo yum groupinstall -y "Web Server" "MySQL Database" "PHP Support"')
        
        ssh.sendline('sudo yum install -y php-mysql')
        ssh.prompt()
        print ssh.before

        ssh.sendline('sudo service httpd start')
        ssh.prompt()
        print ssh.before

        ssh.sendline('sudo chkconfig httpd on')
        ssh.prompt()
        print ssh.before

        ssh.sendline('sudo service mysqld start')
        ssh.prompt()
        
        ssh.sendline('sudo mysql_secure_installation')
        ssh.prompt()
        print ssh.before
 
        ssh.sendline('sudo chkconfig mysqld on')
        ssh.prompt()
        print ssh.before
        ssh.logout()

    except pxssh.ExceptionPxssh, e:
        print('fail in operating!')
        print(str(e))
        return false
    return true
