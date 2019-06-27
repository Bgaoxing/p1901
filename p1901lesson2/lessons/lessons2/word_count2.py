from pyspark import SparkConf, SparkContext
words = 'this is a letter forjohn, which described a girl loves him this is letter how are you'.split()
sf = SparkConf().setMaster("spark://10.2.0.58:7077").setAppName("WordCount")
sc = SparkContext.getOrCreate(sf)
sc.setLogLevel("ERROR")
rdd = sc.parallelize(words)
rdd = rdd.map(lambda x: (x, x + "1"))

rdd1 = rdd.mapValues(lambda v: [v, v])

for x in rdd1.values().collect():
    print(x)

print("There are %d elements" % rdd1.count())

print(rdd1.top(5))
print(rdd1.first())
print(rdd1.take(5), rdd1.takeOrdered(5))

def foreach_cb(x):
    print("*", x, type(x[1]))
    x[1].append("***")

rdd1.foreach(f=foreach_cb)
for w in rdd1.collect():
    print(w)

def combiner(a):
    return [a]

def merge_func(a, b):
    a.append(b)
    return a

def merge_combiner(a, b):
     a.extend(b)
     return a

def values_cb(x):
    return str(x) + "*"

for w in rdd.combineByKey(combiner, merge_func, merge_combiner).collect():
    print(w)

print("Do groupByKey")
for w in rdd.groupByKey().collect():
    print(w[0], [x for x in w[1]])


for x in rdd.mapValues(f=values_cb).collect():
    print(x)

