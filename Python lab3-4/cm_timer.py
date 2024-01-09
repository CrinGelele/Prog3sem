from time import time
from contextlib import contextmanager


class cm_timer1:
    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('time: ', time() - self.start_time, 's', sep='')


@contextmanager
def cm_timer2():
    start_time = time()
    try:
        yield
    finally:
        print('time: ', time() - start_time, 's', sep='')
