from pydantic import BaseModel


class TrainRequest(BaseModel):
    model_name: str
    epochs: int = 5
    learning_rate: float = 0.001
