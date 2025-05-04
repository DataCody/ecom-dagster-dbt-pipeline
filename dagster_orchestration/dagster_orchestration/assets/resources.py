import os
from dagster_dbt import DbtCliClientResource

resources = {
    "dbt": DbtCliClientResource(
        project_dir=os.getenv("DBT_PROJECT_DIR"),
        profiles_dir=os.getenv("DBT_PROFILES_DIR")
    ),
    "airbyte_instance": AirbyteResource(
        host="localhost",
        port=8000,
        username="airbyte",
        password=os.getenv("AIRBYTE_PASSWORD")
    )
}