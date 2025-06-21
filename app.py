# from flask import Flask, render_template, request
# import os
# import numpy as np
# import pandas as pd 
# from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

# app = Flask(__name__)

# @app.route('/', method=['GET'])  ## route to display the home page
# def homepage():
#     return render_template("index.html")

from flask import Flask, render_template, request
import pandas as pd
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

# Wine feature columns (excluding target)
columns = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol"
]

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html", columns=columns, prediction=None)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract values from form and convert to float
        input_data = [float(request.form[col]) for col in columns]
        input_df = pd.DataFrame([input_data], columns=columns)

        # Predict using your pipeline
        pipeline = PredictionPipeline()
        prediction = pipeline.predict(input_df)[0]

        return render_template("index.html", columns=columns, prediction=round(prediction, 2))

    except Exception as e:
        return render_template("index.html", columns=columns, prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True, port=8001)
