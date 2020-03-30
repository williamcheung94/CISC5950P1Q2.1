#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1.1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1.1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /project1.1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/pvqr-7yc4.csv /project1.1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../mapreduce-test-python/project1.1/mapper.py -mapper ../../mapreduce-test-python/project1.1/mapper.py \
-file ../../mapreduce-test-python/project1.1/reducer.py -reducer ../../mapreduce-test-python/project1.1/reducer.py \
-input /project1.1/input/* -output /project1.1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /project1.1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1.1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1.1/output/
../../stop.sh
