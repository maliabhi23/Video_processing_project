# Video_processing_project

```markdown
# 🎥 FastAPI Video Frame Similarity Search

This project is built as part of an internship assignment. It allows uploading videos, extracting frames, computing feature vectors using color histograms, and performing similarity search using Qdrant vector database.

---

## 🚀 Features

- ✅ Upload video files (`.mp4`)
- ✅ Extract frames at regular intervals (1 frame/sec)
- ✅ Compute feature vectors using color histograms (RGB, 8x8x8 bins = 512 dims)
- ✅ Store vectors in Qdrant
- ✅ Search for similar frames by uploading or passing a feature vector
- ✅ Return matching frames and metadata

---

## 🗂️ Project Structure

```
```
video-similarity-search/
├── app/
│   ├── main.py               # FastAPI entrypoint
│   ├── feature\_extraction.py # Feature vector generation logic
│   ├── vector\_db.py          # Qdrant integration (init, store, search)
│   ├── utils.py              # Frame extraction, file saving, etc.
├── frames/                   # Extracted frames from uploaded videos
├── .env                      # Environment variables (Qdrant host, port, etc.)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

````

---

## ⚙️ Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Qdrant client
- OpenCV

Install dependencies:

```bash
pip install -r requirements.txt
````

---

## 🧪 Running the App



### 2️⃣ Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

Open docs: [http://localhost:8000](http://localhost:8000)

---

## 📩 API Endpoints

### `POST /upload_video`

Upload a video (MP4), extract frames, compute vectors, and store in Qdrant.

**Body**: `multipart/form-data`
**Field**: `file`
```
` http://localhost:8000/upload_video'

```


### `POST /search_similar`

Search for similar frames using a feature vector.

```json
{
  "vector": [/* 512 float values */],
  "top_k": 5
}
```

Returns matched frame image names and similarity scores.

---

## 🧠 Feature Vector Details

* Color histogram over RGB with 8 bins per channel
* Histogram shape: (8, 8, 8) = 512
* Normalized and flattened to 1D list

---

## 📁 Example Frame Output

After uploading a video:

```bash
frames/
├── video123_frame_0.jpg
├── video123_frame_1.jpg
└── ...
```

---

## 📸 Example Search Vector (length = 512)

```json
{
  "vector": [0.0, 0.05, ..., 0.01],
  "top_k": 5
}
```

---

## 📝 Notes

* Images are saved in the `frames/` folder
* Vectors are stored in Qdrant using the frame image name as ID
* Supports querying by raw vector (future enhancement: upload image to search)

---

## 📌 Future Enhancements

* Upload image to search instead of raw vector
* Use deep features (e.g., MobileNet, CLIP) instead of color histograms
* Add pagination or similarity thresholding
