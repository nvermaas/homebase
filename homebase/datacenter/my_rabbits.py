import threading

import pika
from django.conf import settings

class AMQPConsuming(threading.Thread):
    def callback(self, ch, method, properties, body):
        # do something
        print('receiving rabbits :'+str(body))

        # send back acknowledgement of the message
        ch.basic_ack(delivery_tag=method.delivery_tag)

    @staticmethod
    def _get_connection():
        parameters = pika.URLParameters(settings.RABBIT_URL)
        return pika.BlockingConnection(parameters)

    def run(self):
        connection = self._get_connection()
        channel = connection.channel()

        # declare my (temporary queue) and bind it to the correct exchange
        channel.exchange_declare(exchange='homebase', exchange_type='fanout')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange='homebase', queue=queue_name)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=queue_name, on_message_callback=self.callback)

        channel.start_consuming()