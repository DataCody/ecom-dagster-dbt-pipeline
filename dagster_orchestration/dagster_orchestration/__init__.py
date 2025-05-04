from dagster import Definitions
from dagster_orchestration.assets import dbt_assets, resources

defs = Definitions(
    assets=dbt_assets,
    resources=resources
)