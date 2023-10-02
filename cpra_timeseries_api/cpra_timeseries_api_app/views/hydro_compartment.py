from cpra_timeseries_api_app.views.base import BaseTimeSeriesView


class HydroCompartmentBaseTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['scenario_name', 'model_group_name', 'elapsed_year', 'geography']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name',
                      'elapsed_year': 'elapsed_year', 'geography': 'geography'}
    group_by_fields = ['model_group_name', 'scenario_name', 'geography', 'elapsed_year']
    order_by_fields = ['elapsed_year']


class HydroCompartmentExceedanceBaseTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    param_fields = ['scenario_name', 'model_group_name', 'elapsed_year', 'geography', 'aep']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name',
                      'elapsed_year': 'elapsed_year', 'geography': 'geography', 'aep': 'aep'}
    group_by_fields = ['aep', 'model_group_name', 'scenario_name', 'geography', 'elapsed_year']


class HydroCompartmentStormBaseTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    param_fields = ['scenario_name', 'model_group_name', 'elapsed_year', 'geography', 'storm_id']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name',
                      'elapsed_year': 'elapsed_year', 'geography': 'geography', 'storm_id': 'storm_id'}
    group_by_fields = ['storm_id', 'model_group_name', 'scenario_name', 'geography', 'elapsed_year']


class HydroCompartmentAnnualSalinityMeanTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_annual_sal'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentDailySalinityMeanTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_daily_sal'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentAnnualSalinityTwoWeekMaxTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_annual_sal_2wkmax'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentAnnualWaterLevelMeanTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_annual_stg'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentAnnualTidalRangeMeanTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_annual_trg'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentDailyWaterLevelMeanTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_daily_stg'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentAnnualTSSMeanTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_annual_tss'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentAnnualTemperatureMeanTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_annual_tmp'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentDailyTSSMeanTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_daily_tss'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentDailyTemperatureMeanTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_daily_tmp'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentDailyTidalRangeMeanTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_daily_trg'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentAnnualLandAreaTimeSeriesView(HydroCompartmentBaseTimeSeriesView):
    table = 'dap.vw_icm_comp_annual_lnd'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, SUM({table}.value) as value'


class HydroCompartmentDecadalElevationExceedance(HydroCompartmentExceedanceBaseTimeSeriesView):
    table = 'dap.vw_clara_comp_decadal_elevation'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value_10) as value_10, SUM({table}.value_50) as value_50, ' \
                    f'SUM({table}.value_90) as value_90'


class HydroCompartmentDecadalElevationStorm(HydroCompartmentStormBaseTimeSeriesView):
    table = 'dap.vw_clara_comp_decadal_elevation_storm'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.storm_id, SUM({table}.value) as value'


class HydroCompartmentDecadalWaveHeightExceedance(HydroCompartmentExceedanceBaseTimeSeriesView):
    table = 'dap.vw_clara_comp_decadal_wave'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value_10) as value_10, SUM({table}.value_50) as value_50, ' \
                    f'SUM({table}.value_90) as value_90'


class HydroCompartmentDecadalWaveHeightStorm(HydroCompartmentStormBaseTimeSeriesView):
    table = 'dap.vw_clara_comp_decadal_wave_storm'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.storm_id, SUM({table}.value) as value'
