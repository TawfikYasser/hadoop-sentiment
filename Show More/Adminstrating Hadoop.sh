cd /usr/local/hadoop/sbin
./start-dfs.sh
./start-yarn.sh
jps
http://tawfik-virtualbox:8088/cluster
http://localhost:9870/explorer.html#/
su - hudser
sudo mkdir Hadoop_Sentiment
sudo wget https://raw.githubusercontent.com/TawfikYasser/hadoop-sentiment/main/Show%20More/bucket_hs.txt
hdfs dfs -ls /
hdfs dfs -mkdir /Hadoop_Sentiment
hdfs dfs -copyFromLocal /usr/Hadoop_Sentiment/bucket_hs.txt /Hadoop_Sentiment

Next: Hive, IntelliJ



-----
Main Hadoop Congf.

Group: hadoopenv => sudo addgroup hadoopenv
User: hduser => sudo adduser --ingroup hadoopenv hduser
Password: 9520hadoop

sudo visudo - add the user - CTRL X - Y - ENTER
su - hduser => to use the new user


to check dfs namenode: http://10.0.2.15:9870/
to check yarn: http://10.0.2.15:8042
to check dfs datanodes: http://10.0.2.15:9864/
