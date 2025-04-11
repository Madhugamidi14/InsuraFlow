#!/bin/bash
export INSURAFLOW_CONFIG_PATH="D:/Data Engineering Prep/Pyspark/config/config.yaml"
dagster dev

# Optional: Wait 10 seconds to let Dagster boot up
#sleep 10

# Automatically materialize all assets
#dagster asset materialize --repository insuraflow_dag