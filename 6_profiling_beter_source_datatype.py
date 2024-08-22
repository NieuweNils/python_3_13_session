import dataclasses
import random
from typing import List

from string_search_algorithms import aho_corasick
from string_search_algorithms import rabin_karp
from string_search_algorithms import linear_search
from data import haikus

HAIKUS = haikus()
POETIC_WORDS = ["warm", "flow", "dance", "sweet", "on", "ancient", "secrets"]


@dataclasses.dataclass
class Data:
    number: int
    context: List[str]


def calculate_fibonacci_sequence(n: int) -> int:
    return n if n < 2 else calculate_fibonacci_sequence(n - 2) + calculate_fibonacci_sequence(n - 1)


def find_occurrences(sentence_list: List[str], word_to_find: str):
    sentences = " ".join(sentence_list)
    words = sentences.split(" ")
    words.count(word_to_find)


def generate_data(number_of_records: int) -> (float, List[str]):
    for _ in range(number_of_records):
        yield random.randint(15, 20), HAIKUS


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
