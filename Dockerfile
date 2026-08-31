# Django 4.1 supports Python 3.8 - 3.11, so 3.11 is the newest usable base.
FROM python:3.11-slim
LABEL maintainer="mjyoder@psc.edu"
LABEL org.opencontainers.image.source="https://github.com/pscedu/cpra-timeseries-api"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt \
    && python -m pip cache purge

# Copy the contents of the Django project so that manage.py and the
# cpra_timeseries_api package sit directly in the working directory.
COPY cpra_timeseries_api/ ./
COPY example_config.json ./

# settings.py reads config.json from the working directory, so mount one:
#   docker run -v /path/to/config.json:/usr/src/app/config.json ...
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--access-logfile", "-", \
     "cpra_timeseries_api.wsgi:application"]
