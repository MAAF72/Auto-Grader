import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()
channel.queue_declare(queue='submission', durable=True)

message = [1, 1, '6a6d5544-f2e8-455d-9691-789cdb25bb2f', 'C++', 1, 256, ['RestaurantNekoya (1)', 'RestaurantNekoya (2)', 'RestaurantNekoya (3)', 'RestaurantNekoya (4)', 'RestaurantNekoya (5)', 'RestaurantNekoya (6)', 'RestaurantNekoya (7)', 'RestaurantNekoya (8)', 'RestaurantNekoya (9)', 'RestaurantNekoya (10)']]
channel.basic_publish(
    exchange='',
    routing_key='submission',
    body=json.dumps(message),
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()
"""
dispatch = mengirim
persistent = tetap/kokoh, dalam hal ini message tidak akan lost
acknowledgment = balasan
"""
