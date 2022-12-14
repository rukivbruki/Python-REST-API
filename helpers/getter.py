import zlib

from settings import datastore_client


def get_name(name):
    key = datastore_client.key("Task", zlib.crc32(bytes(name, 'ascii')))

    task = datastore_client.get(key)

    if task:
        return dict(task)["value"]
    else:
        return f"{task}"


def get_stack(name):
    key = datastore_client.key("Stack", zlib.crc32(bytes(name, 'ascii')))
    task = datastore_client.get(key)
    print(task)
    return task["value"]
