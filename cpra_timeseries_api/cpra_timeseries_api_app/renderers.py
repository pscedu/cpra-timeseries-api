import unicodecsv as csv
from rest_framework.renderers import BaseRenderer
from six import BytesIO


class CSVRenderer(BaseRenderer):
    """
    Renderer which serializes to CSV
    """

    media_type = "text/csv"
    format = "csv"

    def render(self, data, media_type=None, renderer_context={}, writer_opts=None):
        """
        Renders serialized *data* into CSV. For a dictionary:
        """
        csv_buffer = BytesIO()
        csv_writer = csv.writer(csv_buffer)
        for row in data:
            csv_writer.writerow(row)

        return csv_buffer.getvalue()
