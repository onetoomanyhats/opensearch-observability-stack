#!/usr/bin/env bash
set -euo pipefail

curl -sS -X PUT "http://localhost:9200/_index_template/app-logs-template"   -H 'Content-Type: application/json'   --data-binary @opensearch/index-template.json

echo
echo "Index template uploaded."
