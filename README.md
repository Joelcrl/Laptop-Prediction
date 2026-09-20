# Laptop Price Prediction

A machine learning web application built with **Streamlit** to estimate laptop market prices from hardware and product specifications. The project combines web-scraped laptop data, data preprocessing, Optuna hyperparameter tuning, and a stacking ensemble of **XGBoost, LightGBM, and CatBoost** with **RidgeCV** as the meta-learner.

The Streamlit application is the deployment/presentation layer, while the model development and training process is documented in the companion notebooks repository.

## Project Overview

The project is split into two main parts:

- **Model development (`laptop-prediction-notebooks`)**
  - Data collection and cleaning
  - Feature engineering and normalization
  - Preprocessing pipeline
  - Model training and evaluation
  - Optuna hyperparameter tuning
  - Final model export as `model.pkl`

- **Streamlit application (`laptop-prediction-streamlit`)**
  - Interactive laptop specification form
  - Loads the trained `model.pkl`
  - Runs the same preprocessing pipeline stored inside the trained model
  - Displays the estimated laptop price
  - Includes model/pipeline technical documentation and inference-latency benchmarking

## Machine Learning Model

The model used by the Streamlit app is **not trained inside the Streamlit application**. The application loads the serialized pipeline from:

```text
model.pkl
```

This model was trained in the `main_fixed.ipynb` notebook after the experiments and hyperparameter tuning documented in `tuner_fixed.ipynb`.

### Final Model Architecture

The final estimator uses a **stacking ensemble**:

```text
Input Laptop Specifications
          │
          ▼
   Feature Preprocessing
          │
          ▼
 ┌────────┼─────────┐
 │        │         │
 ▼        ▼         ▼
XGBoost  LightGBM  CatBoost
 │        │         │
 └────────┼─────────┘
          ▼
       RidgeCV
     Meta-Learner
          │
          ▼
 Estimated Laptop Price
```

The three base regressors are:

- **XGBoost Regressor**
- **LightGBM Regressor**
- **CatBoost Regressor**

Their predictions are combined by a **RidgeCV** meta-learner through `sklearn.ensemble.StackingRegressor`.

The target variable is transformed with `log1p` during training and converted back with `expm1` during prediction using `TransformedTargetRegressor`.

### Hyperparameter Tuning

The individual base models were tuned using **Optuna** with a **TPE sampler** and 5-fold cross-validation. The tuning objective was based on **MAPE (Mean Absolute Percentage Error)**.

The tuning process is documented in:

```text
tuner_fixed.ipynb
```

The selected model configuration is then assembled into the final stacking pipeline and saved as:

```text
models/model.pkl
```

That trained pipeline is copied to the Streamlit repository as:

```text
model.pkl
```

## Preprocessing Pipeline

The trained pipeline handles preprocessing before the ensemble receives the data.

Key preprocessing steps include:

| Feature group | Processing |
|---|---|
| Brand, model, GPU model, CPU name | Target Encoding |
| RAM type, OS version | One-Hot Encoding |
| Storage type, display type | Ordinal Encoding |
| Display resolution | Converted to pixel-related numerical features |
| GPU VRAM | Custom numerical encoding |
| OS benefits | Multi-hot encoding |
| General numerical features | Median imputation + StandardScaler |
| RAM, storage, display size, battery, weight | KNN imputation + StandardScaler |

This preprocessing is stored together with the estimator inside `model.pkl`, so the Streamlit app can pass raw user inputs directly to the trained pipeline.

## Input Features

The Streamlit predictor accepts the following laptop specifications:

- Brand
- Laptop model
- RAM size
- RAM type
- Storage size
- Storage type
- Display size
- Display type
- Display resolution
- Battery capacity
- Weight
- Operating system
- OS benefits
- GPU model
- GPU VRAM
- Warranty period
- CPU name

`cpu_gen` is derived automatically from the selected CPU name inside the Streamlit application.

## Model Evaluation

The final ensemble was evaluated using 5-fold cross-validation in `main_fixed.ipynb`.

| Metric | Ensemble CV Mean |
|---|---:|
| MAPE | 0.0846 |
| MAE | Rp 1,220,121 |
| RMSE | Rp 2,120,464 |
| RMSLE | 0.1212 |
| R² | 0.9129 |

The reported values are cross-validation averages from the notebook and should be interpreted as model-development evaluation results rather than a guarantee of prediction accuracy for every laptop.

## Streamlit Features

The web application provides:

- **Overview** — project and model overview
- **Price Predictor** — interactive laptop price estimation
- **Technical Deep Dive** — explanation of the ML pipeline
- **Inference Latency Benchmark** — P50/P90/P99 prediction latency measurement

The predictor runs 100 timed inference runs after a warm-up call to calculate latency statistics.

## Project Structure

```text
laptop-prediction-streamlit/
├── app.py
├── model.pkl
├── cpu_names.txt
├── requirements.txt
├── README.md
└── pages/
    ├── functions.py
    ├── overview.py
    ├── predictor.py
    └── technicals.py
```

The model-development repository contains the notebooks and training artifacts:

```text
laptop-prediction-notebooks/
├── main_fixed.ipynb
├── tuner_fixed.ipynb
├── dataset.csv
├── cleaned_dataset.csv
├── dict_replace_os.json
├── models/
│   └── model.pkl
└── scrapper/
    ├── scrapper.py
    ├── agres_all_products.csv
    └── agres_laptops.csv
```

## Installation

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start Streamlit with:

```bash
streamlit run app.py
```

Then open the local URL shown by Streamlit in your browser.

## Notes

- The application uses the pre-trained `model.pkl`; it does not retrain the model when the app starts.
- The model was developed using laptop product data collected from the Agres marketplace.
- Predictions are estimates based on the training data and model learned from it. They should not be interpreted as official market prices.
- If the model is retrained, the exported pipeline should replace `model.pkl` in the Streamlit repository.

## Related Repository

The notebooks repository contains the complete model-development workflow, including preprocessing, experiments, Optuna tuning, evaluation, and model export.

---

**Tech Stack:** Python · Pandas · Scikit-learn · XGBoost · LightGBM · CatBoost · Optuna · Streamlit
