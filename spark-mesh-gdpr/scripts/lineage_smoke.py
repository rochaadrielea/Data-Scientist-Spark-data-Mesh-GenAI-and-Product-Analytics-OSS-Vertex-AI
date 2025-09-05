import os
from openlineage.client import OpenLineageClient
from openlineage.client.run import RunEvent, RunState, Run, Job, Dataset
from datetime import datetime, timezone
from uuid import uuid4

client = OpenLineageClient(url="http://localhost:5000")
job = Job(namespace="spark-mesh", name="lineage_smoke_job")
run = Run(runId=str(uuid4()))
now = datetime.now(timezone.utc).isoformat()

evt = RunEvent(
    eventTime=now,
    eventType=RunState.START,
    run=run,
    job=job,
    inputs=[Dataset(namespace="minio", name="bronze/seed.parquet")],
    outputs=[Dataset(namespace="minio", name="silver/seed_clean.parquet")]
)
client.emit(evt)

client.emit(RunEvent(eventTime=now, eventType=RunState.COMPLETE, run=run, job=job,
                     inputs=evt.inputs, outputs=evt.outputs))
