from flask import Flask, request, render_template, send_from_directory
import os
from recommend import recommend
import shutil

app = Flask(__name__)

# === Paths ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static/uploads")
RESULT_FOLDER = os.path.join(BASE_DIR, "static/results")
STYLE_FOLDER = os.path.join(BASE_DIR, "style")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# === Routes ===
@app.route("/")
def home():
    return render_template("start.html")

@app.route("/recommend")
def recommend_page():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return "No file uploaded."

    file = request.files["image"]
    if not file.filename:
        return "No file selected."

    filename = file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Run recommendation model
    results = recommend(filepath)

    # Clear old results safely
    if os.path.exists(RESULT_FOLDER):
        shutil.rmtree(RESULT_FOLDER)
    os.makedirs(RESULT_FOLDER)

    output_images = []
    for img in results:
        new_path = os.path.join(RESULT_FOLDER, os.path.basename(img))
        shutil.copy(img, new_path)
        output_images.append(os.path.basename(img))

    return render_template(
        "index.html",
        uploaded=filename,
        results=output_images
    )

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route("/results/<filename>")
def result_file(filename):
    return send_from_directory(RESULT_FOLDER, filename)

@app.route("/style/<filename>")
def style(filename):
    return send_from_directory(STYLE_FOLDER, filename)

# === Railway-compatible run ===
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
