from pyspark import SparkContext, SparkConf

conf = SparkConf()
conf.setMaster('spark://10.0.2.58:7077')
conf.setAppName('spark.app.name', 'MBA')
conf.set('spark.executor.memory', '512m')
conf.set('spark.executor.cores', '2')
sc = SparkContext
rdd = sc.textFile('/Users/rimi/Desktop/p1901lesson2/lessons/lessons2/transaction.txt')


def combine(s, n):
    def _iterator(collector, s, i, c, n, data=None):
        if c >= n:
            collector.append(list(data))
            return

        for x in range(i, len(s)):
            data.append(s[x])
            _iterator(collector, s, x + 1, c + 1, n, data)
            data.pop()

    data_set = []
    chars = []
    _iterator(data_set, s, 0, 0, n, chars)
    return data_set
