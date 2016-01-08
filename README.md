# Building Spark Applications Live Lessons

[![Join the chat at https://gitter.im/zipfian/building-spark-applications-live-lessons](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/zipfian/building-spark-applications-live-lessons?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/zipfian/building-spark-applications-live-lessons)

This repository contains the exercises and data for the [Building Spark Applications Live Lessons video series][0]. It provides data scientists and developers with a practical introduction to the Apache Spark framework using Python, R, and SQL.  Additionally, it covers best practices for developing scalable Spark applications for predictive analytics in the context of a data scientist's standard workflow.

## Materials

The corresponding videos can be found on the following sites for purchase:

* [InformIT (individual purchase)][0]
* [Safari Books Online (subscription)][0.1]

In addition to the videos there are many other resources to provide you support in learning this new technology:

* [Galvanize Spark Resources][1]
* [Forum][2]

And/or please do not hesitate to reach out to me directly via email at jondinu@gmail.com or over twitter @clearspandex

> If you find any errors in the code or materials, please open a Github [issue](https://github.com/zipfian/building-spark-applications-live-lessons/issues) in this repository

## Skill Level

Beginning/Intermediate

## What You Will Learn

* How to install and set up a Spark environment locally and on a cluster
* The differences between and the strengths of the Python, R, and SQL programming interfaces
* How to build a machine learning model for text
* Common data science use cases that Spark is especially well-suited to solve
* How to tune a Spark application for performance
* The internals of the Spark framework and its execution model
* How to use Spark in a data science application workflow
* The basics of the larger Spark ecosystem

## Who Should Take This Course

* Practicing Data scientists who already use Python or R and want to learn how to scale up their analyses with Spark.
* Data Engineers who already use Java/Scala for Spark but want to learn about the Python, R, and SQL APIs and understand how Spark can be used to solve Data Science problems.

## Prerequisites

* Basic understanding of programming (Python a plus).
* Familiarity with the data science process and machine learning are a plus.

### Setup

* [Local Installation](http://galvanize-wp.s3.amazonaws.com/wp-content/uploads/2015/11/24162356/spark_local_setup.pdf)
* [Cluster Deployment](http://galvanize-wp.s3.amazonaws.com/wp-content/uploads/2015/11/24162623/spark_cluster_setup.pdf)

#### SparkR with a Notebook

1. Install [IRKernel](https://github.com/IRkernel/IRkernel)
  
```r
install.packages(c('rzmq','repr','IRkernel','IRdisplay'), repos = c('http://irkernel.github.io/', getOption('repos')))

IRkernel::installspec()
```

2. Set [environment variables](https://github.com/apache/spark/tree/master/R#using-sparkr-from-rstudio):

```
# Example: Set this to where Spark is installed
Sys.setenv(SPARK_HOME="/Users/[username]/spark")

# This line loads SparkR from the installed directory
.libPaths(c(file.path(Sys.getenv("SPARK_HOME"), "R", "lib"), .libPaths()))

# if these two lines work, you are all set
library(SparkR)
sc <- sparkR.init(master="local")
```

## Data

* [DonorsChoose.org Data][3]
* [KDD Cup 2009][4]
* [Bulk Data Download][5]

## IPython Console Help

Q: How can I find out all the methods that are available on DataFrame?

- In the IPython console type `sales.[TAB]`

- Autocomplete will show you all the methods that are available.

- To find more information about a specific method, say `.cov` type `help(sales.cov)`

- This will display the API documentation for that method.

## Spark Documentation

Q: How can I find out more about Spark's Python API, MLlib, GraphX,
Spark Streaming, deploying Spark to EC2?

- Go to <https://spark.apache.org/docs/latest>

- Navigate using tabs to the following areas in particular.

- Programming Guide > Quick Start, Spark Programming Guide,
  Spark Streaming, DataFrames and SQL, MLlib, GraphX, SparkR.

- Deploying > Overview, Submitting Applications, Spark Standalone,
  YARN, Amazon EC2.

- More > Configuration, Monitoring, Tuning Guide.

## Books

* [Learning Spark: Lightning-Fast Big Data Analytics (O'Reilly)](http://shop.oreilly.com/product/0636920028512.do)
* [Advanced Analytics with Spark (O'Reilly)](http://shop.oreilly.com/product/0636920035091.do)
* [Spark Knowledge Base](http://databricks.gitbooks.io/databricks-spark-knowledge-base)
* [Spark Reference Applications](http://databricks.gitbooks.io/databricks-spark-reference-applications)
* [Mastering Apache Spark](https://jaceklaskowski.gitbooks.io/mastering-apache-spark/)

## Staying Involved

* [Spark Community](https://spark.apache.org/community.html)
* [Meetups](http://spark.meetup.com/)
* [Mailing Lists](https://spark.apache.org/community.html)
* [Spark Summit](https://spark-summit.org/)

[0]: http://bit.ly/spark-ds-videos
[0.1]: https://www.safaribooksonline.com/library/view/building-spark-applications/9780134393490/
[1]: https://galvanize.com/resources/spark
[2]: https://gitter.im/zipfian/building-spark-applications-live-lessons
[3]: http://data.donorschoose.org/
[4]: http://kdd.org/kdd-cup/view/kdd-cup-2009/Data
[5]: https://s3.amazonaws.com/galvanize-example-data/spark-live-lessons-data.zip

