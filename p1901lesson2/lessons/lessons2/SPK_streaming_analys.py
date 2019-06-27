from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
conf = SparkConf()
conf.setMaster('spark://10.0.2.58:7077')
conf.setAppName('Streaming Analysis')
conf.set('spark.executor.memory', '512m')
conf.set('spark.executor.cores', '2')

sc = SparkContext.getOrCreate(conf)
sc.setLogLevel('ERROR')

streaming = StreamingContext(sc, 2)
streaming.checkpoint('')
dstream = streaming.socketTextStream('127.0.0.1', 6000)
dstream = dstream.window(6, 2)
dstream = dstream.flatMap(lambda x: x.split())

dstream.pprint()

streaming.start()
streaming.awaitTermination()