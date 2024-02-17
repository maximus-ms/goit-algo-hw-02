from queue import Queue, Full, Empty
import time
import random
import numpy as np


class Order:
    def __init__(self, data=None) -> None:
        if data is None:
            data = random.randint(0, 0xFFFF)
        self.data = data

    def process(self):
        return True

    def __str__(self) -> str:
        return str(f"0x{self.data:0x}")


class ServiceCenter:
    def __init__(self, maxsize=0):
        self.q = Queue(maxsize)

    def generate_request(self, data=None):
        order = Order(data)
        try:
            self.q.put(order)
            print(f'Order "{order}" is added')
        except Full:
            print("Queue is full")

    def process_request(self):
        try:
            order = self.q.get(block=False)
            if order.process():
                print(f'Order "{order}" is processed')
        except Empty:
            print("Queue is empty")

    def service_loop(self):
        print("Service center")
        while True:
            time.sleep(1)
            if np.random.choice([True, False]):
                self.generate_request()
            if np.random.choice([True, False]):
                self.process_request()


def main():
    sc = ServiceCenter()
    sc.service_loop()


if __name__ == "__main__":
    main()
