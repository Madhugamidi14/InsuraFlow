# 🛡️ InsuraFlow

![PySpark](https://img.shields.io/badge/PySpark-Data%20Engineering-orange?style=flat-square&logo=apache-spark)
![Apache Spark](https://img.shields.io/badge/Spark-Optimized-green?style=flat-square&logo=apache-spark)
![JSON](https://img.shields.io/badge/Data-JSON-blue?style=flat-square)
![Dagster](https://img.shields.io/badge/Orchestration-Dagster-purple?style=flat-square&logo=dagster)
![GitHub last commit](https://img.shields.io/github/last-commit/Madhugamidi14/InsuraFlow)

## 🚀 Project Overview

**InsuraFlow** is a full-fledged, industry-standard, PySpark-based data engineering pipeline that ingests, cleans, transforms, and prepares insurance data for analytics and visualization. Designed with modularity, scalability, and real-world inconsistencies in mind, this project is perfect for demonstrating end-to-end data engineering capabilities using big data tools It’s designed for modularity, fault-tolerance, and real-world data inconsistencies — powered by PySpark + Dagster.


---

Insurance datasets often contain inconsistencies, formatting issues, and require enrichment for meaningful insights. **InsuraFlow** handles:

- 🧹 **Cleaning**: Standardizes, nullifies, formats fields (e.g. gender, phone, dates)
- 🔁 **Transformation**: Adds derived features like risk level and full address
- ⚙️ **Orchestration with Dagster**: Jupyter notebooks materialized as assets
- 📓 **Notebook Automation**: Powered by Papermill
- 🔧 **Central Config**: YAML-based dynamic file paths
- 🧾 **Logging**: Central log file (`logs/pipeline.log`) for all pipeline steps

---

## 📂 Project Structure

```bash
InsuraFlow/
├── config/
│   └── config.yaml                # Central YAML for file paths + notebooks
├── input/                         # ⚠️ Ignored - Raw input files (e.g., insurance_data.json)
├── output/                        # ⚠️ Ignored - Cleaned & transformed output files
├── notebooks/
│   ├── cleaning/
│   │   └── data_cleaning.ipynb    # Cleaning logic with PySpark
│   └── transforming/
│       └── data_transformer.ipynb # Transforming logic
├── logs/
│   └── pipeline.log               # Unified log file (cleared every run)
├── insuraflow_dag/
│   ├── assets.py                  # Dagster assets (cleaning, transformation)
│   ├── __init__.py
│   └── start_dagster.sh           # 🚀 Shell script to auto-start Dagster + cleanup
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🔄 Dagster-Powered Execution

Each pipeline step is defined as a **Dagster asset** that:

- Executes the corresponding notebook via Papermill
- Passes dynamic paths from `config.yaml`
- Validates output
- Deletes temporary files automatically

```python
@asset
def run_cleaning_notebook() -> Output[str]:
    ...
    pm.execute_notebook(input_path, temp_path, parameters={...})
    ...
```

---

## 🧼 Cleaning Logic

- Standardizes:
  - `gender`, `email_address`, `smoker`, `renewal_flag`
- Formats:
  - `contact_number` → US format: `+1 (555) 123-4567`
  - Dates using `to_date`
- Nullifies:
  - `claim_status` if `claim_id` is missing or invalid
- Logs:
  - Every step is logged using `[CLEANING]` prefix

---

## 🔁 Transformation Logic

- Categorizes policies into **Risk Levels**:
  - Based on `claim_amount`
- Combines:
  - `address + zip_code` into `full_address`
- Drops:
  - Columns like `contact_number` post-cleaning
- Logs with `[TRANSFORMATION]` prefix


---

## 🚀 Usage

```bash

sh insuraflow_dag/start_dagster.sh
```

Then navigate to `http://localhost:3000` and **materialize the assets**!

---

## 📘 Tech Stack

- **Apache Spark (PySpark)**
- **Dagster**
- **Papermill**
- **YAML for config**
- **Pandas (for export)**
- **VSCode + GitHub**

---

## 📈 Pipeline Status

- ✅ Cleaning notebook ✅
- ✅ Transformation notebook ✅
- ✅ Dynamic config via YAML ✅
- ✅ GitHub integration ✅
- ✅ Dagster orchestration ✅
- ✅ PostgreSQL Ingestion (Supabase) ✅
- ✅ dbt transformations ✅
- ⏳ Visualization (Superset / Metabase)


---

## 👤 Author

**Sree Madhuchandra Gamidi**  
📌 GitHub: [@Madhugamidi14](https://github.com/Madhugamidi14)  
🔗 LinkedIn: [linkedin.com/in/madhu-gamidi-31976918b](https://www.linkedin.com/in/madhu-gamidi-31976918b)

---

## ⭐️ Star This Repo

If you like this project, star ⭐️ it on GitHub!

---

## 🧠 Tip

> Run `git status` regularly and check `.gitignore` to avoid pushing large files like `input/`, `output/`, or `logs/`.