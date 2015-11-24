# Lesson 3: Your First Spark Application

> Throughout this lesson, you perform a case study based on data from DonorsChoose.org, a non-profit dedicated to supporting teachers in the classroom.

You focus on how to perform the tasks you might be familiar with from the standard data science process, but with data at scale this time.

We start with a formalization of the data science workflow and see where spark can help us build a machine learning pipeline.

From there, you use Spark and its higher level libraries to explore the DonorsChoose.org data sets and compute basic statistics to better understand the data.

Once you have done some basic exploratory analysis, you dive into a primer on natural language processing and see how to use text as an input to a model.

With properly vectorized data, you implement your own machine learning model with Spark to understand a little bit more about machine learning and see how you might build a complex algorithm with the framework.

## Objectives

* Understand how Spark can help with common tasks from the Data Science process
* Perform EDA on the DonorsChoose.org project data with Spark
* See how to perform basic data quality checks at scale with Spark
* Visualize the distribution of your data locally with pandas after aggregating and summarizing it with Spark.
* Understand the basics of tokenizing and vectorizing text
* See how to leverage NLP techniques (like tf-idf weighting) to make sense of text
* Understand the basics of the different types of machine learning
* Perform k-means clustering on DonorsChoose.org project essays
* Understand how to interpret the results of k-means, as well as the limitations of the algorithm

## Examples

* __3.3 - 3.5__: [donors_choose_eda.ipynb](../code/donors_choose_eda.ipynb)
* __3.6 - 3.8__: [natural_language_processing.ipynb](../code/natural_language_processing.ipynb)
* __3.10 - 3.12__: [kmeans.ipynb](../code/kmeans.ipynb)
* __Extra__: [nlp_ec2cluster.ipynb](../code/nlp_ec2cluster.ipynb)

## References

### 3.1: How Spark Fits into the Data Science Process

* [Quora: What is the work flow or process of a data scientist?][1]
* [Stitch Fix: Rapid Development & Performance in Spark For Data Scientists][1.1]

### 3.2: Introduction to Exploratory Data Analysis

