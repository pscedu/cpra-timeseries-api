from cpra_timeseries_api_app.views.base import BaseTimeSeriesView


class ClaraBaseTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['pumping_id', 'fragility_scenario', 'asset_type', 'scenario', 'model_group_name', 'geography', 'time']
    param_to_field = {'scenario': 'Scenario', 'model_group_name': 'ModelGroup', 'pumping_id': 'PumpingID', 'fragility_scenario': 'FragilityScenario', 'asset_type': 'AssetType', 'geography': 'CommunityID', 'time': 'Year_FWOA'}
    table = 'clara.risk'
    group_by_fields = ['ModelGroup', 'Scenario', 'CommunityID', 'PumpingID', 'FragilityScenario', 'AssetType', 'Year_FWOA']
    order_by_fields = ['Year_FWOA']


class ClaraDecadalEADDTimeSeriesView(ClaraBaseTimeSeriesView):
    table = ClaraBaseTimeSeriesView.table
    select_clause = f'{table}."Year_FWOA" as time, {table}."ModelGroup" as model_group_name, {table}."Scenario" as scenario, {table}."CommunityID" as geography, ' \
                    f'SUM({table}."EAD_10") as value_min, SUM({table}."EAD_50" - {table}."EAD_10") as value_q1, SUM({table}."EAD_50") as value_median,' \
                    f' SUM({table}."EAD_90" - {table}."EAD_50") as value_q3, SUM({table}."EAD_90") as value_max, {table}."PumpingID" as pumping_id, ' \
                    f'{table}."FragilityScenario" as fragility_scenario, {table}."AssetType" as asset_type'


class ClaraDecadalEASDTimeSeriesView(ClaraBaseTimeSeriesView):
    table = ClaraBaseTimeSeriesView.table
    select_clause = f'{table}."Year_FWOA" as time, {table}."ModelGroup" as model_group_name, {table}."Scenario" as scenario, {table}."CommunityID" as geography, ' \
                    f'SUM({table}."EASD_10") as value_min, SUM({table}."EASD_50" - {table}."EASD_10") as value_q1, SUM({table}."EASD_50") as value_median,' \
                    f' SUM({table}."EASD_90" - {table}."EASD_50") as value_q3, SUM({table}."EASD_90") as value_max, {table}."PumpingID" as pumping_id, ' \
                    f'{table}."FragilityScenario" as fragility_scenario, {table}."AssetType" as asset_type'


class ClaraDecadalDamageTimeSeriesView(ClaraBaseTimeSeriesView):
    table = 'dap.vw_clara_comm_decadal_damage'
    param_fields = ['pumping_id', 'fragility_scenario', 'asset_type', 'scenario_name', 'model_group_name', 'geography', 'elapsed_time']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name', 'pumping_id': 'pumping_id', 'fragility_scenario': 'fragility_scenario', 'asset_type': 'asset_type', 'geography': 'geography', 'elapsed_time': 'elapsed_time'}
    select_clause = f'{table}.elapsed_time, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'{table}.aep as aep, SUM({table}.value_min) as value_min, SUM({table}.value_q1) as value_q1, SUM({table}.value_median) as value_median, ' \
                    f'SUM({table}.value_q3) as value_q3, SUM({table}.value_max) as value_max, {table}.pumping_id, ' \
                    f'{table}.fragility_scenario, {table}.asset_type'
    group_by_fields = ['aep', 'model_group_name', 'scenario_name', 'geography', 'pumping_id', 'fragility_scenario', 'asset_type', 'elapsed_time']
    order_by_fields = ['elapsed_time']
