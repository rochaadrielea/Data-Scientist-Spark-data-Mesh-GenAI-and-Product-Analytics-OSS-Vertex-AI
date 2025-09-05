# Spark-Optimization-Data-Mesh-Project-oss-Databricks-agnostic-LLM-AI-

```bash
conda env create -f env/conda-environment.yml
conda activate spark-mesh-gdpr
docker compose up -d
bash scripts/make-buckets.sh
python scripts/spark_smoke.py
python scripts/lineage_smoke.py

- [ ] `conda activate spark-mesh-gdpr` works; imports `pyspark`, `great_expectations`, `openlineage` OK  
- [ ] `docker compose ps` shows **minio, postgres, marquez, marquez-ui, openmetadata, ranger, spark-history** healthy  
- [ ] MinIO buckets `bronze/ silver/ gold/ spark-events/` exist  
- [ ] Running `scripts/spark_smoke.py` creates an app in **Spark History**  
- [ ] Running `scripts/lineage_smoke.py` creates job/datasets in **Marquez UI**  
- [ ] README has a copy-paste quick-start that someone else could run on a fresh machine