* [Doing Data Science (Schutt and O'Neil)][2]
* [Exploratory Data Analysis (Tukey)][3]

### 3.3: Case Study: DonorsChoose.org

* [DonorsChoose.org][4]
* [DonorsChoose.org Open Data][5]
* [Writing and Using Custom Exceptions in Python][6]

### 3.4: Data Quality Checks with Accumulators

* [HyperLogLog in practice: algorithmic engineering of a state of the art cardinality estimation algorithm][7]
* [Sketch of the Day: HyperLogLog — Cornerstone of a Big Data Infrastructure][8]
* [Spark Docs (1.4.1): DataFrame NA Functions][9]
* [Spark Docs (1.4.1): Accumulators][10]

### 3.5: Making Sense of Data: Summary Statistics and Distributions

* [Statistical and Mathematical Functions with DataFrames in Spark][11]
* [A simple algorithm for finding frequent elements in streams and bags][12]
* [Wikipedia: Summary Statistics][13]
* [Wikipedia: Anscombe's quartet][14]
* [Pandas Plotting][15]
* [Plotting Spark DataFrames with Plotly][16]

### 3.6: Working with Text: Introduction to NLP

* [Dan Jurafsky & Chris Manning: Natural Language Processing][17]
* [Bag-of-Words Model][18]

### 3.7: Tokenization and Vectorization with Spark

* [Introduction to Information Retrival][19]
* [Wikipedia: Vector Space Model][20]

### 3.8: Summarization with tf-idf

* [Tf-idf: A Single-Page Tutorial][21]
* [Tutorial: Finding Important Words in Text Using TF-IDF][22]
* [Text Summarization: Generating Snippets][23]
* [Spark Docs (1.4.1): Feature Extraction and Transformation][24]

### 3.9: Introduction to Machine Learning

* [Wikipedia: Machine Learning][25]
* [A Visual Introduction to Machine Learning][26]
* [Stanford CS 229 Lecture Notes (Andrew Ng)][27]
* [IOM 530: Intro. to Statistical Learning][28]
* [Kaggle: Data Science Use Cases][29]
* [Visualizing k-means Clustering][30]
* [K-Medoids](http://www.stat.cmu.edu/~ryantibs/datamining/lectures/04-clus1-marked.pdf)

### 3.10: Unsupervised Learning with Spark: Implementing k-means

* [Stanford CS 221: k-means Algorithm][31]

### 3.11: Testing k-means with DonorsChoose.org Essays

* [k-means vs. k-medoids: Convergence][32]

### 3.12: Challenges of k-means: Latent Features, Interpretation, and Validation

* [Stack Exchange: Meaning of Latent Features?][33]
* [Finding the K in k-means Clustering][34]
* [Silhouettes: A graphical aid to the interpretation and validation of cluster analysis][35]
* [Scalable K-Means++](http://theory.stanford.edu/~sergei/papers/vldb12-kmpar.pdf)

[1]: https://www.quora.com/What-is-the-work-flow-or-process-of-a-data-scientist
[1.1]: http://multithreaded.stitchfix.com/blog/2015/10/06/spark-for-data-science/
[2]: http://columbiadatascience.com/doing-data-science/
[3]: http://www.amazon.com/Exploratory-Data-Analysis-John-Tukey/dp/0201076160
[4]: http://www.donorschoose.org/
[5]: http://data.donorschoose.org/open-data/overview/
[6]: https://www.codementor.io/python/tutorial/how-to-write-python-custom-exceptions
[7]: http://dl.acm.org/citation.cfm?doid=2452376.2452456
[8]: http://content.research.neustar.biz/blog/hll.html
[9]: https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrameNaFunctions
[10]: http://spark.apache.org/docs/1.4.1/programming-guide.html#accumulators-a-nameaccumlinka
[11]: https://databricks.com/blog/2015/06/02/statistical-and-mathematical-functions-with-dataframes-in-spark.html
[12]: http://dl.acm.org/citation.cfm?doid=762471.762473
[13]: https://en.wikipedia.org/wiki/Summary_statistics
[14]: https://en.wikipedia.org/wiki/Anscombe%27s_quartet
[15]: http://pandas.pydata.org/pandas-docs/stable/visualization.html
[16]: https://plot.ly/ipython-notebooks/apache-spark/
[17]: https://www.youtube.com/playlist?list=PL6397E4B26D00A269
[18]: https://en.wikipedia.org/wiki/Bag-of-words_model
[19]: http://nlp.stanford.edu/IR-book/
[20]: https://en.wikipedia.org/wiki/Vector_space_model
[21]: http://www.tfidf.com/
[22]: http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/
[23]: https://class.coursera.org/nlp/lecture/192
[24]: http://spark.apache.org/docs/1.4.1/mllib-feature-extraction.html
[25]: https://en.wikipedia.org/wiki/Machine_learning
[26]: http://www.r2d3.us/visual-intro-to-machine-learning-part-1/
[27]: http://cs229.stanford.edu/notes/cs229-notes1.pdf
[28]: http://media.wix.com/ugd/6d8e3a_6b3b349674524a09a2c1e9f407bf7043.pdf
[29]: https://www.kaggle.com/wiki/DataScienceUseCases
[30]: http://stanford.edu/class/ee103/visualizations/kmeans/kmeans.html
[31]: http://stanford.edu/~cpiech/cs221/handouts/kmeans.html
[32]: https://commons.wikimedia.org/wiki/File:K-means_versus_k-medoids.png
[33]: http://datascience.stackexchange.com/questions/749/meaning-of-latent-features
[34]: https://datasciencelab.wordpress.com/2013/12/27/finding-the-k-in-k-means-clustering/
[35]: http://www.sciencedirect.com/science/article/pii/0377042787901257