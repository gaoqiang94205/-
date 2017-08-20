import boto.ec2
    
conn=boto.ec2.connect_to_region("us-west-2",aws_access_key_id='AKIAIVMTRX5MLUQE46EA',aws_secret_access_key='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')

image_id='ami-d0f506b0'
key_name='MyKey1'
instance_type='t2.micro'
security_group='sg-55c4ce32'

Reservation=conn.run_instances(image_id,key_name,instance_type, security_groups=[security_group])

ins=Reservation[0]
ins.add_tag(key='mycloud',value='mysql')
