from fastapi import FastAPI
from schemas import TrainRequest

app = FastAPI()


@app.post("/train")
def start_training(req: TrainRequest):
    return {
        "message": f"Received request to train {req.model_name} for {req.epochs} epochs at {req.learning_rate} LR. (Training logic is in notebooks.)"
    }


@app.get("/")
def read_root():
    return {
        "message": "MNIST API running. Use /train endpoint or run notebooks for model training and tuning."
    }
