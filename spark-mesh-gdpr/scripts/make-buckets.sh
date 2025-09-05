#!/usr/bin/env bash
set -euo pipefail
export MC_HOST_minio=http://minioadmin:minioadmin@localhost:9000
mc alias set minio http://localhost:9000 minioadmin minioadmin >/dev/null
mc mb -p minio/bronze || true
mc mb -p minio/silver || true
mc mb -p minio/gold || true
mc mb -p minio/spark-events || true
