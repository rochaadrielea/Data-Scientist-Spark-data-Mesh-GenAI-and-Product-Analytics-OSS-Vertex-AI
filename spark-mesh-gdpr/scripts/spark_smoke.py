import os
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("smoke-eventlog")
    .config("spark.eventLog.enabled", "true")
    .config("spark.eventLog.dir", "s3a://spark-events/")
    .config("spark.hadoop.fs.s3a.endpoint", "http://localhost:9000")
    .config("spark.hadoop.fs.s3a.path.style.access", "true")
    .config("spark.hadoop.fs.s3a.access.key", "minioadmin")
    .config("spark.hadoop.fs.s3a.secret.key", "minioadmin")
    .getOrCreate()
)

df = spark.range(0, 5_000_000).repartition(8)
df.groupByExpr("id % 10 as g").count().collect()

spark.stop()
