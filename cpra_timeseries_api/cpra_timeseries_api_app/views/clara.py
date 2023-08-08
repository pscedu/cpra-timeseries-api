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
                    f'SUM({table}.value_min) as value_min, SUM({table}.value_q1) as value_q1, SUM({table}.value_median) as value_median,' \
                    f' SUM({table}.value_q3) as value_q3, SUM({table}.value_max) as value_max, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'


class ClaraDecadalNSEADDTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_ead_ns'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value_min) as value_min, SUM({table}.value_q1) as value_q1, SUM({table}.value_median) as value_median,' \
                    f' SUM({table}.value_q3) as value_q3, SUM({table}.value_max) as value_max, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'


class ClaraDecadalEASDTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_easd'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value_min) as value_min, SUM({table}.value_q1) as value_q1, SUM({table}.value_median) as value_median,' \
                    f' SUM({table}.value_q3) as value_q3, SUM({table}.value_max) as value_max, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'


class ClaraDecadalNSEASDTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_easd_ns'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value_min) as value_min, SUM({table}.value_q1) as value_q1, SUM({table}.value_median) as value_median,' \
                    f' SUM({table}.value_q3) as value_q3, SUM({table}.value_max) as value_max, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'


class ClaraDecadalDamageTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_damage'
    param_fields = ['pumping_id', 'fragility_scenario', 'asset_type', 'scenario_name', 'model_group_name', 'geography', 'elapsed_year']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name', 'pumping_id': 'pumping_id', 'fragility_scenario': 'fragility_scenario', 'asset_type': 'asset_type', 'geography': 'geography', 'elapsed_year': 'elapsed_year'}
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value_min) as value_min, SUM({table}.value_q1) as value_q1, SUM({table}.value_median) as value_median, ' \
                    f'SUM({table}.value_q3) as value_q3, SUM({table}.value_max) as value_max, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'
    group_by_fields = ['aep', 'model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario', 'asset_type', 'elapsed_year']


class ClaraDecadalExposureAssetCountTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_exposure'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value) as value, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'
    group_by_fields = ['aep', 'model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario', 'asset_type', 'elapsed_year']


class ClaraDecadalExposureCriticalInfrastructureCountTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'PDD clara.exposure_critical_infrastructure'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value) as value, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'
    group_by_fields = ['aep', 'model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario', 'asset_type', 'elapsed_year']


class ClaraDecadalExposureHistoricPropertiesCountTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'PDD clara.exposure_historic_properties'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value) as value, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'
    group_by_fields = ['aep', 'model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario', 'asset_type', 'elapsed_year']
