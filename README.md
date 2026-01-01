# 🎨 Art Recommendation System (End-to-End)

An **end-to-end Art Recommendation System** built using **Deep Learning (ResNet50)** and **K-Nearest Neighbors (KNN)**. The system analyzes an uploaded artwork image, extracts deep visual features, and recommends visually similar artworks — all through a **Flask-based web application**.

This project is **API-free**, fully local, and production-ready for deployment platforms like **Railway** or **Render**.

---

## 🚀 Project Overview

* Trained on **~85,000 artwork images**
* Uses **ResNet50 (ImageNet pretrained)** for feature extraction
* Converts images into **high-dimensional embeddings**
* Applies **KNN similarity search** to recommend artworks
* Fully integrated **Flask frontend + backend**
* Clean UI with HTML & CSS

---

## 🧠 How It Works (Pipeline)

```
Input Image
     ↓
ResNet50 (Feature Extraction)
     ↓
Image Embedding (Vector)
     ↓
KNN Similarity Search
     ↓
Top-5 Similar Art Recommendations
```

---

## 🏗️ Model Architecture

* **Base Model:** ResNet50
* **Weights:** ImageNet
* **Top Layer:** Removed (`include_top=False`)
* **Pooling:** GlobalMaxPooling2D
* **Output:** Normalized feature vector

The extracted embeddings are stored in:

* `embedding.pkl` → feature vectors
* `file.pkl` → corresponding image paths

---

## 🔍 Recommendation Strategy

* Uses **Euclidean distance** via `sklearn.neighbors.NearestNeighbors`
* Finds visually closest artworks
* Returns **Top-5 recommendations**

---

## 📁 Project Structure

```
art-recommendation-system/
│
├── app.py                  # Flask application
├── recommend.py            # Recommendation logic
├── requirements.txt        # Dependencies
├── model/
│   ├── embedding.pkl       # Image embeddings
│   └── file.pkl            # Image file paths
├── static/
│   ├── uploads/            # Uploaded images
│   ├── results/            # Recommended images
│   └── style/              # CSS files
├── templates/
│   ├── start.html
│   └── index.html
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/art-recommendation-system.git
cd art-recommendation-system
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application Locally

```bash
python app.py
```

Now open your browser and go to:

```
http://127.0.0.1:8080
```

---

## 🖼️ How to Use the App

1. Open the homepage
2. Navigate to the **Recommendation Page**
3. Upload an artwork image
4. Click **Predict / Recommend**
5. View **Top-5 visually similar artworks** instantly

---

## 🌐 Deployment Ready

* Railway compatible (`PORT` auto-detection)
* No external APIs required
* Lightweight and fast inference

---

## ✅ Key Features

* ✔ End-to-end Deep Learning project
* ✔ No API / No Cloud dependency
* ✔ Large-scale dataset (8k images)
* ✔ Real-time image similarity search
* ✔ Clean Flask architecture


---

## 📌 Use Cases

* Art galleries & museums
* Image similarity search engines
* Creative inspiration tools


---

## 📜 License

This project is for **educational and portfolio purposes**.

---

## ⭐ Final Note

This is a **best-in-class Art Recommendation System** demonstrating:

* Deep Learning
* Machine Learning
* Computer Vision
* Feature Engineering
* Similarity Search



