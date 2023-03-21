from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connections
from django.http import HttpResponse, JsonResponse


class BaseTimeSeriesView(APIView):
    # permission_classes = [IsAuthenticated]

    param_fields = []
    param_values = {}
    param_to_field = {}
    table = ''
    select_clause = ''
    where_clause = ''
    group_by_clause = ''
    order_by_clause = ''

    def get_timeseries_query(self):
        return f'SELECT {self.select_clause} ' \
               f'FROM {self.table} ' \
               f'WHERE {self.build_where_clause()} ' \
               f'GROUP BY {self.group_by_clause} ' \
               f'ORDER BY {self.order_by_clause}'

    def parse_params(self, params):
        for key in set(params.keys()).intersection(
            set(self.param_fields)):
                val = params.getlist(key)
                self.param_values[key] = params[key] if len(val) == 1 else tuple(val)

    def build_where_clause(self):
        where_clause = self.where_clause
        for field, val in self.param_values.items():
            where_field = f'{self.table}."{self.param_to_field[field]}"' if field != "scenario_model_groups" else f'CONCAT({self.table}."Scenario", \'_\', {self.table}."ModelGroup")'
            where_clause += f'{where_field}' if not where_clause else f' AND {where_field}'
            where_clause += ' = %s' if type(val) != tuple else ' IN %s'
        return where_clause


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
    param_to_field = {'geographies': 'Ecoregion'}
    table = 'icm.mv_land_veg'
    select_clause = f'{table}."Year_ICM" as year, {table}."ModelGroup" as modelGroup, {table}."Scenario" as scenario, {table}."Ecoregion" as geoId, ' \
                    f'SUM({table}."Area_m2") as value'
    where_clause = f'{table}."VegetationCode" IN (\'LND\', \'BRG\', \'FLT\')'
    group_by_clause = f'{table}."ModelGroup", {table}."Scenario", {table}."Ecoregion", {table}."Year_ICM"'
    order_by_clause = f'{table}."Year_ICM" ASC'

class ClaraDecadalEADDTimeSeriesView(BaseTimeSeriesView):
    param_fields = ['pumping_id', 'fragility_scenario', 'asset_type', 'scenario_model_groups', 'geographies']
    param_values = {'pumping_id': '', 'fragility_scenario': '', 'asset_type': '', 'scenario_model_groups': [], 'geographies': []}
    param_to_field = {'pumping_id': 'PumpingID', 'fragility_scenario': 'FragilityScenario', 'asset_type': 'AssetType', 'geographies': 'CommunityID'}
    table = 'clara.risk'
    select_clause = f'{table}."Year_FWOA" as year, {table}."ModelGroup" as modelGroup, {table}."Scenario" as scenario, {table}."CommunityID" as geoId, ' \
                    f'SUM({table}."EAD_10") as min, SUM({table}."EAD_50" - {table}."EAD_10") as q1, SUM({table}."EAD_50") as median,' \
                    f' SUM({table}."EAD_90" - {table}."EAD_50") as q3, SUM({table}."EAD_90") as max'
    group_by_clause = f'{table}."ModelGroup", {table}."Scenario", {table}."CommunityID", {table}."Year_FWOA"'
    order_by_clause = f'{table}."Year_FWOA" ASC'