hadoop-etl-example
==================

A hadoop based ETL example project. 

Prerequisite
------------

- `HDP 2.4 on Hortonworks Sandbox <http://hortonworks.com/downloads/#sandbox>`_
- `Apache Airflow <https://github.com/apache/incubator-airflow>`_

Hadoop Sandbox Setup
^^^^^^^^^^^^^^^^^^^^

.. code:: bash

  # After startup the sandbox on virtualbox
  # Add host settings
  echo 127.0.0.1 sandbox.hortonworks.com >> /etc/hosts

  cat <<EOF >> ~/.ssh/config
  Host sbx.hdp
    HostName sandbox.hortonworks.com
    User root
    Port 2222
  EOF

  # copy hive and hadoop executable and expand them
  scp sbx.hdp:/usr/hdp/current/hive-client/hive.tar.gz ./
  tar xvzf hive.tar.gz
  scp sbx.hdp:/usr/hdp/current/hadoop-client/mapreduce.tar.gz ./
  tar xvzf mapreduce.tar.gz

  # set hadoop environment variables
  export PROJECT_HOME=$(pwd)
  export HADOOP_HOME=${PROJECT_HOME}/hadoop
  export HIVE_HOME=${PROJECT_HOME}/hive
  export PATH="$HADOOP_HOME/bin:$HIVE_HOME/bin:$PATH"
  
  # open sandbox home page and Ambari
  open http://sandbox.hortonworks.com:8888
  open http://sandbox.hortonworks.com:8080

  # connect hive and issue a query 
  beeline -u jdbc:hive2://sandbox.hortonworks.com:10000 -n guest -p guest-password
  show tables;
  select * from sample_07 limit 10;


Airflow Setup
^^^^^^^^^^^^^

.. code:: bash

   # set airflow environment variables
   export AIRFLOW_HOME=${PROJECT_HOME}/airflow

   cd airflow 

   # enable python 3.4 and install dependencies 
   pyenv activate py34
   pip install -r requirements.txt
   
   # initialize sqlite db
   airflow initdb
   sqlite3 db.sqlite3 < ./setup/init-data.sqlite3.sql

   # list and run 'select' task of hive dag
   airflow list_tasks hive
   airflow run hive select 2016-01-01

   # start web UI
   airflow webserver -p 1111
   open http://localhost:1111

