# Laptop Price Prediction

A Streamlit app for ML-powered laptop price prediction with a cyberpunk/tech-noir UI.

## Project Structure

```
laptop_pricer/
├── app.py
├── model.pkl
├── requirements.txt
└── pages/
    ├── functions.py
    ├── __init__.py
    ├── overview.py
    ├── technicals.py
    └── predictor.py
```

## Setup

```bash
pip install -r requirements.txt
```

## Add your model

The model must accept a `pd.DataFrame` with these columns:
| Column | Type | Example |
|---|---|---|
| `in_stock` | bool | `True` |
| `brand` | str | `"Apple"` |
| `model` | str | `"Pro"` |
| `ram_gb` | int | `32` |
| `ram_type` | str | `"DDR5"` |
| `storage_gb` | float | `2000.0` |
| `storage_type` | str | `"SSD"` |
| `display_size_inch` | float | `14.0` |
| `display_type` | str | `"OLED"` |
| `display_resolution` | str | `"3820x1200"` |
| `battery_wh` | float | `60.0` |
| `weight_kg` | float | `1.39` |
| `os_version` | str | `"Windows 11"` |
| `os_benefits` | list[str] | `["Microsoft 365"]` |
| `gpu_model` | str | `"RTX 5070"` |
| `gpu_vram` | str | `"8GB"` |
| `cpu_name` | str | `"Intel Core i9-13620H"` |
| `warranty_years` | int | `3` |
| `cpu_brand` | str | `"Intel"` |
| `cpu_tier` | str | `"Core i9"` |
| `cpu_gen` | int | `13` |

## Run

```bash
streamlit run app.py
```
