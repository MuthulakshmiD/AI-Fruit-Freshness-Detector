from flask import Flask, render_template, request
from PIL import Image
import torch
import numpy as np
import joblib
import json
from pathlib import Path

from huggingface_hub import hf_hub_download
from transformers import AutoImageProcessor, ViTModel


app = Flask(__name__)

REPO_ID = "Meeteshn/vit_fruit_ripeness_classifier"
NESTED_FOLDER = "vit_fruit_ripeness_updated"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print("Loading AI model...")
print("Device:", DEVICE)


def download_file(filename):
    try:
        return hf_hub_download(
            repo_id=REPO_ID,
            filename=f"{NESTED_FOLDER}/{filename}"
        )
    except Exception:
        return hf_hub_download(
            repo_id=REPO_ID,
            filename=filename
        )


# Load image processor
try:
    processor = AutoImageProcessor.from_pretrained(
        REPO_ID,
        subfolder=f"{NESTED_FOLDER}/processor"
    )
except Exception:
    processor = AutoImageProcessor.from_pretrained(
        REPO_ID,
        use_fast=True
    )


# Load ViT backbone
try:
    backbone = ViTModel.from_pretrained(
        REPO_ID,
        subfolder=f"{NESTED_FOLDER}/vit_backbone"
    )
except Exception:
    backbone = ViTModel.from_pretrained(
        "google/vit-base-patch16-224"
    )

backbone.to(DEVICE)
backbone.eval()


# Download classifier files
scaler_path = download_file("scaler.joblib")
classifier_path = download_file("logistic_model.joblib")
metadata_path = download_file("metadata.json")

scaler = joblib.load(scaler_path)
classifier = joblib.load(classifier_path)

with open(metadata_path, "r", encoding="utf-8") as f:
    metadata = json.load(f)

classes = metadata["classes"]

print("AI model loaded successfully!")
print("Classes:", classes)


def predict_image(image):
    image = image.convert("RGB")

    inputs = processor(
        images=image,
        return_tensors="pt"
    )

    pixel_values = inputs["pixel_values"].to(DEVICE)

    with torch.no_grad():
        output = backbone(
            pixel_values=pixel_values,
            return_dict=True
        )

        pooled = getattr(output, "pooler_output", None)

        if pooled is None:
            pooled = output.last_hidden_state[:, 0, :]

        features = pooled.cpu().numpy()

    features_scaled = scaler.transform(features)

    probabilities = classifier.predict_proba(
        features_scaled
    )[0]

    index = int(np.argmax(probabilities))

    label = classes[index]
    confidence = float(probabilities[index]) * 100

    return label, confidence


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    error = None

    if request.method == "POST":

        if "image" not in request.files:
            error = "Please select an image."

        else:
            file = request.files["image"]

            if file.filename == "":
                error = "Please select an image."

            else:
                try:
                    image = Image.open(file)

                    prediction, confidence = predict_image(image)

                except Exception as e:
                    error = str(e)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)