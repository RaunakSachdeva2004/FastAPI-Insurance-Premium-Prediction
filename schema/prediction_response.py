from pydantic import BaseModel, Field
from typing import Dict

class PredictionDetail(BaseModel):
    predicted_category: str = Field(..., description="Predicted insurance premium category (High, Medium, Low)")
    confidence: float = Field(..., description="Model confidence score for the predicted category")
    class_probabilities: Dict[str, float] = Field(..., description="Probability distribution across all insurance premium categories")

class PredictionResponse(BaseModel):
    response: PredictionDetail
