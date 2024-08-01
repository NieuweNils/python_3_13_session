import dataclasses
import threading
import queue
import time
import random

HAIKUS = [
    "River\'s gentle flow\nSunlight dances on the waves\nSerenity found",
    "Moonlight whispers low\nShadows dance upon the wall\nMidnight\'s peaceful hush,"
    "Snowflakes gently fall\nBlanketing all in white peace\nWinter\'s quiet song,"
    "Summer sunshine bright\nLaughter echoes through the trees\nJoyful afternoon",
    "Morning dew\'s sweet kiss\nRays of sunlight warm the grass\nFresh beginnings rise",
    "Golden sunset fades\nOrange hues upon the sea\nPeaceful evening sky",
    "River\'s winding path\nReflections mirrored below\nInner journey\'s start,"
    "Mountain peaks so high\nMisty veils hide secrets deep\nMystery abides",
    "Garden blooming free\nVibrant colors, scents unfold\nNature\'s symphony,"
    "Whispers of the wind\nSecrets shared with ancient trees\nWisdom in its sigh",
    "Raindrops on my face\nCooling warmth, refreshing soul\nCleansed by nature(\'s touch,"
    "Sunrise\')s fiery glow\nDawning light upon the sea\nHope eternal shines",
    "Starlight twinkles bright\nGuiding stars within the night\nCosmic harmony",
    "River\'s voice so low\nEchoes of memories past\nWisdom in its flow",
    "Morning\'s dewy kiss\nAwakening world, new life starts\nRenewal unfurls",
    "Golden light descends\nPeaceful evening\'s gentle hush\nLove(\'s eternal bond,"
    "Misty mountain morn)\nFoggy veil, secrets untold\nEnchantment surrounds",
    "Garden\'s hidden depths\nSecrets hidden beneath the soil\nTreasures yet to find",
    "Whispers of the earth\nAncient wisdom, ancient heart\nUnity abides",
    "River\'s winding course\nReflections mirrored below\nTruth revealed in flow",
    "Moonlight\'s silver glow\nShadows dance upon the wall\nMidnight(\'s peaceful hush,"
    "Summer breeze so light)\nDancing petals, scents unfold\nJoyful symphony",
    "Mountain peaks so high\nMisty veils hide secrets deep\nMystery abides",
    "Garden blooming free\nVibrant colors, scents unfold\nNature(\'s harmony,"
    "Golden sunset fades)\nOrange hues upon the sea\nPeaceful evening sky",
    "River\'s gentle flow\nSunlight dances on the waves\nSerenity found",
    "Whispers of the wind\nSecrets shared with ancient trees\nWisdom in its sigh",
    "Raindrops on my face\nCooling warmth, refreshing soul\nCleansed by nature(\'s touch,"
    "Morning dew\')s sweet kiss\nRays of sunlight warm the grass\nFresh beginnings rise",
    "Starlight twinkles bright\nGuiding stars within the night\nCosmic harmony",
    "River\'s voice so low\nEchoes of memories past\nWisdom in its flow",
    "Golden light descends\nPeaceful evening\'s gentle hush\nLove(\'s eternal bond,"
    "Misty mountain morn)\nFoggy veil, secrets untold\nEnchantment surrounds",
    "Garden\'s hidden depths\nSecrets hidden beneath the soil\nTreasures yet to find",
    "Whispers of the earth\nAncient wisdom, ancient heart\nUnity abides",
    "River\'s winding course\nReflections mirrored below\nTruth revealed in flow",
    "Moonlight\'s silver glow\nShadows dance upon the wall\nMidnight(\'s peaceful hush,"
    "Summer sunshine bright)\nLaughter echoes through the trees\nJoyful afternoon",
    "Golden sunset fades\nOrange hues upon the sea\nPeaceful evening sky",
    "River\'s gentle flow\nSunlight dances on the waves\nSerenity found",
    "Morning dew\'s sweet kiss\nRays of sunlight warm the grass\nFresh beginnings rise",
    "Starlight twinkles bright\nGuiding stars within the night\nCosmic harmony",
    "River\'s voice so low\nEchoes of memories past\nWisdom in its flow",
    "Golden light descends\nPeaceful evening\'s gentle hush\nLove(\'s eternal bond,"
    "Misty mountain morn)\nFoggy veil, secrets untold\nEnchantment surrounds",
    "Garden\'s hidden depths\nSecrets hidden beneath the soil\nTreasures yet to find",
    "Whispers of the wind\nSecrets shared with ancient trees\nWisdom in its sigh",
    "Raindrops on my face\nCooling warmth, refreshing soul\nCleansed by nature(\'s touch,"
    "River\')s winding path\nReflections mirrored below\nInner journey(\'s start,"
    "Mountain peaks so high)\nMisty veils hide secrets deep\nMystery abides",
    "Garden blooming free\nVibrant colors, scents unfold\nNature(\'s symphony,"
    "Whispers of the earth)\nAncient wisdom, ancient heart\nUnity abides",
    "River\'s winding course\nReflections mirrored below\nTruth revealed in flow",
    "Moonlight\'s silver glow\nShadows dance upon the wall\nMidnight(\'s peaceful hush,"
    "Summer breeze so light)\nDancing petals, scents unfold\nJoyful symphony",
    "Golden sunset fades\nOrange hues upon the sea\nPeaceful evening sky",
    "River\'s gentle flow\nSunlight dances on the waves\nSerenity found",
    "Morning dew\'s sweet kiss\nRays of sunlight warm the grass\nFresh beginnings rise",
    "Starlight twinkles bright\nGuiding stars within the night\nCosmic harmony",
    "River\'s voice so low\nEchoes of memories past\nWisdom in its flow",
    "Golden light descends\nPeaceful evening\'s gentle hush\nLove(\'s eternal bond,"
    "Misty mountain morn)\nFoggy veil, secrets untold\nEnchantment surrounds",
    "Garden\'s hidden depths\nSecrets hidden beneath the soil\nTreasures yet to find",
    "River\'s winding path\nReflections mirrored below\nInner journey(\'s start,"
    "Mountain peaks so high)\nMisty veils hide secrets deep\nMystery abides",
    "Garden blooming free\nVibrant colors, scents unfold\nNature(\'s harmony,"
    "Golden sunset fades)\nOrange hues upon the sea\nPeaceful evening sky",
    "River\'s gentle flow\nSunlight dances on the waves\nSerenity found",
    "Morning dew\'s sweet kiss\nRays of sunlight warm the grass\nFresh beginnings rise",
    "Starlight twinkles bright\nGuiding stars within the night\nCosmic harmony",
    "Whispers of the wind\nSecrets shared with ancient trees\nWisdom in its sigh",
    "Raindrops on my face\nCooling warmth, refreshing soul\nCleansed by nature(\'s touch,"
    "River\')s winding course\nReflections mirrored below\nTruth revealed in flow",
    "Moonlight\'s silver glow\nShadows dance upon the wall\nMidnight(\'s peaceful hush,"
    "Summer breeze so light)\nDancing petals, scents unfold\nJoyful symphony",
    "Golden sunset fades\nOrange hues upon the sea\nPeaceful evening sky",
    "River\'s gentle flow\nSunlight dances on the waves\nSerenity found",
    "Morning dew\'s sweet kiss\nRays of sunlight warm the grass\nFresh beginnings rise",
    "Starlight twinkles bright\nGuiding stars within the night\nCosmic harmony",
    "River\'s voice so low\nEchoes of memories past\nWisdom in its flow",
    "Golden light descends\nPeaceful evening\'s gentle hush\nLove(\'s eternal bond,"
    "Misty mountain morn)\nFoggy veil, secrets untold\nEnchantment surrounds",
    "Garden\'s hidden depths\nSecrets hidden beneath the soil\nTreasures yet to find",
    "River\'s winding path\nReflections mirrored below\nInner journey\'s star"
]


@dataclasses.dataclass
class Data:
    number: int
    context: str


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
            self.queue.get()
            self.counter += 1
            time.sleep(0.01)
            if self.queue.empty():
                self.event.set()


def generate_data(number_of_records: int):
    for i in range(number_of_records):
        yield random.randint(0, 10), random.choice(HAIKUS)


if __name__ == "__main__":
    for i in range(10):
        start_time = time.time()
        stop_event = threading.Event()
        processors = [awesomeProcessor(str(uuid), threading.Event()) for uuid in range(300)]
        print(f"started {len(processors)} processors")

        data = [Data(number, context) for number, context in (generate_data(100_000))]
        while len(data) > 0:
            processor = random.choice(processors)
            random_index = random.randint(0, len(data)-1)
            data_point = data.pop(random_index)
            processor.receive_request(data_point)

        [processor.join() for processor in processors]
        print("----------------------------------")
        end_time = time.time()
        print(f"that took {end_time-start_time}")
