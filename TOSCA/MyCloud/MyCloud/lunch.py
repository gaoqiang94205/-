import boto.ec2

def lunch():
    result=''
    image_id='ami-d0f506b0'
    key_name='MyKey1'
    instance_type="t2.micro"
    security_group='Fd3-linux-WebServerSecurityGroup-WSBRHRB7SGU8'
    try:   
        conn=boto.ec2.connect_to_region("us-west-2",aws_access_key_id='AKIAIVMTRX5MLUQE46EA',aws_secret_access_key='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')
        Reservation=conn.run_instances(image_id=image_id,key_name=key_name,instance_type=instance_type,security_groups=[security_group])
    except Exception as e:
        result='no'
        print('error')
        print(str(e))
    if(result!='no'):
        ins=Reservation.instances[0]
        ins.add_tag(key='mycloud',value='mysql')
        print('aaaaaaa')
        result=ins
    return result
