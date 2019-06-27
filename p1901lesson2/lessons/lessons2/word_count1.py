
from pyspark import SparkConf, SparkContext
words = 'this is a letter forjohn, which described a girl loves him this is letter how are you'.split()
def filter_func(x):
    if x == 'letter':
        return None
    return x
sf = SparkConf().setMaster('spark://10.2.0.58:7077').setAppName('WordCount')
sc = SparkContext(conf=sf)
rdd = sc.parallelize(words)

rdd2 = rdd.filter(filter_func)
for x in rdd2.collect():
    print(x)

# rdd2 = rdd.Map(lambda x:(x, len(x)))
# for w in rdd2.collect():
#     print(w)

# rdd2 = rdd.flatMap(lambda x:((x, len(x)),(x, 1)))
# for w in rdd2.collect():
#     print(w)

# rdd2 = rdd.flatMap(lambda x: x)
# for w in rdd2.collect():
#      print(w)

# for x in rdd.distinct().collect():
#     print(x)
# pair_rdd = rdd.map(lambda x:(x, len(x)))
# def count_words(e):
#     key, value = e
#     return (key, len([m for m in value]))
#
# rdd1 = pair_rdd.groupByKey()
# rdd2 = rdd1.map(count_words)
# for x in rdd2.collect():
#     print(x)

sc.stop()