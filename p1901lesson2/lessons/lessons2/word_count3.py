from pyspark import SparkContext, SparkConf
import csv, StringIO

conf = SparkConf().setMaster("spark://10.2.3.41:7077").setAppName("SPK_file")
sc = SparkContext.getOrCreate(conf)
sc.setLogLevel("ERROR")


# 将整个CSV文本文件转换成字典列表
def mapToDict(f):
    _, text = f
    input = StringIO.StringIO(text)
    csv_reader = csv.DictReader(input)
    users = []
    for line in csv_reader:
        users.append(line)
    return users


csvRDD = sc.wholeTextFiles("file:///media/psf/Home/Workspace/Rimi/P1901/lessons/spark/users.csv").flatMap(mapToDict)

# 将RDD所有的元素合并成一个列表
def combine_func(item, item1):
    if isinstance(item, list):
        item.append(item1)
        return item
    else:
        return [item, item1]

# 将列表中的字典输出到CSV文件
def write_to_csv(records):
    with open("./users2.csv", "w") as fp:
        csv_writer = csv.DictWriter(fp, fieldnames=("age", "name", "address"))
        csv_writer.writeheader()
        for x in records:
            csv_writer.writerow(x)


write_to_csv(csvRDD.reduce(f=combine_func))
