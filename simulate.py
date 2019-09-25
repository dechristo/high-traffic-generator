from threading import Thread
import queue
import requests

concurrent_requests = 200
num_threads = 4


def make_request(q):
    while not q.empty():
        current = q.get()
        print(f'request {current} sent.')
        requests.post('http://localhost:3000/applications/telco/graphql',
            json={'query': '{getCitiesByPostCode(postCode: "12107"){cityName}}'})
        q.task_done()


q = queue.Queue(concurrent_requests * num_threads)

for index in range(concurrent_requests):
    q.put(index)

for threadIndex in range(num_threads):
    t = Thread(target=make_request, args=(q,))
    t.daemon = True
    t.start()

q.join()


