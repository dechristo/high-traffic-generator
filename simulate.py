from threading import Thread
import queue
import requests

concurrent_requests = 200
num_threads = 4
url = 'url here'
post_body = {}


def make_request(q):
    while not q.empty():
        current = q.get()
        print(f'request {current} sent.')
        requests.post(url, json=post_body)
        q.task_done()


q = queue.Queue(concurrent_requests * num_threads)

for index in range(concurrent_requests):
    q.put(index)

for threadIndex in range(num_threads):
    t = Thread(target=make_request, args=(q,))
    t.daemon = True
    t.start()

q.join()


