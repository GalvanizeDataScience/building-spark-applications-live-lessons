'''
1.9: Introduction to RDDs: Functions, Transformations, and Actions

Counting coin flips example with SparkContext

    Run with: python coin.py

'''

import pyspark as ps
import random

# initialize SparkContext
sc = ps.SparkContext()

# Turn off debug logging to console
logger = sc._jvm.org.apache.log4j
logger.LogManager.getLogger("org"). setLevel( logger.Level.ERROR )
logger.LogManager.getLogger("akka").setLevel( logger.Level.ERROR )

###################################

flips = 1000000

# lazy eval
coins = xrange(flips)

# lazy eval, nothing executed
heads = sc.parallelize(coins) \
          .map(lambda i: random.random()) \
          .filter(lambda r: r < 0.51) \
          .count()

print "{0} heads flipped!".format(heads)

# shutdown SparkContext
sc.stop()