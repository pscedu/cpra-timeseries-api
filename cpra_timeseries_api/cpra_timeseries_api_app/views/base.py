from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connections
from rest_framework.settings import api_settings
from cpra_timeseries_api_app.renderers import CSVRenderer

import json


class BaseTimeSeriesView(APIView):
    # permission_classes = [IsAuthenticated]
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES) + (CSVRenderer,)

    param_fields = []
    param_values = {}
    param_to_field = {}
    group_by_fields = []
    order_by_fields = []
    table = ''
    select_clause = ''
    where_clause = ''
    group_by_clause = ''
    order_by_clause = ''

    def get_timeseries_query(self, param_values):
        return f'SELECT {self.select_clause} ' \
               f'FROM {self.table} ' \
               f' {self.build_where_clause(param_values)} ' \
               f'GROUP BY {self.build_group_by_clause()} ' \
               f'ORDER BY {self.build_order_by_clause()}'

    def parse_params(self, params):
        param_values = {}
        for key in set(params.keys()).intersection(
            set(self.param_fields)):
                val = params[key]
                param_values[key] = val if type(val) != list else tuple(val)
        return param_values

    def build_where_clause(self, param_values):
        where_clause = self.where_clause
        for field, val in param_values.items():
            if not val:
                continue

            where_field = f'{self.table}."{self.param_to_field[field]}"'
            where_clause += f'{where_field}' if not where_clause else f' AND {where_field}'
            where_clause += ' = %s' if type(val) != tuple else ' IN %s'
        return f'WHERE {where_clause}' if where_clause else where_clause

    def build_group_by_clause(self):
        group_by_clause = self.group_by_clause
        for field in self.group_by_fields:
            group_by_clause += f'{self.table}."{field}"' if not group_by_clause else f', {self.table}."{field}"'
        return group_by_clause

    def build_order_by_clause(self):
        order_by_clause = self.order_by_clause
        for field in self.order_by_fields:
            order_by_clause += f'{self.table}."{field}"' if not order_by_clause else f', {self.table}."{field}"'
        return f'{order_by_clause} ASC'

    def execute_query(self, param_values):
        rows = []
        scenarios = param_values.pop('scenarios', [])
        with connections['pdd'].cursor() as cursor:
            if not scenarios:
                merged_params = self.parse_params(param_values)
                cursor.execute(self.get_timeseries_query(merged_params), [val for val in merged_params.values()])
                rows = [[header[0] for header in cursor.description]]
                rows += cursor.fetchall()
            else:
                for scenario in scenarios:
                    scenario.update(param_values)
                    merged_params = self.parse_params(scenario)
                    cursor.execute(self.get_timeseries_query(merged_params), [val for val in merged_params.values()])
                    if not rows:
                        rows = [[header[0] for header in cursor.description]]
                    rows += cursor.fetchall()

        return rows

    def get(self, request):
        param_values = json.loads(request.GET.get('filters', "{}"))

        # At this point I should have model_group_names: passed_model_group_names (etc) in dict form
        timeseries_data = self.execute_query(param_values)

        if request.accepted_renderer.format == 'csv':
            return Response(timeseries_data, headers={'Content-Disposition': 'attachment; filename="timeseries.csv"'})
        else:
            return Response({
                "message": "Successful.",
                "success": True,
                "data": timeseries_data
            })