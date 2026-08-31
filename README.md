# cpra-timeseries-api
API used to gather timeseries data from PDD.

For API docs, please copy and paste [the YAML doc](cpra-timeseries-api-spec.yaml) into the [Swagger API Editor](https://editor.swagger.io/).

## Configuration

The API reads its settings from a `config.json` in the working directory. Copy
[`example_config.json`](example_config.json) and fill in the secret key,
database credentials and allowed hosts.

## Container image

Each release publishes an image to the GitHub Container Registry:

```
ghcr.io/pscedu/cpra-timeseries-api:<version>
```

The image runs gunicorn on port 8000 and expects `config.json` to be mounted
into the working directory:

```
docker run --rm -p 8000:8000 \
  -v /path/to/config.json:/usr/src/app/config.json \
  ghcr.io/pscedu/cpra-timeseries-api:<version>
```

To build it locally:

```
docker build . --tag cpra-timeseries-api:dev
```

## Releases

Releases are managed by [Release Please](https://github.com/googleapis/release-please).
Commits to `main` must follow the
[Conventional Commits](https://www.conventionalcommits.org/) format, for example:

```
feat(clara): add annual temperature endpoint
fix(parish): correct inheritance of the base view
```

Release Please keeps an open pull request that collects the changelog and the
next version number. Merging that pull request tags the release and triggers the
container image build.
