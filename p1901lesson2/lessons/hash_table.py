from sys import getrefcount

from gglib.link import list


class HashTable:
    def __init__(self, size):
        links = list()
        self.size = size
        for i in range(size):
            links.append(list())

        self.links = tuple(links)

    def __get_hash_id_by_key(self, key):
        assert isinstance(key, bytes)
        sum = 0
        for k in key:
            sum += k
        return sum % self.size

    def put(self, key, value):
        hash_id = self.__get_hash_id_by_key(key.encode("utf-8"))
        link = self.links[hash_id]
        link.append((key, value))
        # link.insert(0, (key, value))

    def get(self, key):
        hash_id = self.__get_hash_id_by_key(key.encode("utf-8"))
        link = self.links[hash_id]
        for l in link:
            if l[0] == key:
                return l[1]
        raise KeyError

    def __delitem__(self, key):
        hash_id = self.__get_hash_id_by_key(key.encode("utf-8"))
        link = self.links[hash_id]
        value = self.get(key)
        link.remove((key, value))

    def __del__(self):
        print("object is ding")


def func():
    h = HashTable(10)
    print(getrefcount(h))


if __name__ == "__main__":
    func()
    import time
    time.sleep(1)

    # h.put("name", "zhangshan")
    # h.put("age", 19)
    #
    # print("name = {}".format(h.get("name")))
    # print("age = {}".format(h.get("age")))
    #
    # m = h
    # print(getrefcount(h))
    # del m
    # print(getrefcount(h))
    # del h
    # print(getrefcount(h))
    #
    #
    # print("name = {}".format(h.get("name")))
