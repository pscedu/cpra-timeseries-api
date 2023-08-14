from cpra_timeseries_api_app.views.base import BaseTimeSeriesView


class ClaraBaseTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['pumping_id', 'fragility_scenario', 'asset_type', 'scenario_name', 'model_group_name', 'geography', 'elapsed_year']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name',
                      'pumping_id': 'pumping_id', 'fragility_scenario': 'fragility_scenario',
                      'asset_type': 'asset_type', 'geography': 'geography', 'elapsed_year': 'elapsed_year'}
    table = ''
    group_by_fields = ['model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario', 'asset_type', 'elapsed_year']
    order_by_fields = ['elapsed_year']


class ClaraDecadalEADDTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_ead'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value_10) as value_10, SUM({table}.value_50) as value_50, ' \
                    f'SUM({table}.value_90) as value_90, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'


class ClaraDecadalNSEADDTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_ead_ns'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value_10) as value_10, SUM({table}.value_50) as value_50, ' \
                    f'SUM({table}.value_90) as value_90, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'


class ClaraDecadalEASDTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_easd'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value_10) as value_10, SUM({table}.value_50) as value_50, ' \
                    f'SUM({table}.value_90) as value_90, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'


class ClaraDecadalNSEASDTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_easd_ns'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value_10) as value_10, SUM({table}.value_50) as value_50, ' \
                    f'SUM({table}.value_90) as value_90, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'


class ClaraDecadalDamageTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_damage'
    param_fields = ['pumping_id', 'fragility_scenario', 'asset_type', 'scenario_name', 'model_group_name', 'geography', 'elapsed_year']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name', 'pumping_id': 'pumping_id', 'fragility_scenario': 'fragility_scenario', 'asset_type': 'asset_type', 'geography': 'geography', 'elapsed_year': 'elapsed_year'}
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value_10) as value_10, SUM({table}.value_50) as value_50, ' \
                    f'SUM({table}.value_90) as value_90, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'
    group_by_fields = ['aep', 'model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario', 'asset_type', 'elapsed_year']
    group_by_fields = ['aep', 'model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario', 'asset_type', 'elapsed_year']


class ClaraDecadalExposureBaseTimeSeriesView(ClaraBaseTimeSeriesView):
    param_fields = ['pumping_id', 'fragility_scenario', 'asset_type', 'scenario_name', 'model_group_name', 'geography',
                    'elapsed_year', 'exposure_type', 'aep']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name',
                      'pumping_id': 'pumping_id', 'fragility_scenario': 'fragility_scenario',
                      'asset_type': 'asset_type', 'geography': 'geography', 'elapsed_year': 'elapsed_year',
                      'exposure_type': 'exposure_type', 'aep': 'aep'}
    group_by_fields = ['aep', 'model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario',
                       'asset_type', 'exposure_type', 'elapsed_year']
    order_by_fields = ['elapsed_year']


class ClaraDecadalExposureAssetCountTimeSeriesView(ClaraDecadalExposureBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_exposure'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value) as value, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type, {table}.exposure_type'


class ClaraDecadalExposureCriticalInfrastructureCountTimeSeriesView(ClaraDecadalExposureBaseTimeSeriesView):
    table = 'PDD clara.exposure_critical_infrastructure'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value) as value, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type, {table}.exposure_type'


class ClaraDecadalExposureHistoricPropertiesCountTimeSeriesView(ClaraDecadalExposureBaseTimeSeriesView):
    table = 'PDD clara.exposure_historic_properties'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value) as value, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type, {table}.exposure_type'
