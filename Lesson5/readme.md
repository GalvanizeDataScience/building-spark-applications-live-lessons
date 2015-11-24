# Lesson 4

> In this lesson, you learn how to leverage Spark's machine learning libraries to build a powerful model to predict customer propensity to buy.

We start by using Spark to prepare our data for input into a model.From there, you build a complex model for classification using MLlib and spark.ml.

But building a model isn't the whole story when it comes to machine learning. Often the most important step of a machine learning pipeline is the evaluation step.

Once you build a model, you then will evaluate and tune its performance. And finally you finish by seeing how to serialize your model to deploy it to make predictions.

## Objectives

* Understand the differences between Spark's two machine learning libraries: MLlib and spark.ml
* Learn how to effective process your data for input into Spark's machine learning libraries
* Use MLlib to perform supervised learning on large datasets
* Understand the basics of how to evaluate machine learning models with cross validation
* Evaluate machine learning models trained with Spark locally using scikit-learn
* Build an end-to-end machine learning pipeline with spark.ml and perform model selection and hyperparameter optimization with grid search.
* See how to properly serialize and deploy a machine learning model trained with Spark

## Examples

* __5.4 - 5.9__: [machine-learning.ipynb](../code/machine-learning.ipynb)

## References

### 5.1: Machine Learning on Spark: MLlib and spark.ml

* [KDD Cup 2009: Customer Relationship Prediction][1]

### 5.2: The KDD Cup Competition: Preparing Data and Imputing Values

* None

### 5.3: Introduction to Supervised Learning: Logistic Regression

* [Iris flower Data set][2]
* [Stanford CS 229 (Ng): Supervised Learning][3]
* [mathematical monk (video): Logistic Regression][4]
* [An Introduction to Statistical Learning][5]
    * Logistic Regression: Chapter 4 (pp. 127-137)
    * Tree Based Methods: Chapter 8 (pp. 303-332)

### 5.4: Building a Model with MLlib

* [Spark Docs (1.4.1): Machine Learning Library (MLlib) Guide][6]
* [Multinomial Logistic Regression with Apache Spark][7]

### 5.5: Model Evaluation and Metrics

* [Cross Validation: the Right and Wrong Way][8]
* [An Introduction to ROC Analysis][9]

### 5.6: Leveraging scikit-learn to Evaluate MLlib Models

* [scikit-learn: Model evaluation, quantifying the quality of predictions][10]
* [Wikipedia: Precision and Recall][11]

### 5.7: Training Models with spark.ml

* [Spark Docs (1.4.1): Spark ML Programming Guide][12]

### 5.8: Machine Learning Pipelines with spark.ml

* None

### 5.9: Tuning Models: Features, Cross Validation, and Grid Search

* [Spark Docs (1.4.1): Feature Transformers][13]
* [mathematical monk (video): k-fold Cross Validation][14]
* [Hyperparameter Tuning][15]

### 5.10: Serializing and Deploying Models

* [Spark Docs (1.4.1): PMML Model Export][16]
* [Spark Docs (1.4.1): Spark Streaming MLlib Operations][17]

[1]: http://kdd.org/kdd-cup/view/kdd-cup-2009
[2]: https://en.wikipedia.org/wiki/Iris_flower_data_set
[3]: http://cs229.stanford.edu/notes/cs229-notes1.pdf
[4]: https://www.youtube.com/watch?v=-Z2a_mzl9LM
[5]: http://www-bcf.usc.edu/~gareth/ISL/ISLR%20First%20Printing.pdf
[6]: http://spark.apache.org/docs/1.4.1/mllib-guide.html
[7]: http://www.slideshare.net/dbtsai/2014-0501-mlor
[8]: https://www.kaggle.com/c/the-analytics-edge-mit-15-071x/forums/t/7837/cross-validation-the-right-and-the-wrong-way
[9]: https://ccrma.stanford.edu/workshops/mir2009/references/ROCintro.pdf
[10]: http://scikit-learn.org/stable/modules/model_evaluation.html
[11]: https://en.wikipedia.org/wiki/Precision_and_recall
[12]: http://spark.apache.org/docs/1.4.1/ml-guide.html
[13]: http://spark.apache.org/docs/1.4.1/ml-features.html#feature-transformers
[14]: https://www.youtube.com/watch?v=m5StqDv-YlM
[15]: http://blog.dato.com/how-to-evaluate-machine-learning-models-part-4-hyperparameter-tuning
[16]: http://spark.apache.org/docs/1.4.1/mllib-pmml-model-export.html
[17]: http://spark.apache.org/docs/1.4.1/streaming-programming-guide.html#mllib-operations