
# 🛡️ InsuraFlow

![PySpark](https://img.shields.io/badge/PySpark-Data%20Engineering-orange?style=flat-square&logo=apache-spark)
![Apache Spark](https://img.shields.io/badge/Spark-Optimized-green?style=flat-square&logo=apache-spark)
![JSON](https://img.shields.io/badge/Data-JSON-blue?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/Madhugamidi14/InsuraFlow)

**InsuraFlow** is a PySpark-based industry-grade data engineering pipeline tailored for cleaning, transforming, and preparing fictitious insurance data for downstream analytics and reporting.

---

## 🚀 Overview

Insurance datasets often contain inconsistencies, formatting issues, and require enrichment for meaningful insights. **InsuraFlow** handles:

- 🧹 **Data Cleaning**: Fixes formatting issues, handles missing values, validates and normalizes fields.
- 🔄 **Data Transformation**: Enriches and reshapes the cleaned data for analytical use.
- 🔗 **Pipeline Orchestration**: Modular execution using Jupyter Notebooks and Papermill.
- 📝 **Robust Logging**: Logs every operation using centralized logging with contextual labels (`[CLEANING]`, `[TRANSFORMATION]`).

---

## 📂 Project Structure

```bash
InsuraFlow/
├── input/                       # Raw input files (JSON)
├── output/                      # Cleaned + Transformed outputs
├── notebooks/
│   ├── cleaning/                # Data cleaning notebook
│   │   └── data_cleaning.ipynb
│   └── transforming/            # Data transformation notebook
│       └── data_transformer.ipynb
├── logs/
│   └── pipeline.log             # Truncated and reused every run
├── config/
│   └── config.yaml              # Centralized config for file paths
├── main.py                      # Orchestration script
└── README.md                    # You're here!
```

---

## 🧼 Cleaning Highlights

- Standardizes gender, email, boolean fields
- Validates and formats date columns
- Normalizes `contact_number` to **US format** like `+1 (123) 456-7890`
- Removes `xEXT` from phone numbers (e.g. `x12345`)
- Nullifies `claim_status` if `claim_id` is missing or invalid
- Robust logging after every step

---

## 🔁 Transformations

- Categorizes policies into **Risk Levels** (`High`, `Medium`, `Low`) based on claim amounts
- Generates `full_address` using `address + zip_code`
- Drops unnecessary fields post-cleaning (e.g., `contact_number`)

---

## 📘 Configurable Parameters

All notebook paths and logs are driven by `config/config.yaml`:

```yaml
log_file: logs/pipeline.log

notebooks:
  cleaning:
    input: notebooks/cleaning/data_cleaning.ipynb
    output_template: notebooks/cleaning/data_cleaning_output_{timestamp}.ipynb
  transforming:
    input: notebooks/transforming/data_transformer.ipynb
    output_template: notebooks/transforming/data_transformer_output_{timestamp}.ipynb
```

---

## 🧪 Tech Stack

- **PySpark**
- **Pandas**
- **Jupyter + Papermill**
- **YAML-based configuration**
- **Logging & Exception Handling**

---

## 👤 Author

**Sree Madhuchandra Gamidi**  
📌 GitHub: [@Madhugamidi14](https://github.com/Madhugamidi14)  
🔗 LinkedIn: [linkedin.com/in/madhu-gamidi-31976918b](https://www.linkedin.com/in/madhu-gamidi-31976918b)

---

## 📈 What's Next?

- ✅ Cleaning + Transformation complete  
- 🔜 Ingestion to PostgreSQL using Parquet  
- 🔜 DBT transformations and modeling  
- 🔜 Visualization using Superset or Metabase  
- 🔜 Airflow-based orchestration  
- 🔜 CI/CD + Docker packaging


---

## ⭐️ Star This Repo

If you find **InsuraFlow** helpful, show some ❤️ by starring the repo!
