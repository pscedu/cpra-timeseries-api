from cpra_timeseries_api_app.views.base import BaseTimeSeriesView


class HydroCompartmentBaseTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['scenario_name', 'model_group_name', 'elapsed_time', 'geography']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name', 'elapsed_time': 'elapsed_time', 'geography': 'geography'}
    group_by_fields = ['model_group_name', 'scenario_name', 'geography', 'elapsed_time']
    order_by_fields = ['elapsed_time']


class HydroCompartmentAnnualSalinityMeanTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_annual_sal'
    select_clause = f'{table}.elapsed_time, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentAnnualSalinityTwoWeekMaxTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_annual_sal_2wkmax'
    select_clause = f'{table}.elapsed_time, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentAnnualWaterLevelMeanTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_annual_stg'
    select_clause = f'{table}.elapsed_time, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentAnnualTSSMeanTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_annual_tss'
    select_clause = f'{table}.elapsed_time, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentAnnualLandAreaTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_annual_lnd'
    select_clause = f'{table}.elapsed_time, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentAnnualTemperatureMeanTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_annual_tmp'
    select_clause = f'{table}.elapsed_time, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'
