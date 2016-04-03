from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
import time
from models import *

time.sleep(15)

producer = KafkaProducer(bootstrap_servers='kafka:9092')
es = Elasticsearch(['es'])

for blog_post in BlogPost.objects.all():
	some_new_listing = {'title': blog_post.title, 'body': blog_post.body, 'id': blog_post.pk}
	producer.send('new-listings-topic', json.dumps(some_new_listing).encode('utf-8'))

consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])

while True:
	for message in consumer:
		new_listing = json.loads((message.value).decode('utf-8'))
		es.index(index='listing_index', doc_type='listing', id=new_listing['id'], body=new_listing)
		es.indices.refresh(index='listing_index')