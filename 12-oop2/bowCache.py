import pylru
from base import main
from bowInverted import BOWInvertedIndexEngine


class LRUCache(object):
    def __init__(self, size=32):
        self.cache = pylru.lrucache(size)

    def has(self, key):
        return key in self.cache

    def get(self, key):
        return self.cache[key]

    def set(self, key, value):
        self.cache[key] = value


class BOWInvertedIndexEngineWithCache(BOWInvertedIndexEngine, LRUCache):
    def __init__(self):
        super(BOWInvertedIndexEngineWithCache, self).__init__()
        LRUCache.__init__(self)

    def search(self, query):
        if self.has(query):
            print('cache hit!')
            return self.get(query)

        print('not in cache')
        result = super(BOWInvertedIndexEngineWithCache, self).search(query)
        self.set(query, result)

        return result

if __name__ == "__main__":
    search_engine = BOWInvertedIndexEngineWithCache()
    main(search_engine)