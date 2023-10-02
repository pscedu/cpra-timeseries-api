from cpra_timeseries_api_app.views.base import BaseTimeSeriesView


class BlockGroupBaseTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['scenario_name', 'model_group_name', 'geography', 'elapsed_year', 'ssp', 'migration']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name',
                      'geography': 'geography', 'elapsed_year': 'elapsed_year', 'ssp': 'ssp', 'migration': 'migration'}
    group_by_fields = ['model_group_name', 'scenario_name', 'geography', 'ssp', 'migration', 'elapsed_year']
    order_by_fields = ['elapsed_year']


class BlockGroupDecadalPopulationChangeTimeSeriesView(BlockGroupBaseTimeSeriesView):
    table = 'dap.vw_clara_bg_decadal_population'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.ssp, {table}.migration, SUM({table}.value_05) as value_05, ' \
                    f'SUM({table}.value_50) as value_50, SUM({table}.value_95) as value_95'
