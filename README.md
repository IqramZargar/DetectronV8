🖼️ YOLO-Django-Project
🎯 Goal of the Project

Upload an image, run YOLOv8 object detection, and get:

🖼️ The image with bounding boxes and labels

📋 A list of detected objects with confidence scores

💡 How It Works — Step by Step

Open the web page and upload an image.

Click Detect.

Django saves the uploaded image.

YOLOv8 runs object detection on the image.

Bounding boxes and labels are drawn on the image.

The results page shows:

🖼️ The processed image

📋 A list of detected objects with confidence values

📂 Project Structure (Key Files)
File / Folder	Description
backend/	Main Django project (settings, urls, apps)
media/	Stores uploaded and processed images
yolov8n.pt	YOLOv8 model weights (Nano version)
templates/	HTML templates (home, about, detection pages)
views.py	Handles uploads, runs detection, sends data to templates
utils.py	YOLOv8 detection logic and image processing
.gitignore	Excludes venv/, __pycache__/, etc. from version control
requirements.txt	Python dependencies (cross-platform)
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/IqramZargar/WEB-APPLICATION-For-Object-Detection.git
cd WEB-APPLICATION-For-Object-Detection

2️⃣ Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # On Linux/macOS
venv\Scripts\activate      # On Windows

3️⃣ Install dependencies

⚠️ Important: YOLOv8 requires PyTorch. Install it separately depending on your OS.

🔥 Install PyTorch

Linux/macOS (CUDA 11.8 for GPU):

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118


Windows (CPU only):

pip install torch torchvision torchaudio

📦 Install other dependencies
pip install -r requirements.txt

4️⃣ Download YOLOv8 weights

If yolov8n.pt is not included in the repo:

wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt

5️⃣ Apply migrations
python manage.py migrate

6️⃣ Run the development server
python manage.py runserver

🖥️ Usage

Visit http://127.0.0.1:8000/ in your browser.

Upload an image.

View detection results:

🖼️ Image with bounding boxes

📋 List of detected objects & confidence scores

📜 Example Output

Objects Detected:

Person: 0.89
Car: 0.78
Dog: 0.91


And the processed image will show green bounding boxes with labels.

🛠 Tech Stack

Backend: Django

ML Model: YOLOv8 (Ultralytics)

Language: Python

Frontend: HTML + Django Templates

Image Processing: OpenCV

🤝 Contributing

Pull requests are welcome!
If you find bugs or have suggestions, open an issue.

📄 License

This project is licensed under the MIT License.
