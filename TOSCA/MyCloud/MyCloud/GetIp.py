import boto.ec2

def getip():
    conn=boto.ec2.connect_to_region("us-west-2",aws_access_key_id='AKIAIVMTRX5MLUQE46EA',aws_secret_access_key='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')

    res=conn.get_only_instances(filters={'tag:aws:cloudformation:stack-name':'awswebstack'})
    for ins in res:
        ip = ins.ip_address
        if(ip is not None):
            return ip
    return "can't get ip"
