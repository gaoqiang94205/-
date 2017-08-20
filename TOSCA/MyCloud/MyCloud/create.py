import os

os.system('aws cloudformation create-stack --stack-name awsstack --template-body file://meng.template')
