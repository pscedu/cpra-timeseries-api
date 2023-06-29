from cpra_timeseries_api_app.views.base import BaseTimeSeriesView


class HydroCompartmentBaseTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['scenario_name', 'model_group_name', 'elapsed_time', 'geography']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name', 'elapsed_time': 'elapsed_time', 'geography': 'geography'}
    group_by_fields = ['model_group_name', 'scenario_name', 'geography', 'elapsed_time']
    order_by_fields = ['elapsed_time']


class HydroCompartmentExceedanceBaseTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    group_by_fields = ['aep', 'model_group_name', 'scenario_name', 'geography', 'elapsed_time']


class HydroCompartmentStormBaseTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    group_by_fields = ['storm_id', 'model_group_name', 'scenario_name', 'geography', 'elapsed_time']


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


class HydroCompartmentDecadalElevationExceedance(HydroCompartmentExceedanceBaseTimeSeriesView):
    table = 'dap.vw_clara_comp_decadal_elevation'
    select_clause = f'{table}.elapsed_time, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value_min) as value_min, SUM({table}.value_q1) as value_q1, SUM({table}.value_median) as value_median, ' \
                    f'SUM({table}.value_q3) as value_q3, SUM({table}.value_max) as value_max'


class HydroCompartmentDecadalElevationStorm(HydroCompartmentStormBaseTimeSeriesView):
    table = 'dap.vw_clara_comp_decadal_elevation_storm'
    select_clause = f'{table}.elapsed_time, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.storm_id, SUM({table}.value) as value'


class HydroCompartmentDecadalWaveHeightExceedance(HydroCompartmentExceedanceBaseTimeSeriesView):
    table = 'dap.vw_clara_comp_decadal_wave'
    select_clause = f'{table}.elapsed_time, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value_min) as value_min, SUM({table}.value_q1) as value_q1, SUM({table}.value_median) as value_median, ' \
                    f'SUM({table}.value_q3) as value_q3, SUM({table}.value_max) as value_max'


class HydroCompartmentDecadalWaveHeightStorm(HydroCompartmentStormBaseTimeSeriesView):
    table = 'dap.vw_clara_comp_decadal_wave_storm'
    select_clause = f'{table}.elapsed_time, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.storm_id, SUM({table}.value) as value'
