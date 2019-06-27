from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = 'python3'

conf = SparkConf().setMaster("spark://10.02.0.58:7077").setAppName("ML")
sc = SparkContext.getOrCreate(conf)
sc.setLogLevel("ERROR")

red_points = [(1.13, 2.23), (1.0, 1.9), (0.7, 1.5), (1.5, 1.33), (1.13, 1.1), (1.3, 1.5), (0.97, 1.43), (1.4, 1.83),
              (1.33, 2.0), (1.23, 1.77), (1.97, 1.63), (1.67, 2.1), (1.43, 2.23), (2.13, 2.07), (1.7, 1.67),
              (1.63, 1.8), (1.7, 1.3), (1.57, 1.5), (2.0, 1.73), (1.77, 1.9)]
blue_points = [(1.07, 0.47), (1.7, 0.63), (2.37, 0.33), (2.67, 0.8), (2.2, 0.8), (1.77, 0.47), (2.03, 0.9), (1.87, 0.6),
               (1.43, 0.47), (1.73, 0.23), (2.13, 0.5), (2.07, 0.7), (1.57, 0.4), (1.43, 0.23), (1.4, 0.53),
               (1.77, 0.57), (2.03, 0.67), (2.23, 0.77), (2.37, 0.83), (2.57, 0.67), (2.57, 0.5), (2.4, 0.53),
               (2.23, 0.37), (2.03, 0.33), (1.87, 0.33), (2.13, 0.47), (2.27, 0.53), (2.5, 0.53), (2.63, 0.67),
               (1.93, 0.77), (1.6, 0.57), (1.53, 0.67), (1.9, 0.8)]

red_labeled_points = []
for x, y in red_points:
    point = LabeledPoint(1, (x, y))
    red_labeled_points.append(point)

blue_labeled_points = []
for x, y in blue_points:
    point = LabeledPoint(0, (x, y))
    blue_labeled_points.append(point)

m = LogisticRegressionWithSGD.train(sc.parallelize(red_labeled_points + blue_labeled_points))
print(m.predict((1.5, 0.5)))