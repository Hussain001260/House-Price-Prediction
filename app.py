from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("house_price_model.pkl", "rb"))

# Get model feature names
model_features = model.feature_names_in_

# Extract locations from model columns
locations = sorted([
    col.replace("location_", "")
    for col in model_features
    if col.startswith("location_")
])

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        total_sqft = float(request.form["total_sqft"])
        bath = float(request.form["bath"])
        balcony = float(request.form["balcony"])
        bhk = int(request.form["bhk"])
        location = request.form["location"]

        # Create input dataframe
        input_df = pd.DataFrame(
            np.zeros((1, len(model_features))),
            columns=model_features
        )

        input_df.at[0, 'total_sqft'] = total_sqft
        input_df.at[0, 'bath'] = bath
        input_df.at[0, 'balcony'] = balcony
        input_df.at[0, 'bhk'] = bhk

        location_col = f"location_{location}"
        if location_col in input_df.columns:
            input_df.at[0, location_col] = 1
        else:
            input_df.at[0, "location_other"] = 1

        prediction = round(model.predict(input_df)[0], 2)

    return render_template(
        "index.html",
        prediction=prediction,
        locations=locations
    )

if __name__ == "__main__":
    app.run(debug=True)
