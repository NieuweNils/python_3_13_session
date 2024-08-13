import dataclasses
import threading
import queue
import time
import random
from typing import List

from data import haikus

HAIKUS = haikus()


@dataclasses.dataclass
class Data:
    number: int
    context: str


def calculate_fibonacci_sequence(n):
    return n if n < 2 else calculate_fibonacci_sequence(n - 2) + calculate_fibonacci_sequence(n - 1)


class awesomeProcessor(threading.Thread):
    def __init__(self, uuid: str, event: threading.Event):
        super().__init__(name=f"Data Processor {uuid}", daemon=False, args=(event,))
        self.queue: queue.Queue[Data] = queue.Queue()
        self.event = event
        self.counter = 0
        self.start()

    def receive_request(self, data: Data):
        self.queue.put(data, block=False)

    # Overrides threading.Thread.run()
    def run(self):
        while not self.event.is_set():
            data_to_process = self.queue.get()
            self.counter += 1
            calculate_fibonacci_sequence(data_to_process.number)
            if self.queue.empty():
                self.event.set()


def generate_data(number_of_records: int) -> (int, str):
    for _ in range(number_of_records):
        yield random.randint(20, 25), random.choice(HAIKUS)


if __name__ == "__main__":
    for i in range(10):
        start_time = time.time()
        stop_event = threading.Event()
        processors = [awesomeProcessor(str(uuid), threading.Event()) for uuid in range(8)]
        print(f"started {len(processors)} processors")

        data = [Data(number, context) for number, context in (generate_data(3_000))]
        print(f"processing {len(data)} data points")
        while len(data) > 0:
            processor = random.choice(processors)
            random_index = random.randint(0, len(data) - 1)
            data_point = data.pop(random_index)
            processor.receive_request(data_point)

        [processor.join() for processor in processors]
        print("----------------------------------")
        end_time = time.time()
        print(f"that took {end_time - start_time}")
