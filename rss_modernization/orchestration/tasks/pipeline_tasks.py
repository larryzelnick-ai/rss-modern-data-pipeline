import subprocess
import os
import sys
from prefect import task
from pathlib import Path

@task(retries=3, retry_delay_seconds=10)
def run_rss_ingestion():

    root_path = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(__file__)
            )
        )
    )

    script_path = os.path.join(
        root_path,
        "python_scripts",
        "ingest_rss.py"
    )

    subprocess.run(
        [sys.executable, script_path],
        check=True
    )

@task(retries=2, retry_delay_seconds=5)
def run_dbt_run():

    project_path = Path(__file__).resolve().parents[2]

    subprocess.run(
        ["dbt", "run"],
        cwd=project_path,
        check=True
    )


@task(retries=2, retry_delay_seconds=5)
def run_dbt_test():

    project_path = Path(__file__).resolve().parents[2]

    subprocess.run(
        ["dbt", "test"],
        cwd=project_path,
        check=True
    )
