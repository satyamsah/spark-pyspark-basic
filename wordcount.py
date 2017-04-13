import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

  # tak two arguments, input and output
  if len(sys.argv) != 3:
    print("Usage: wordcount <input> <output>")
    exit(-1)

  # create Spark context with Spark configuration
  conf = SparkConf().setAppName("Spark Count")
  sc = SparkContext(conf=conf)

  # read in text file
  text_file = sc.textFile(sys.argv[1])

  # split each line into words
  # count the occurrence of each word
  # sort the output based on word
  counts = text_file.flatMap(lambda line: line.split(" ")) \
           .map(lambda word: (word, 1)) \
           .reduceByKey(lambda a, b: a + b) \
           .sortByKey()

  # save the result in the output text file
  counts.saveAsTextFile(sys.argv[2])
