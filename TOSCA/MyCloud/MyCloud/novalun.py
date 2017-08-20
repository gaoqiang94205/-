from novaclient.client import Client

def lunch():
    p = {}
    p['username'] = "meng@g2.usc.edu.tw"
    p['api_key'] = "62996299aB@"
    p['auth_url'] = "https://compute.datacentred.io:5000"
    p['project_id'] = "mengg2uscedutw_primary"

    nova = Client('2', **p)
    #floating_ip = nova.floating_ips.create(nova.floating_ip_pools.list()[0].name)
    image = nova.images.find(name="Ubuntu 14.04")
    flavor = nova.flavors.find(name="dc1.1x1.80")

    server = nova.servers.create(name='mytest',image=image.id,flavor=flavor.id,key_name='mykey',security_groups=['mysqlgp'])
    server.add_floating_ip('185.98.149.59 ',fixed_address=None)
