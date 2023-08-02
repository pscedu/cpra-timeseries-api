from cpra_timeseries_api_app.views.base import BaseTimeSeriesView


class EcoregionBaseTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['scenario_name', 'model_group_name', 'geography', 'elapsed_year']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name', 'geography': 'geography', 'elapsed_year': 'elapsed_year'}
    group_by_fields = ['model_group_name', 'scenario_name', 'geography', 'elapsed_year']
    order_by_fields = ['elapsed_year']


class EcoregionAnnualLandAreaTimeSeriesView(EcoregionBaseTimeSeriesView):
    table = 'dap.vw_icm_ecor_annual_lnd'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'


class EcoregionAnnualVegetationCoverageAreaTimeSeriesView(EcoregionBaseTimeSeriesView):
    table = 'dap.vw_icm_ecor_annual_veg'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'


class EcoregionAnnualHabitatSuitabilityUnitTimeSeriesView(EcoregionBaseTimeSeriesView):
    table = 'dap.vw_icm_ecor_annual_hsi'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'
