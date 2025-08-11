# 🖼️ YOLO-Django-Project

## 🎯 Goal of the Project

Upload an image, run **YOLOv8** object detection, and get:

- The image with **bounding boxes** and **labels**
- A **list of detected objects** with confidence scores

---

## 💡 How It Works — Step by Step

1. Open the web page and upload an image.
2. Click **Detect**.
3. Django saves the uploaded image.
4. YOLOv8 runs object detection on the image.
5. Bounding boxes and labels are drawn on the image.
6. The results page shows:
    - 🖼️ The **processed image**
    - 📋 A **list of detected objects** with confidence values

---

## 📂 Project Structure (Key Files)

| File / Folder | Description |
| --- | --- |
| `backend/` | Main Django project (settings, urls, apps) |
| `media/` | Stores uploaded and processed images |
| `yolov8n.pt` | YOLOv8 model weights (Nano version) |
| `templates/upload.html` | HTML upload form & results display |
| `views.py` | Handles uploads, runs detection, sends data to template |
| `utils.py` | YOLOv8 detection logic and image processing |
| `.gitignore` | Files/folders excluded from version control |
| `requirements.txt` | Python dependencies list |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <https://github.com/IqramZargar/WEB-APPLICATION-For-Object-Detection.git>
cd WEB-APPLICATION-For-Object-Detection
2️⃣ Create and activate a virtual environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Download YOLOv8 weights
If yolov8n.pt is not included:

bash
Copy
Edit
wget <https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt>
5️⃣ Apply migrations
bash
Copy
Edit
python manage.py migrate
6️⃣ Run the development server
bash
Copy
Edit
python manage.py runserver
🖥️ Usage
Visit <http://127.0.0.1:8000/> in your browser.

Upload an image.

View detection results:

Image with bounding boxes

List of detected objects and confidence scores

📜 Example Output
makefile
Copy
Edit
Person: 0.89
Car: 0.78
Dog: 0.91
And the processed image will show green boxes and labels.

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
```

[Yolo-Django-Project](https://www.notion.so/Yolo-Django-Project-2485edf1c10680898ffae254c7d4fdcd?pvs=21)