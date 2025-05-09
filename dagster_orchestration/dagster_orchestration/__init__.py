from dagster import Definitions, load_assets_from_modules
from .assets import resources
from dagster import AssetSelection, ScheduleDefinition, define_asset_job

big_star_job = define_asset_job("big_star_job", selection=AssetSelection.all())

big_star_schedule = ScheduleDefinition(
    job=big_star_job,
    cron_schedule="0 * * * *" # every hour
)

defs = Definitions(
    assets=load_assets_from_modules([assets]),
    resources=resources,
    jobs=[big_star_job],
    schedules=[big_star_schedule]
)