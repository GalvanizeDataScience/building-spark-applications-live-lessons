# Lesson 4

> In this lesson, I peel back the layers on Spark and show you some of its internals.

We start with primer on distributed systems and the theory that underlays them.

From there, I walk through Spark's execution context and how Spark actually executes your code in a distributed fashion on a cluster.

By understanding some of the intricacies of how Spark coordinates program execution, you learn how to improve Spark performance for your applications.

And finally we finish by setting up our own cluster on Amazon Web Services enabling us to really leverage all of the performance gains of a distributed system.

## Objectives

* Understand the basics of distributed systems and how they help us scale data storage as well as computation
* See how Spark and its execution context efficient runs code in a distributed manner
* Understand the RDD abstraction and the interface it gives us to manipulate distributed datasets
* Deploy your own Spark cluster on Amazon Web Services
* Monitor your Spark jobs to tune them and optimize their execution
* See how Spark can leverage the memory of a cluster to cache data that is used repeated

## References

### 4.1: Introduction to Distributed Systems

* [Distributed Systems: for fun and profit][1]
* [Resilience Engineering: Learning to Embrace Failure][2]

### 4.2: Building Systems that Scale

* [CAP Theorem: Revisited][3]
* [Brewer’s Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services (original paper)][4]
* [CAP Twelve Years Later: How the "Rules" Have Changed][5]
* [You Can't Sacrifice Partition Tolerance][6]
* [How to Beat the CAP Theorem][7]
* [Questioning the Lambda Architecture][8]

### 4.3: The Spark Execution Context

* [MapReduce and Spark][9]
* [Introduction to Hadoop][10]

### 4.4: RDD Deep Dive: Dependencies and Lineage

* [Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing (original paper)][11]

### 4.5: A Day in the Life of a Spark Application

* None

### 4.6: How Code Runs: Stages, Tasks, and the Shuffle

* None

### 4.7: Spark Deployment: Local and Cluster Modes

* [Spark High Availability][12]
* [A tale of two clusters: Mesos and YARN][13]

### 4.8: Setting Up Your Own Cluster

* [Amazon Web Services (AWS)][14]
* [Master Node Setup Script][15]
* [Worker Node Setup Script][16]
* [IPython Startup Script][17]

### 4.9: Spark Performance: Monitoring and Optimization

* [Metrics, Metrics Everywhere][18]
* [Spark Docs (1.4.1): Monitoring and Instrumentation][19]

### 4.10: Tuning Your Spark Application

* [Spark Docs (1.4.1): Tuning Spark][20]

### 4.11: Making Spark Fly: Parallelism

* [Amdahl's Law][21]

### 4.12: Making Spark Fly: Caching

* [Spark Docs (1.4.1): RDD Persistence][22]

[1]: http://book.mixu.net/distsys/
[2]: queue.acm.org/detail.cfm?id=2371297
[3]: http://robertgreiner.com/2014/08/cap-theorem-revisited/
[4]: https://www.comp.nus.edu.sg/~gilbert/pubs/BrewersConjecture-SigAct.pdf
[5]: http://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed
[6]: http://codahale.com/you-cant-sacrifice-partition-tolerance/
[7]: http://nathanmarz.com/blog/how-to-beat-the-cap-theorem.html
[8]: http://radar.oreilly.com/2014/07/questioning-the-lambda-architecture.html
[9]: http://vision.cloudera.com/mapreduce-spark/
[10]: http://www.jamesserra.com/archive/2014/02/introduction-to-hadoop/
[11]: https://www.cs.berkeley.edu/~matei/papers/2012/nsdi_spark.pdf
[12]: http://spark.apache.org/docs/latest/spark-standalone.html#high-availability
[13]: http://radar.oreilly.com/2015/02/a-tale-of-two-clusters-mesos-and-yarn.html
[14]: https://aws.amazon.com/
[15]: deploy/master.sh
[16]: deploy/worker.sh
[17]: deploy/pyspark.py
[18]: http://codahale.com/codeconf-2011-04-09-metrics-metrics-everywhere.pdf
[19]: http://spark.apache.org/docs/1.4.1/monitoring.html
[20]: http://spark.apache.org/docs/1.4.1/tuning.html
[21]: https://en.wikipedia.org/wiki/Amdahl's_law
[22]: http://spark.apache.org/docs/1.4.1/programming-guide.html#rdd-persistence