# metabase-clickhouse-cba

A sample repository to explore deployment options for container based metabase/clickhouse application.

- [ ] Docker Compose (Local)
- [ ] Elastic Container Service (AWS)
- [ ] Elastic Kubernetes Service (AWS)
- [ ] Google Kubernetes Engine (GCP)

### Loading data into clickhouse

```
# Download the dataset
$ make get_sample_dataset

# Load into clickhouse
# https://clickhouse.tech/docs/en/interfaces/cli/#command-line-options
$ docker run --rm -v $(PWD):$(PWD) -w $(PWD) --network 'container:metabase-clickhouse-cba_clickhouse_1' yandex/clickhouse-client --queries-file scripts/init_clickhouse_db.sql --multiquery --multiline

# Verify load success
$ docker run -it --rm --network 'container:metabase-clickhouse-cba_clickhouse_1' yandex/clickhouse-client --query "SELECT COUNT(*) FROM coronavirus_cases_and_vaccinations.phe_vaccines_age_london_boroughs"
147264
```
