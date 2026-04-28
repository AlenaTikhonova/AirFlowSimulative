with DAG(
    dag_id="first_dag",
    schedule="@daily",
    start_date=datetime(year=2024, month=8, day=1),
) as dag:

    start_dag = EmptyOperator(
        task_id="start_dag",
    )

    end_dag = EmptyOperator(
        task_id="end_dag",
    )

    test = PythonOperator(
        task_id="test",
        python_callable=test_func,
        op_kwargs={
            "ds": "{{ ds }}"
        },
    )

    start_dag >> test >> end_dag