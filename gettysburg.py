"""
A sample program to illustrate text processing and some commom programming best practices.

Mark Foley,
Feb. 2019
"""
import string
from utilities.read_from_file_or_net import get_stuff_from_net as gn
from utilities.read_from_file_or_net import read_any_text_file as rf

# Variables to hold file URLs
SPEECH_URL = "http://193.1.33.31:88/pa1/gettysburg.txt"
STOPWORDS_URL = "http://193.1.33.31:88/pa1/stopwords.txt"
SPEECH_FILE = "data/gettysburg.txt"
STOPWORDS_FILE = "data/stopwords.txt"


def parse_text(speech, stopwords):
    stopwords = stopwords.strip().split(",")
    speech = speech.strip().split()
    cleaned_speech = []
    unique_words = set()
    word_count = {}

    for word in speech:
        word = word.strip(string.punctuation)
        if word.lower() in stopwords:
            continue
        if word:
            cleaned_speech.append(word.lower())
            unique_words.add(word.lower())

            if word in word_count:
                word_count[word.lower()] += 1
            else:
                word_count[word.lower()] = 1

    return cleaned_speech, unique_words, word_count


def try_net_version():
    """
    Tasks:
    1. Get speech from Internet OR from local files
    2. Get stopwords from Internet OR from local files
    3. Look at these -- inspect, print, whatever.
    4. Chop speech into words.
    5. Get rid of punctuation.
    6. Make sure every word is lowercase

    :return: speech, stopwords
    """
    try:
        speech = gn(SPEECH_URL)
        stopwords = gn(STOPWORDS_URL)

        process_speech(speech, stopwords)

    except Exception as e:
        print(f"{e}")


def process_speech(speech, stopwords):
    cleaned_speech, unique_words, word_count = parse_text(speech, stopwords)

    print("Results - Number of words: {}\nNumber of unique words: {}\n\nWord Counts:".format(
        len(cleaned_speech), len(unique_words)
    ))
    for k, v in word_count.items():
        print("{}: {}".format(k, v))


def try_file_version():
    try:
        speech = rf(SPEECH_FILE)
        stopwords = rf(STOPWORDS_FILE)

        process_speech(speech, stopwords)
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    try:
        print(f"From {SPEECH_URL}.\n")
        try_net_version()
    except Exception as e:
        print(f"Couldn't get {SPEECH_URL} from NET.\n{e}")
    finally:
        print("=" * 50)

    try:
        print(f"From {SPEECH_FILE}.\n")
        try_file_version()
    except Exception as e:
        print(f"Couldn't read {SPEECH_FILE}.\n{e}")
    finally:
        print("=" * 50)

