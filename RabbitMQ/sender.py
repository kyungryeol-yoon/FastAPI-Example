from datetime import datetime
import pika

HOST_NAME = "localhost"
QUEUE_NAME = "snowdeer_queue"


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST_NAME))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)

    msg = f"[{datetime.now()}] hello, snowdeer !!"
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=msg)
    print(f"Sent message.\n{msg}")
    connection.close()


if __name__ == '__main__':
    main()