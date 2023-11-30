import pika
import sys
import os
from dotenv import load_dotenv


def callback(ch, method, properties, body):
    print(f" [x] received {body.decode()}")
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
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
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='activity_tracking',
                          on_message_callback=callback)

    print('[*] waiting for messages. To exit press ctrl+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
