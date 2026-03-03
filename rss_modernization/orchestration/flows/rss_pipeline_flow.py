import uuid
import datetime
from prefect import flow

from rss_modernization.orchestration.tasks.pipeline_tasks import (
    run_rss_ingestion,
    run_dbt_run,
    run_dbt_test
)

@flow(name="RSS Modern Data Pipeline")
def rss_pipeline():

    run_id = str(uuid.uuid4())
    pipeline_name = "rss_pipeline"

    start_time = datetime.datetime.now()

    try:
        run_rss_ingestion()
        run_dbt_run()
        run_dbt_test()

        print("Pipeline completed successfully!")

    except Exception as e:
        print(f"Pipeline failed: {str(e)}")
        raise e


if __name__ == "__main__":
    rss_pipeline()
