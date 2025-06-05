# 🧠 EndToEnd_DSproject - Wine Quality Prediction

An end-to-end Machine Learning project for predicting wine quality based on chemical attributes.  
This project follows a modular, production-grade pipeline using MLOps principles, with MLflow for experiment tracking and Flask for deployment.

---

## 🔁 Workflow - ML Pipeline

1. **Data Ingestion**  
   - Downloads dataset and stores it in artifacts.
2. **Data Validation**  
   - Schema check, column/type validation.
3. **Data Transformation**  
   - Preprocessing, feature engineering (scaling, splitting).
4. **Model Trainer**  
   - Trains model using ElasticNet.
   - Tracks experiments using MLflow.
   - Integrates with DagsHub.
5. **Model Evaluation**  
   - Calculates metrics and logs them to MLflow.

---

## ⚙️ Configuration-Driven Workflow

This project is driven by 3 configuration files:

- `config.yaml` — controls pipeline steps, paths, model output
- `params.yaml` — holds hyperparameters (e.g., ElasticNet `alpha`, `l1_ratio`)
- `schema.yaml` — defines expected data types and target column

---

## 🧪 How to Run the Pipeline

### 1. Update Configurations
Before running, update the following:
- `config.yaml`
- `schema.yaml`
- `params.yaml`

### 2. Update Entity and Config Classes
- `src/entity/`: defines structured config using `@dataclass`
- `src/config/configuration.py`: manages parsing logic for YAML files

### 3. Build Each Pipeline Component
- `src/components/`: core logic for ingestion, transformation, training, etc.
- Each component follows clean function or class-based logic.

### 4. Define Pipeline Flows
- `src/pipeline/`: wraps components into step-wise flows (e.g., `data_ingestion_pipeline.py`)

### 5. Entry Point
- `main.py`: orchestrates the pipeline step-by-step using logs and configs

---

## 🚀 How to Use the Flask App (Frontend)

```bash
# Run the Flask app
python app.py


