import pika
import json
import sqlite3
import oop_grader as grader
from os import path

DB_FILE = path.join('..', 'website', 'db.sqlite3')
DB_CON = None

def callback(ch, method, properties, body):
    print(' [x] Received new submission')
    try:
    
        id, score, status = grader.Submission(json.loads(body)).judge()
        DB_CON.cursor().execute(
            '''
            UPDATE
                apps_submission
            SET
                score = ?,
                status = ?
            WHERE
                id = ?
            ''',
            (score, status, id)
        )
        print(' [x] Submission ID : {}, Status : {}, Score : {}'.format(id, status, score))
        print(' [x] Done')
    except Exception as e:
        print(body)
        print(' [x] Error :', e)
    print()
    ch.basic_ack(delivery_tag=method.delivery_tag)

try:
    DB_CON = sqlite3.connect(DB_FILE, isolation_level=None)
    
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )

    channel = connection.channel()
    #channel.queue_delete(queue='submission') kalau diaktifasi, yg pending ga bakal di judge
    channel.queue_declare(queue='submission', durable=True)

    print(' [*] Waiting for submissions. To exit press CTRL+C')
    
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='submission', on_message_callback=callback)

    channel.start_consuming()
    
except sqlite3.Error as error:
    print('Error while connecting to database', error)
except KeyboardInterrupt:
    pass
except Exception as error:
    print(error)
else:
    if DB_CON.is_connected():
        DB_CON.cursor().close()
        DB_CON.close()
        print('Database connection is closed.')
