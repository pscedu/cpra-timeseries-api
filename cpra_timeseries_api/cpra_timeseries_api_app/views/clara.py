from cpra_timeseries_api_app.views.base import BaseTimeSeriesView


class ClaraBaseTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['pumping_id', 'fragility_scenario', 'asset_type', 'scenario_name', 'model_group_name', 'geography',
                    'elapsed_year']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name',
                      'pumping_id': 'pumping_id', 'fragility_scenario': 'fragility_scenario',
                      'asset_type': 'asset_type', 'geography': 'geography', 'elapsed_year': 'elapsed_year'}
    table = ''
    group_by_fields = ['model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario',
                       'asset_type', 'elapsed_year']
    order_by_fields = ['elapsed_year']


class ClaraNSBaseTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['pumping_id', 'fragility_scenario', 'asset_type', 'scenario_name', 'model_group_name', 'geography',
                    'elapsed_year', 'participation_rate', 'ns_project_id']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name',
                      'pumping_id': 'pumping_id', 'fragility_scenario': 'fragility_scenario',
                      'asset_type': 'asset_type', 'geography': 'geography', 'elapsed_year': 'elapsed_year',
                      'participation_rate': 'ns_project_id'}
    table = ''
    group_by_fields = ['model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario',
                       'participation_rate', 'ns_project_id', 'asset_type', 'elapsed_year']
    order_by_fields = ['elapsed_year']


class ClaraDecadalEADDTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_ead'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value_10) as value_10, SUM({table}.value_50) as value_50, ' \
                    f'SUM({table}.value_90) as value_90, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'


class ClaraDecadalNSEADDTimeSeriesView(ClaraNSBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_ead_ns'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value_10) as value_10, SUM({table}.value_50) as value_50, ' \
                    f'SUM({table}.value_90) as value_90, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type, {table}.participation_rate, {table}.ns_project_id'


class ClaraDecadalEASDTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_easd'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value_10) as value_10, SUM({table}.value_50) as value_50, ' \
                    f'SUM({table}.value_90) as value_90, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'


class ClaraDecadalNSEASDTimeSeriesView(ClaraNSBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_easd_ns'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value_10) as value_10, SUM({table}.value_50) as value_50, ' \
                    f'SUM({table}.value_90) as value_90, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type, {table}.participation_rate, {table}.ns_project_id'


class ClaraDecadalDamageTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_damage'
    param_fields = ['aep', 'pumping_id', 'fragility_scenario', 'asset_type', 'scenario_name', 'model_group_name',
                    'geography', 'elapsed_year']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name',
                      'pumping_id': 'pumping_id', 'fragility_scenario': 'fragility_scenario',
                      'asset_type': 'asset_type', 'geography': 'geography', 'elapsed_year': 'elapsed_year',
                      'aep': 'aep'}
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value_10) as value_10, SUM({table}.value_50) as value_50, ' \
                    f'SUM({table}.value_90) as value_90, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'
    group_by_fields = ['aep', 'model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario',
                       'asset_type', 'elapsed_year']


class ClaraDecadalExposureAssetCountTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['pumping_id', 'fragility_scenario', 'asset_type', 'scenario_name', 'model_group_name', 'geography',
                    'elapsed_year', 'exposure_type', 'aep']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name',
                      'pumping_id': 'pumping_id', 'fragility_scenario': 'fragility_scenario',
                      'asset_type': 'asset_type', 'geography': 'geography', 'elapsed_year': 'elapsed_year',
                      'exposure_type': 'exposure_type', 'aep': 'aep'}
    table = 'dap.vw_clara_comm_decadal_exposure'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value) as value, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type, {table}.exposure_type'
    group_by_fields = ['aep', 'model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario',
                       'asset_type', 'exposure_type', 'elapsed_year']
    order_by_fields = ['elapsed_year']


class ClaraDecadalExposureCriticalInfrastructureCountTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['pumping_id', 'fragility_scenario', 'scenario_name', 'model_group_name', 'geography',
                    'elapsed_year', 'exposure_type', 'aep', 'clara_group_id', 'source_dataset']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name',
                      'pumping_id': 'pumping_id', 'fragility_scenario': 'fragility_scenario',
                      'asset_type': 'asset_type', 'geography': 'geography', 'elapsed_year': 'elapsed_year',
                      'exposure_type': 'exposure_type', 'aep': 'aep', 'clara_group_id': 'clara_group_id',
                      'source_dataset': 'source_dataset'}
    table = 'dap.vw_clara_comm_decadal_exposure_ci'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value) as value, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.exposure_type, {table}.clara_group_id, ' \
                    f'{table}.source_dataset'
    group_by_fields = ['aep', 'model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario',
                       'exposure_type', 'clara_group_id', 'source_dataset', 'elapsed_year']
    order_by_fields = ['elapsed_year']


class ClaraDecadalExposureHistoricPropertiesCountTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['pumping_id', 'fragility_scenario', 'scenario_name', 'model_group_name', 'geography',
                    'elapsed_year', 'exposure_type', 'aep']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name',
                      'pumping_id': 'pumping_id', 'fragility_scenario': 'fragility_scenario',
                      'geography': 'geography', 'elapsed_year': 'elapsed_year',
                      'exposure_type': 'exposure_type', 'aep': 'aep'}
    table = 'dap.vw_clara_comm_decadal_exposure_hp'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep, SUM({table}.value) as value, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.exposure_type'
    group_by_fields = ['aep', 'model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario',
                       'exposure_type', 'elapsed_year']
    order_by_fields = ['elapsed_year']
