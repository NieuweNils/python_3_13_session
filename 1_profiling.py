import dataclasses
import random
from typing import List

from data import haikus
from string_search_algorithms import rabin_karp

HAIKUS = haikus()
POETIC_WORDS = ["warm", "flow", "dance", "sweet", "on", "ancient", "secrets"]


@dataclasses.dataclass
class Data:
    number: float
    context: List[str]


def calculate_fibonacci_sequence(n: float):
    return n if n < 2 else calculate_fibonacci_sequence(n - 2) + calculate_fibonacci_sequence(n - 1)


def find_occurrences(sentence_list: List[str], word_to_find: str):
    sentences = " ".join(sentence_list)
    rabin_karp(sentences, word_to_find)  # O(nˆc)


def generate_data(number_of_records: int) -> (float, List[str]):
    for _ in range(number_of_records):
        yield random.random() * 5 + 15, HAIKUS


if __name__ == "__main__":
    data = [Data(number, context) for number, context in (generate_data(10_000))]
    print(f"processing {len(data)} data points..")
    while len(data) > 0:
        random_index = random.randint(0, len(data) - 1)
        data_point = data.pop(random_index)
        word = random.choice(POETIC_WORDS)
        calculate_fibonacci_sequence(data_point.number)
        find_occurrences(sentence_list=data_point.context, word_to_find=word)
    print("done!")
