import json
import pika
import os
from dotenv import load_dotenv
from random import choice, randrange

# This line brings all environment variables from .env into os.environ
load_dotenv()
credentials = pika.PlainCredentials(
    os.environ.get('RABBITMQ_USER'), os.environ.get('RABBITMQ_PASS'))
parameters = pika.ConnectionParameters(
    os.environ.get('RABBITMQ_HOST'),
    os.environ.get('RABBITMQ_PORT'), '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='activity_tracking', durable=True)

events = ['login', 'logoff', 'order_success', 'order_failed', 'payment']
user = randrange(1000, 10000)

# Simulates an event
event_data = {'user_id': user, 'event_type': choice(events)}
channel.basic_publish(exchange='',
                      routing_key='activity_tracking',
                      body=json.dumps(event_data),
                      properties=pika.BasicProperties(
                          delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                      ))

print(f"[x] Sent {event_data}")

connection.close()
