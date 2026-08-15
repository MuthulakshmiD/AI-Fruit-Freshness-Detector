# AI-Fruit-Freshness-Detector# 🍎 AI Fruit Freshness Detector

An AI-powered web application that uses a Vision Transformer (ViT) and computer vision to classify the ripeness condition of fruit images.

The system allows users to upload an image through a Flask web interface and predicts whether the fruit is **Fresh, Unripe, or Rotten**, along with a confidence score.

## 🚀 Features

* Upload fruit images through a web interface
* AI-based image classification
* Vision Transformer (ViT) feature extraction
* Fresh, Unripe, and Rotten classification
* Confidence score for predictions
* Flask-based web application
* Simple and responsive user interface
* Supports Apple, Banana, and Orange images
* Runs locally on a computer

## 🧠 How It Works

```text
User
  ↓
Upload Fruit Image
  ↓
Flask Web Application
  ↓
Image Preprocessing
  ↓
Vision Transformer (ViT)
  ↓
Feature Extraction
  ↓
Classifier
  ↓
Prediction + Confidence
  ↓
Display Result
```

## 🛠️ Technologies Used

* Python
* Flask
* PyTorch
* Torchvision
* Transformers
* Vision Transformer (ViT)
* Hugging Face
* PIL
* NumPy
* Joblib
* HTML
* CSS

## 📂 Project Structure

```text
fruit_detector/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd fruit_detector
```

### 2. Install dependencies

```bash
python -m pip install flask torch torchvision transformers scikit-learn pillow joblib numpy huggingface_hub
```

### 3. Run the application

```bash
python app.py
```

### 4. Open the application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 📸 Usage

1. Open the web application.
2. Click **Choose Image**.
3. Select an image of an apple, banana, or orange.
4. Click **Analyze Image**.
5. The application sends the image to the AI model.
6. The model predicts the ripeness condition.
7. The result and confidence score are displayed.

Example:

```text
Prediction: Fresh
Confidence: 94.20%
```

## 🤖 AI Model

This project uses a Vision Transformer-based model for image feature extraction and classification.

The model processes the uploaded image and extracts visual features. A classifier then uses those features to determine the predicted ripeness category.

The model used for this project is available on Hugging Face:

**Meeteshn/vit_fruit_ripeness_classifier**

The model supports:

* Fresh
* Unripe
* Rotten

for supported fruit categories including:

* Apple
* Banana
* Orange

## 🔬 Image Processing Pipeline

The uploaded image follows this pipeline:

```text
Input Image
    ↓
RGB Conversion
    ↓
Image Preprocessing
    ↓
Resize / Model Transform
    ↓
Tensor Conversion
    ↓
Vision Transformer
    ↓
Feature Extraction
    ↓
Feature Scaling
    ↓
Classifier
    ↓
Class Probability
    ↓
Final Prediction
```

## 📊 Output

The application provides two main outputs:

### Prediction

The predicted ripeness condition:

```text
Fresh
```

or:

```text
Unripe
```

or:

```text
Rotten
```

### Confidence

The model's confidence in its classification:

```text
Confidence: 94.20%
```

The confidence score represents the model's classification confidence and should not be interpreted as a guarantee of food safety.

## 🎯 Project Objectives

* Automate visual fruit-ripeness classification
* Demonstrate AI-based computer vision
* Use a Vision Transformer for image analysis
* Create a simple web-based AI application
* Provide quick visual classification results
* Demonstrate deployment of an AI model through Flask

## ✅ Advantages

* Simple user interface
* Fast prediction after model loading
* Automated image classification
* Uses modern transformer-based computer vision
* Can run locally
* Can be extended to additional fruit categories

## ⚠️ Limitations

* Prediction depends on image quality.
* Poor lighting can affect classification.
* Blurry images may produce incorrect results.
* The model may perform poorly on images that differ significantly from its training data.
* The current model supports a limited number of fruit categories.
* Visual classification cannot detect every type of food contamination.
* The system does not guarantee that food is safe to eat.

## 🔮 Future Scope

The project can be improved by adding:

* More fruits and vegetables
* Additional classes such as moldy, bruised, and overripe
* Mobile application support
* Real-time camera detection
* Batch image processing
* Grocery-store quality inspection
* Food-quality monitoring dashboard
* Larger and more diverse training datasets
* Improved model architectures
* Model performance analytics

## 🏪 Possible Applications

This system could be used as an assistive tool in:

* Grocery stores
* Supermarkets
* Restaurants
* Food warehouses
* Household food monitoring
* Agricultural applications
* Food-quality inspection research

## 🔐 Food Safety Disclaimer

This project is an **AI-based visual classification prototype**.

It should not be used as a definitive food-safety inspection system. A fruit or vegetable may contain harmful contamination that cannot be detected visually.

Always follow appropriate food-safety practices and professional guidance.

## 📚 Learning Outcomes

Through this project, the following concepts are demonstrated:

* Python programming
* Flask web development
* Computer vision
* Deep learning
* Vision Transformers
* Image preprocessing
* Model inference
* Classification
* Confidence scores
* Web-based AI deployment


## 📄 License

This project is intended for educational and demonstration purposes.

Add an appropriate license if you plan to distribute or reuse the project publicly.
