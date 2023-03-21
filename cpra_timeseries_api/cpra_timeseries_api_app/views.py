from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connections
from django.http import HttpResponse, JsonResponse


class BaseTimeSeriesView(APIView):
    # permission_classes = [IsAuthenticated]

    param_fields = []
    param_values = {}
    table = ''
    select_clause = ''
    where_clause = ''
    group_by_clause = ''
    order_by_clause = ''

    def get_timeseries_query(self):
        return f'SELECT {self.select_clause} ' \
               f'FROM {self.table} ' \
               f'WHERE {self.where_clause} ' \
               f'GROUP BY {self.group_by_clause} ' \
               f'ORDER BY {self.order_by_clause}'

    def parse_params(self, params):
        for key in set(params.keys()).intersection(
            set(self.param_fields)):
                self.param_values[key] = params[key]

    def execute_query(self):
        with connections['pdd'].cursor() as cursor:
            cursor.execute(self.get_timeseries_query(), [self.param_values[param] for param in self.param_fields])
            rows = [[header[0] for header in cursor.description]]
            rows += cursor.fetchall()

        return rows
    def get(self, request):
        if params := request.GET:
            self.parse_params(params)

        # At this point I should have model_groups: passed_model_groups (etc) in dict form
        timeseries_data = self.execute_query()

        return JsonResponse(
            {
                "message": "Successful.",
                "success": True,
                "data": timeseries_data,
            }
        )

class EcoregionAnnualLandAreaTimeSeriesView(BaseTimeSeriesView):
    # permission_classes = [IsAuthenticated]
    param_fields = ['scenario_model_groups', 'geographies']
    param_values = {'scenario_model_groups': [], 'geographies': []}
    table = 'icm.mv_land_veg'
    select_clause = f'{table}."Year_ICM" as year, {table}."ModelGroup" as modelGroup, {table}."Scenario" as scenario, {table}."Ecoregion" as geoId, ' \
                    f'SUM({table}."Area_m2") as value'
    where_clause = f'CONCAT({table}."Scenario", \'_\', {table}."ModelGroup") IN (%s) AND {table}."Ecoregion" IN (%s) AND {table}."VegetationCode" ' \
                   f'IN (\'LND\', \'BRG\', \'FLT\')'
    group_by_clause = f'{table}."ModelGroup", {table}."Scenario", {table}."Ecoregion", {table}."Year_ICM"'
    order_by_clause = f'{table}."Year_ICM" ASC'

class ClaraDecadalEADDTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['pumping_id', 'fragility_scenario', 'asset_type', 'scenario_model_groups', 'geographies']
    param_values = {'pumping_id': '', 'fragility_scenario': '', 'asset_type': '', 'scenario_model_groups': [], 'geographies': []}
    table = 'clara.risk'
    select_clause = f'{table}."Year_FWOA" as year, {table}."ModelGroup" as modelGroup, {table}."Scenario" as scenario, {table}."CommunityID" as geoId, ' \
                    f'SUM({table}."EAD_10") as min, SUM({table}."EAD_50" - {table}."EAD_10") as q1, SUM({table}."EAD_50") as median,' \
                    f' SUM({table}."EAD_90" - {table}."EAD_50") as q3, SUM({table}."EAD_90") as max'
    where_clause = f'{table}."PumpingID" = %s AND {table}."FragilityScenario" = %s AND {table}."AssetType" IN (%s) AND ' \
                   f'CONCAT({table}."Scenario", \'_\', {table}."ModelGroup") IN (%s) AND {table}."CommunityID" IN (%s)'
    group_by_clause = f'{table}."ModelGroup", {table}."Scenario", {table}."CommunityID", {table}."Year_FWOA"'
    order_by_clause = f'{table}."Year_FWOA" ASC'