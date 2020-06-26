from django.apps import AppConfig
from django.conf import settings
from .my_rabbits import AMQPConsuming

class MyAppConfig(AppConfig):
    name = 'datacenter'

    # see how in __init.py this config is called.
    # overriding ready
    def ready(self):
        try:
            if settings.ENABLE_RABBITMQ:
                print('using rabbits on '+str(settings.RABBIT_URL))
                consumer = AMQPConsuming()
                consumer.daemon = True
                consumer.start()
        except:
            print("no rabbits activated")
