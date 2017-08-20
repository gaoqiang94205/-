import pxssh

def sshop(userip):
    ssh=pxssh.pxssh()
    host=userip
    username='ec2-user'
    try:
        ssh.login(host,'ec2-user',ssh_key='/home/gq/MyKey1.pem',auto_prompt_reset=False)
        ssh.prompt()
        print ssh.before
        
        ssh.sendline('sudo yum update -y')
        ssh.prompt()
        print ssh.before
        
        ssh.sendline('sudo yum groupinstall -y "Web Server" "MySQL Database" "PHP Support"')
        ssh.prompt()
        print ssh.before
        
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
        print ssh.before
    except pxssh.Exception,e:
        print('fain in oroperating!')
        print(str(e))
