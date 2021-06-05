# metabase-clickhouse-cba

A sample repository to explore deployment options for container based metabase/clickhouse application.

- [ ] Docker Compose (Local)
- [ ] Elastic Container Service (AWS)
- [ ] Elastic Kubernetes Service (AWS)
- [ ] Google Kubernetes Engine (GCP)

### Local environment setup

#### 1. Download data

```shell
$ make get_clickhouse_metabase_driver
$ make get_sample_dataset 
```

#### 2. Launch docker containers

```shell
docker compose up -d
docker compose ps  # wait until containers are healthy
```

#### 3. Loading data into clickhouse

```shell
# Commandline options for clickhouse-client
# https://clickhouse.tech/docs/en/interfaces/cli/#command-line-options
$ docker run --rm -v $(PWD):$(PWD) -w $(PWD) --network 'container:metabase-clickhouse-cba_clickhouse_1' yandex/clickhouse-client --queries-file scripts/init_clickhouse_db.sql --multiline --multiquery

# Verify load success
$ docker run -it --rm --network 'container:metabase-clickhouse-cba_clickhouse_1' yandex/clickhouse-client --query "SELECT COUNT(*) FROM coronavirus_cases_and_vaccinations.phe_vaccines_age_london_boroughs"
147264
```

#### Configure metabase

Open http://localhost:3000 in your host browser and follow the instructions. Specify 'default' for the clickhouse database user, and leave the password blank.
