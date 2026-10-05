# 🏥 FastAPI Insurance Premium Prediction

An end-to-end Machine Learning API built with **FastAPI**, **Pydantic**, and **Scikit-Learn** that predicts insurance premium categories (`High`, `Medium`, `Low`) along with model confidence and class probabilities based on user demographics, health factors, and economic indicators.

---

## 📌 Features

- **Automated Feature Engineering**: Uses Pydantic `@computed_field` to calculate:
  - **BMI**: Derived dynamically from height and weight ($\text{weight} / \text{height}^2$).
  - **Lifestyle Risk**: Evaluated using smoking status and BMI (`high`, `medium`, `low`).
  - **Age Group**: Categorized into `young`, `adult`, `middle_aged`, and `senior`.
  - **City Tier**: Classified across Tier 1, Tier 2, and Tier 3 Indian cities.
- **Robust Pipeline**: End-to-end `scikit-learn` Pipeline featuring `ColumnTransformer` (One-Hot Encoding for categorical features and passthrough for numerical) coupled with a `RandomForestClassifier`.
- **Fast & Interactive**: Instant predictions with confidence metrics and automatic interactive API documentation via Swagger UI.

---

## 📁 Repository Structure

```plaintext
FastAPI-Insurance-Premium-Prediction/
├── app.py                  # FastAPI application, Pydantic schemas, and inference endpoint
├── ml-model/
│   └── model.pkl           # Trained Scikit-Learn Pipeline (Preprocessor + Random Forest)
├── requirements.txt        # Pinned dependencies for reproducible deployment
├── .gitignore              # Ignored virtual environments, bytecode, and cache
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.10+** (tested on Python 3.13)
- `git`

### 2. Clone the Repository
```bash
git clone https://github.com/RaunakSachdeva2004/FastAPI-Insurance-Premium-Prediction.git
cd FastAPI-Insurance-Premium-Prediction
```

### 3. Create & Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv myvenv
.\myvenv\Scripts\Activate.ps1
```

**On Linux / macOS:**
```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Server
```bash
uvicorn app:app --reload
```
The API will be live at: `http://127.0.0.1:8000`

Interactive Swagger Documentation: `http://127.0.0.1:8000/docs`  
ReDoc Documentation: `http://127.0.0.1:8000/redoc`

---

## 🔌 API Reference

### Health & Info Endpoints

- **Root**: `GET /`
  - Returns a human-readable welcome message.
  - Response: `{"message": "Insurance Premium Prediction API"}`
- **Health Check**: `GET /health`
  - Returns service status, model loaded state, and API version.
  - Response: `{"status": "OK", "model_loaded": true, "version": "1.0.0"}`

---

### Predict Premium Category

- **Endpoint**: `POST /predict`
- **Content-Type**: `application/json`

#### Request Body Schema

| Field | Type | Description | Valid Values / Constraints |
| :--- | :--- | :--- | :--- |
| `age` | `int` | Age of user in years | `0 < age < 120` |
| `weight` | `float` | Weight in kilograms | `> 0` |
| `height` | `float` | Height in meters | `0 < height < 2.5` |
| `income_lpa` | `float` | Annual salary in Lakhs Per Annum (LPA) | `> 0` |
| `smoker` | `bool` | Smoker status | `true` or `false` |
| `city` | `str` | Residential city | e.g. `"Mumbai"`, `"Lucknow"` |
| `occupation` | `str` | User's profession | `'retired'`, `'freelancer'`, `'student'`, `'government_job'`, `'business_owner'`, `'unemployed'`, `'private_job'` |

#### Example Request Payload

```json
{
  "age": 30,
  "weight": 70.0,
  "height": 1.75,
  "income_lpa": 12.0,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

#### Example Response Payload

```json
{
  "response": {
    "predicted_category": "Low",
    "confidence": 0.74,
    "class_probabilities": {
      "High": 0.01,
      "Low": 0.74,
      "Medium": 0.25
    }
  }
}
```

---

## 🧪 Testing with cURL

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "age": 45,
       "weight": 85.0,
       "height": 1.70,
       "income_lpa": 18.5,
       "smoker": true,
       "city": "Delhi",
       "occupation": "business_owner"
     }'
```

---

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Validation**: [Pydantic v2](https://docs.pydantic.dev/)
- **Machine Learning**: [Scikit-Learn](https://scikit-learn.org/) (RandomForestClassifier, ColumnTransformer)
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)