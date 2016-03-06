
import boto

sqs_port = 9324
sqs_endpoint = '192.168.1.110'
region = boto.sqs.regioninfo.RegionInfo(name='elasticmq', endpoint=sqs_endpoint)
conn = boto.connect_sqs(aws_access_key_id='x',aws_secret_access_key='x',is_secure=False,port=sqs_port,region=region)

# Create Queue
q = conn.create_queue('myqueue')

# List all Queues
conn.get_all_queues()

# Get the Queue
my_queue = conn.get_queue('myqueue')
print my_queue

# Writing a message

from boto.sqs.message import Message
m = Message()
m.set_body('This is my first message.')
q.write(m)

# You can define the message body as a JSON String with using JSON
import json
dis = {}
dis['id'] = 123
name = {}
name['lastName'] = 'Chiu'
name['firstName'] = 'Felix'
dis['name'] = name
dis['phone'] = '(650) 603-0170'
k = json.dumps(dis)
m = Message()
m.set_body(k)
q.write(m)
