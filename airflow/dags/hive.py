#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simpel Hive dag with template
"""
from airflow import DAG
from airflow.operators.hive_operator import HiveOperator
from datetime import datetime, timedelta

tpl_params = {'table':'sample_07'}

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('hive', 
    default_args=default_args,
    template_searchpath='j2_templates',
    user_defined_macros=tpl_params
)

t1 = HiveOperator(
        task_id='select',
        hql='select.hql',
        hive_cli_conn_id='beeline_sbx',
        dag=dag) 
