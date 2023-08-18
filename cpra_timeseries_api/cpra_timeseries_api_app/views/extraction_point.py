from cpra_timeseries_api_app.views.base import BaseTimeSeriesView


class ExtractionPointBaseTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['scenario_name', 'model_group_name', 'elapsed_year', 'geography']
    param_to_field = {'scenario_name': 'scenario_name', 'model_group_name': 'model_group_name',
                      'elapsed_year': 'elapsed_year', 'geography': 'geography'}
    group_by_fields = ['model_group_name', 'scenario_name', 'geography', 'elapsed_year']
    order_by_fields = ['elapsed_year']


class ExtractionPointAnnualInundationDepthMeanTimeSeriesView(ExtractionPointBaseTimeSeriesView):
    table = 'dap.vw_icm_exp_annual_depth'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'


class ExtractionPointAnnualElevationTimeSeriesView(ExtractionPointBaseTimeSeriesView):
    table = 'dap.vw_icm_exp_annual_ground_elevation'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'


class ExtractionPointAnnualMineralDepositionTimeSeriesView(ExtractionPointBaseTimeSeriesView):
    table = 'dap.vw_icm_exp_annual_mnrl_dep'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'


class ExtractionPointAnnualMineralAccretionTimeSeriesView(ExtractionPointBaseTimeSeriesView):
    table = 'dap.vw_icm_exp_annual_mnrl_accr'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'


class ExtractionPointAnnualOrganicAccumulationTimeSeriesView(ExtractionPointBaseTimeSeriesView):
    table = 'dap.vw_icm_exp_annual_org_accu'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'


class ExtractionPointAnnualOrganicAccretionTimeSeriesView(ExtractionPointBaseTimeSeriesView):
    table = 'dap.vw_icm_exp_annual_org_accr'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'


class ExtractionPointAnnualSalinityMeanTimeSeriesView(ExtractionPointBaseTimeSeriesView):
    table = 'dap.vw_icm_exp_annual_sal'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'


class ExtractionPointAnnualSalinityTwoWeekMaxTimeSeriesView(ExtractionPointBaseTimeSeriesView):
    table = 'dap.vw_icm_exp_annual_sal_2wkmax'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'


class ExtractionPointAnnualDeepSubsidenceTimeSeriesView(ExtractionPointBaseTimeSeriesView):
    table = 'dap.vw_icm_exp_annual_subsi_deep'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'


class ExtractionPointAnnualShallowSubsidenceTimeSeriesView(ExtractionPointBaseTimeSeriesView):
    table = 'dap.vw_icm_exp_annual_subsi_shallow'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'


class ExtractionPointAnnualWaterLevelMeanTimeSeriesView(ExtractionPointBaseTimeSeriesView):
    table = 'dap.vw_icm_exp_annual_stg'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'


class ExtractionPointAnnualTidalRangeMeanTimeSeriesView(ExtractionPointBaseTimeSeriesView):
    table = 'dap.vw_icm_exp_annual_trg'
    select_clause = f'{table}.elapsed_year, {table}.model_group_name, {table}.scenario_name, {table}.geography, ' \
                    f'SUM({table}.value) as value'
