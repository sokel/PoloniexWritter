import pika


def callback(ch, method, properties, body):
    print(" [x] %r" % (body,))

while True:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # channel.queue_declare(queue='hello')
    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)
    channel.start_consuming()