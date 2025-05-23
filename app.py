
# dashboard.render.com

from flask import flask, request, render_template

import pandas as pd
import numpy as np

from src.pipeline import PredictPipeline
from src.pipeline import CustomData
from src.logger import logging

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET","POST"])
def predict_datapoint():
    if(request.method=="GET"):
        return render_template("home.html")

    else:
        data = CustomData(

            gender  =  request.form.get("gender"),
            race_ethnicity =  request.form.get("ethnicity"),
            parental_level_of_education =  request.form.get("parental_level_of_education"),
            lunch =  request.form.get("lunch"),
            test_preparation_course =  request.form.get("test_preparation_course"),
            reading_score =  float(request.form.get("reading_score")),
            writing_score =  float(request.form.get("writing_score"))
        
        )
        
        pred_df = data.get_data_as_data_frame(data)
        print(pred_df)
        logging.info("Before Prediction got the data", str(pred_df))

        predict_pipeline = PredictPipeline()

        results = predict_pipeline.predict(pred_df)
        return render_template("home.html", results = results[0])


if (__name__ == "__main__"):
    app.run(host="0.0.0.0", debug=True  )

