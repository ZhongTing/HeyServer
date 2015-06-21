from threading import Lock, Thread


class Notification():
    def __init__(self, throughput=5):
        self._throughput = throughput
        self._threads = dict()
        self._queue = list()
        self._lock = Lock()

        for i in range(throughput):
            self._threads[i] = Thread(target=self.execute)
            self._threads[i].start()

    def push(self, push_object):
        self._lock.acquire()
        self._queue.append(push_object)
        self._lock.release()
        for i in self._threads:
            if not self._threads[i].isAlive():
                self._threads[i] = Thread(target=self.execute)
                self._threads[i].start()
                break

    def execute(self):
        push_object = self._get_push_object()
        if push_object is not None:
            push_object.send()
            self.execute()

    def _get_push_object(self):
        push_object = None

        self._lock.acquire()
        if len(self._queue) > 0:
            push_object = self._queue[0]
            self._queue.remove(push_object)
        self._lock.release()

        return push_object