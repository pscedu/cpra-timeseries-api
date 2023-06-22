from cpra_timeseries_api_app.views.base import BaseTimeSeriesView


class EcoregionBaseTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['scenario', 'model_group_name', 'geography', 'time']
    param_to_field = {'scenario': 'Scenario', 'model_group_name': 'ModelGroup', 'geography': 'Ecoregion', 'time': 'Year_FWOA'}
    table = 'icm.mv_land_veg'
    select_clause = f'{table}."Year_FWOA" as time, {table}."ModelGroup" as model_group_name, {table}."Scenario" as scenario, {table}."Ecoregion" as geography, ' \
                    f'SUM({table}."Area_m2") as value'
    group_by_fields = ['ModelGroup', 'Scenario', 'Ecoregion', 'Year_FWOA']
    order_by_fields = ['Year_FWOA']


class EcoregionAnnualLandAreaTimeSeriesView(EcoregionBaseTimeSeriesView):
    table = EcoregionBaseTimeSeriesView.table
    where_clause = f'{table}."VegetationCode" IN (\'LND\', \'BRG\', \'FLT\')'


class EcoregionAnnualVegetationCoverageAreaTimeSeriesView(EcoregionBaseTimeSeriesView):
    table = EcoregionBaseTimeSeriesView.table
    where_clause = f'{table}."VegetationCode" IN (\'FRM\', \'INM\', \'BRM\', \'SAM\', \'FOR\')'


class EcoregionAnnualHabitatSuitabilityUnitTimeSeriesView(EcoregionBaseTimeSeriesView):
    table = 'icm.mv_hsi'
    select_clause = f'{table}."Year_FWOA" as time, {table}."ModelGroup" as model_group_name, {table}."Scenario" as scenario, {table}."Ecoregion" as geography, ' \
                    f'SUM({table}."HabitatSuitability") as value'
