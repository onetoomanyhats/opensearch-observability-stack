# OpenSearch Observability Stack

Portfolio-grade observability platform demonstrating log ingestion, centralised search, dashboards, and alerting using OpenSearch. This repository is designed to showcase practical experience operating OpenSearch for high-throughput application and infrastructure telemetry.

## Objectives

- Centralise logs from application and infrastructure sources
- Provide searchable operational visibility
- Support basic incident response and troubleshooting workflows
- Demonstrate scalable structure that can be extended for higher-volume ingestion

## Stack

- OpenSearch
- OpenSearch Dashboards
- Fluent Bit
- Sample application log generator
- Docker Compose for local development

## Repository structure

```text
.
├── dashboards/
│   └── sample-dashboard.ndjson
├── docker-compose.yml
├── fluent-bit/
│   └── fluent-bit.conf
├── generators/
│   └── app_log_generator.py
└── opensearch/
    └── index-template.json
```

## Quick start

```bash
docker compose up -d
python3 generators/app_log_generator.py
```

Then open OpenSearch Dashboards on the configured local port.

## What this demonstrates

- Centralised logging patterns
- Basic schema management via index templates
- Structured JSON logging
- Search and visualisation workflows
- Foundation for alerting, anomaly detection, and performance troubleshooting

## Production-minded considerations

For a production deployment, the next steps would be:

- TLS and authentication hardening
- Multi-node cluster design
- Index State Management policies
- Snapshot strategy
- Data retention controls
- Dedicated ingest tiers where appropriate
- Alerting integration with chat or incident tooling

## Suggested enhancements

- Add security analytics dashboards
- Add synthetic traffic generator
- Add ingestion rate and latency alerting
- Add infrastructure metrics alongside logs

## Disclaimer

This repository is designed for learning and demonstration purposes and should be hardened before production use.
