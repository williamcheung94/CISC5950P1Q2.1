#!/bin/sh
./start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /CISC5950P1Q2.1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /CISC5950P1Q2.1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /CISC5950P1Q2.1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /CISC5950P1Q2.1/shot_logs.csv /CISC5950P1Q2.1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file /CISC5950P1Q2.1/mapper.py -mapper /CISC5950P1Q2.1/mapper.py \
-file /CISC5950P1Q2.1/reducer.py -reducer /CISC5950P1Q2.1/reducer.py \
-input /project1.1/input/* -output /CISC5950P1Q2.1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /CISC5950P1Q2.1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /CISC5950P1Q2.1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /CISC5950P1Q2.1/output/
./stop.sh
