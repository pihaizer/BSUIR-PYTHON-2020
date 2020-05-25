import time
from multiprocessing import Process, Queue
import queue
import logging

from django.core.mail import EmailMessage

started = False
message_queue = Queue()


def send(subject, message, to):
    if not started:
        start()
    message_queue.put(EmailMessage(subject, message, to=to))


def process_message(q):
    while True:
        try:
            message = q.get_nowait()
        except queue.Empty:
            time.sleep(1)
            continue
        else:
            message.send()


def start(number_of_processes=4):
    for w in range(number_of_processes):
        p = Process(target=process_message, args=(message_queue,))
        p.daemon = True
        p.start()

    global started
    started = True
