'''
1.10: MapReduce with Spark: Programming with Key-Value Pairs

Finding users who bought more than 5 items

    Run with: python big_spenders.py

'''
import os, json
import pyspark as ps

# need to get local path since we are reading local files
filepath = os.path.abspath(__file__)
data = os.path.join(filepath, '../data/toy_data.txt')

# initialize SparkContext
sc = ps.SparkContext()

# Turn off debug logging to console
logger = sc._jvm.org.apache.log4j
logger.LogManager.getLogger("org"). setLevel( logger.Level.ERROR )
logger.LogManager.getLogger("akka").setLevel( logger.Level.ERROR )

###################################

# read in toy_data into an RDD
file_rdd = sc.textFile('file://' + data)

# convert strings of JSON into Python dictionaries
json_rdd = file_rdd.map(lambda x: json.loads(x))

# convert RDD of dictionaries into key-value pairs
big_spenders = json_rdd.map(lambda x: tuple((x.keys()[0], int(x.values()[0]))))

# calculate "big spenders"
print big_spenders.reduceByKey(lambda a, b: a + b) \
                  .filter(lambda x: x[1] > 5).collect()

# shutdown SparkContext
sc.stop()