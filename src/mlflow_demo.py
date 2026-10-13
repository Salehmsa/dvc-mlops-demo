import json
import mlflow

# قراءة نتائج DVC
with open("metrics.json", "r") as f:
    metrics = json.load(f)

mlflow.set_experiment("saleh-dvc-demo")

with mlflow.start_run(run_name="metrics_from_dvc"):

    mlflow.log_param("pipeline", "dvc")

    mlflow.log_metric(
        "total_sales",
        metrics["total_sales"]
    )

    mlflow.log_metric(
        "num_rows",
        metrics["num_rows"]
    )

print("MLflow run completed")