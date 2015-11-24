# Lesson 2: Spark Programming APIs

> In this lesson, you see how Spark makes large scale data analysis much more accessible by providing application programming interfaces in languages familiar to data scientists.

We start by using Python and the PySpark interface to perform basic data analysis on a large dataset.

Throughout the lesson you learn how PySpark and SparkR interface with a Spark cluster and the Spark core framework, which is written in Scala.

With the SparkR API, you see how to reason about your data from a higher level using the DataFrame abstraction.

And finally, you see how by adding structure to your data with Spark SQL, you can construct complex queries to efficiently analyze your data.

## Objectives

* Understand how the extensibility the core Spark framework enables programming APIs to be developed in other languages
* Work with the PySpark API to perform an end-to-end analysis of flight delay data
* See how the DataFrame API in Spark allows for efficient analyses, both in terms of developer productivity and execution performance
* Aggregate and filter a large dataset with Spark to visualize locally with ggplot2
* Understand how to integrate existing SQL workflows with Spark

## References

### 2.1: Introduction to the Spark Programming APIs

* [PySpark Internals][1]
* [A deeper understanding of Spark's internals](https://spark-summit.org/2014/wp-content/uploads/2014/07/A-Deeper-Understanding-of-Spark-Internals-Aaron-Davidson.pdf)

### 2.2: PySpark: Loading and Importing Data

* [Amazon Web Service Account][4]
* [Mortar Data Github examples][2]
* [Bureau of Transportation Statistics: Airline Data][3]
* [IPython/Jupyter magic functions][5]

### 2.3: PySpark: Parsing and Transforming Data

* [Spark Docs (1.4.1): PySpark API][6]

### 2.4: PySpark: Analyzing Flight Delays

* [Plotting Spark DataFrames with Plotly](https://plot.ly/ipython-notebooks/apache-spark/)
* [Which Flight Will Get You There Fastest (FiveThirtyEight)][7]

### 2.5: SparkR: Introduction to DataFrames

* [SparkR: The Past, the Present and the Future][8]

### 2.6: SparkR: Aggregations and Analysis

* [Spark Docs (1.4.1): SparkR API][9]

### 2.7: SparkR: Visualizing Data with ggplot2

* [ggplot2 Homepage][10]
* [ggplot2: An Implementation of the Grammar of Graphics][11]

### 2.8: Why (Spark) SQL?

* [Spark Docs (1.4.1): Spark SQL API][12]

### 2.9: Spark SQL: Adding Structure to Your Data

* [SQL Zoo (interactive SQL tutorial)][13]

### 2.10: Spark SQL: Integration into Existing Workflows

* [Spark SQL: Data Sources][14]
* [Spark SQL: JDBC to Other Databases][15]
* [Spark SQL: Distributed SQL Engine][16]

[1]: https://cwiki.apache.org/confluence/display/SPARK/PySpark+Internals
[2]: https://github.com/mortardata/mortar-examples
[3]: http://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236
[4]: https://aws.amazon.com/account/
[5]: https://ipython.org/ipython-doc/3/interactive/magics.html
[6]: http://spark.apache.org/docs/1.4.1/api/python/
[7]: http://projects.fivethirtyeight.com/flights/
[8]: https://spark-summit.org/2015/events/sparkr-the-past-the-present-and-the-future/
[9]: http://spark.apache.org/docs/1.4.1/api/R/
[10]: http://ggplot2.org/
[11]: http://ggplot2.org/resources/2007-vanderbilt.pdf
[12]: http://spark.apache.org/docs/1.4.1/sql-programming-guide.html
[13]: http://sqlzoo.net/
[14]: http://spark.apache.org/docs/latest/sql-programming-guide.html#data-sources
[15]: http://spark.apache.org/docs/latest/sql-programming-guide.html#jdbc-to-other-databases
[16]: http://spark.apache.org/docs/latest/sql-programming-guide.html#distributed-sql-engine