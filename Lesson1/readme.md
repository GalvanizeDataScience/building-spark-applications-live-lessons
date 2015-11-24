# Lesson 1: Introduction to the Spark Environment

> In this lesson, you learn how to get setup with Spark and see the basics of how to program with Spark.

I start with a little bit of history of the project and provide motivation for the framework: why Spark, why now?

From there, I walk through the process of getting Spark setup locally on your laptop so you can start developing your our Spark applications!

And all along the way you learn the common paradigms and abstractions Spark leverages, mainly functional programming and resilient distributed datasets.

## Objectives

* Understand the history and motivation behind Spark
* Setup a local Spark environment
* Program your first Spark job with the PySpark shell
* Understand the common paradigms for programming with Spark: RDDs and functional programming
* Work with key-value pairs to perform MapReduce operations

## Examples

* 1.9: [coin.py](../code/coin.py)
* 1.10: [big_spenders.py](../code/big_spenders.py)

## References

### 1.1: Getting the Materials

* [Galvanize Spark Resources][1]
* [Lesson Forum][2]
* [DonorsChoose.org Data][3]
* [KDD Cup 2009][4]

### 1.2: A Brief Historical Diversion

* [Moore's Law][5]
* [At the limit of Moore's law: scientists develop molecule-sized transistors][6]
* [Quora: Why haven't CPU clock speeds increased in the last 5 years?][7]
* [Why CPUs aren't getting any faster][7.1]

### 1.3: Origins of the Framework

* [An Architecture for Fast and General Data Processing on Large Clusters (Matei's Dissertation)][8]
* [The Google File System (original paper)][9]
* [Nutch, and Search Engine History][10]
* [MapReduce: Simplified Data Processing on Large Clusters (original paper)][11]
* [Doug Cutting: The History of Hadoop][12]
* [Hadoop: A brief History](research.yahoo.com/files/cutting.pdf)
* [Spark: Cluster Computing with Working Sets (original paper)][13]
* [About Databricks][14]
* [The Apache Software Foundation Announces Apache™ Spark™ as a Top-Level Project][15]
* [The State of Spark: And where we are going next](https://spark-summit.org/2013/wp-content/uploads/2013/10/Zaharia-spark-summit-2013-matei.pdf)

### 1.4: Why Spark?

* [Apache Spark Homepage][16]

### 1.5: Getting Set Up: Spark and Java

* [Spark Downloads][17]
* [Java JDK Downloads][18]
* [Spark on Windows 7](http://nishutayaltech.blogspot.in/2015/04/how-to-run-apache-spark-on-windows7-in.html)

### 1.6: Getting Set Up: Scientific Python

* [Continuum Analytics: Anaconda Downloads][19]
* [Project Jupyter (formerly IPython) Homepage][20]
* [Py4J Homepage][21]

### 1.7: Getting Set Up: R Kernel for Jupyter

* [Installing R][22]
* [IRKernel Homepage][23]
* [SparkR Setup][24]
* [Jupyter/IPython tutorial][25]
* [Cloudera QuickStart VM][26]
* [Hortonworks Sandbox VM][27]

### 1.8: Your First PySpark Job

* [Getting Started with Spark (in Python)](https://districtdatalabs.silvrback.com/getting-started-with-spark-in-python)
* [Stack Overflow: How to use custom classes with Apache Spark (pyspark)][28]

### 1.9: Introduction to RDDs: Functions, Transformations, and Actions

* [Python Closures][29]
* [Spark Programming Guide][30]

### 1.10: MapReduce with Spark: Programming with Key-Value Pairs

* [A Practical Introduction to Functional Programming][31]
* [Stack Overflow: How to turn off INFO logging in PySpark?][32]

[1]: http://galvanize.com/resources/spark
[2]: https://gitter.im/zipfian/building-spark-applications-live-lessons
[3]: http://data.donorschoose.org/open-data/overview/
[4]: http://kdd.org/kdd-cup/view/kdd-cup-2009/Data
[5]: https://en.wikipedia.org/wiki/Moore's_law
[6]: http://www.theguardian.com/technology/2015/jul/21/limit-law-scientists-molecule-sized-transistors-atoms-chips
[7]: https://www.quora.com/Why-havent-CPU-clock-speeds-increased-in-the-last-5-years
[7.1]: http://www.technologyreview.com/view/421186/why-cpus-arent-getting-any-faster/
[8]: www.eecs.berkeley.edu/Pubs/TechRpts/2014/EECS-2014-12.pdf
[9]: http://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf
[10]: https://courses.cs.washington.edu/courses/cse490h/08au/lectures/490h_nutch.pdf
[11]: http://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf
[12]: https://www.udacity.com/course/viewer#!/c-ud617/l-306818608/m-312934728
[13]: http://www.cs.berkeley.edu/~matei/papers/2010/hotcloud_spark.pdf
[14]: https://databricks.com/company/about-us
[15]: https://blogs.apache.org/foundation/entry/the_apache_software_foundation_announces50
[16]: http://spark.apache.org/
[17]: http://spark.apache.org/downloads.html
[18]: http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
[19]: https://www.continuum.io/downloads
[20]: http://jupyter.org/
[21]: https://www.py4j.org/
[22]: https://cran.r-project.org/bin/
[23]: https://github.com/IRkernel/IRkernel
[24]: https://github.com/apache/spark/tree/master/R
[25]: http://jupyter-notebook-beginner-guide.readthedocs.org/en/latest/
[26]: http://www.cloudera.com/content/cloudera/en/downloads/quickstart_vms/cdh-5-4-x.html
[27]: http://hortonworks.com/products/hortonworks-sandbox/#install
[28]: http://stackoverflow.com/questions/31093179/how-to-use-custom-classes-with-apache-spark-pyspark
[29]: https://newcircle.com/bookshelf/python_fundamentals_tutorial/functional_programming
[30]: http://spark.apache.org/docs/1.4.1/programming-guide.html
[31]: http://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming
[32]: http://stackoverflow.com/questions/25193488/how-to-turn-off-info-logging-in-pyspark/32208445#32208445