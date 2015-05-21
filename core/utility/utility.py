import sys


class Utility():
    def __init__(self):
        pass

    @staticmethod
    def hash_to_key(content):
        if content is None:
            return content
        # print content, hash(content) % sys.maxsize
        return hash(content) % sys.maxsize