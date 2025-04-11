from dagster import asset, Output
import papermill as pm
import os
import yaml
import logging

# Load dynamic configuration
with open("D:\Data Engineering Prep\Pyspark\config\config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Set up logger
log_file = config["log_file"]
os.makedirs(os.path.dirname(log_file), exist_ok=True)

logger = logging.getLogger("dagster_assets")
if not logger.hasHandlers():
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("[DAGSTER] %(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

@asset
def run_cleaning_notebook() -> Output[str]:
    config_path = os.getenv("INSURAFLOW_CONFIG_PATH")
    if not config_path or not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")
    
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
        
    input_nb = config["notebooks"]["cleaning"]["input"]
    temp_nb = config["notebooks"]["cleaning"]["output_temp"]
    input_path = config["paths"]["raw_data"]
    output_json = config["paths"]["cleaned_data"]

    try:
        logger.info(f"Executing cleaning notebook: {input_nb}")
        pm.execute_notebook(
            input_path=input_nb,
            output_path=temp_nb,
            parameters={
                "input_path": input_path,
                "output_path": output_json,
                "config_path": config_path
            }
        )
        if not os.path.exists(output_json):
            raise FileNotFoundError(f"Expected output file not found: {output_json}")
        logger.info(f"Cleaning notebook completed. Output written to: {output_json}")
        return Output(output_json)
    finally:
        if os.path.exists(temp_nb):
            os.remove(temp_nb)
            logger.info(f"Temporary notebook removed: {temp_nb}")


@asset
def run_transformation_notebook(run_cleaning_notebook: str) -> str:
    config_path = os.getenv("INSURAFLOW_CONFIG_PATH")
    if not config_path or not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")
    
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
        
        
    input_nb = config["notebooks"]["transforming"]["input"]
    temp_nb = config["notebooks"]["transforming"]["output_temp"]
    input_path = config["paths"]["cleaned_data"]
    output_json = config["paths"]["transformed_data"]

    try:
        logger.info(f"Executing transformation notebook: {input_nb}")
        pm.execute_notebook(
            input_path=input_nb,
            output_path=temp_nb,
            parameters={
                "input_path": input_path,
                "output_path": output_json
            }
        )
        if not os.path.exists(output_json):
            raise FileNotFoundError(f"Expected output file not found: {output_json}")
        logger.info(f"Transformation notebook completed. Output written to: {output_json}")
        return output_json
    finally:
        if os.path.exists(temp_nb):
            os.remove(temp_nb)
            logger.info(f"Temporary notebook removed: {temp_nb}")
