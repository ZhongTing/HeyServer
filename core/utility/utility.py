import sys
import uuid


class Utility():
    def __init__(self):
        pass

    @staticmethod
    def hash_to_key(content):
        if content is None:
            return content
        # print content, hash(content) % sys.maxsize
        return hash(content) % sys.maxsize

    @staticmethod
    def generate_token():
        return str(uuid.uuid4()).replace("-", "")
