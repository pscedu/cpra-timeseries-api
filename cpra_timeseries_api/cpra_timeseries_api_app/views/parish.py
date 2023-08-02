from cpra_timeseries_api_app.views.base import BaseTimeSeriesView


class ParishBaseTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['scenario_name', 'model_group_name', 'geography', 'elapsed_year']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name',
                      'geography': 'geography', 'elapsed_year': 'elapsed_year'}
    group_by_fields = ['model_group_name', 'scenario_name', 'geography', 'ssp', 'migration', 'elapsed_year']
    order_by_fields = ['elapsed_year']


class ParishDecadalPopulationTimeSeriesView(BaseTimeSeriesView):
    table = 'dap.vw_clara_parish_decadal_population'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.ssp, {table}.migration, SUM({table}.value) as value'
