from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id = "dags_bash_with_template",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    # 누락된 구간을 돌리지 않음
    catchup=False
) as dag:
    # task 객체명 : bash_t1 # 객체명과 task_id는 동일하게
    basg_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo data_interval_end : {{ date_interval_end }}",
    )
    
    basg_t2 = BashOperator(
        task_id="bash_t2",
        env = {
            # date_interval_start : 타임스탬프 +> | ds : 날짜 형식으로 변환
            "START_DATE" : "{{date_interval_start | ds }}",
            "END_DATE" : "{{date_interval_end | ds }}"
        },
        # && : 앞의 명령어가 성공했을 때 뒤의 명령어 실행
        bash_command="echo $START_DATE && echo $END_DATE",
    )
    
    basg_t1 >> basg_t2