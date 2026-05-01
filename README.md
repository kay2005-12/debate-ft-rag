## Football Debate RAG Pipeline

A complete end-to-end pipeline that converts YouTube football debate videos into a structured, RAG-ready dataset.

The project processes long-form debate content (e.g., Messi vs Ronaldo discussions) into meaningful text chunks and enables retrieval-based question answering using embeddings and LLM inference.

---

🚀 Features

- 🎥 Download YouTube videos
- 🔊 Convert videos to audio using FFmpeg
- 🧠 Transcribe audio using Whisper / Faster-Whisper (offline)
- 🌐 Translate non-English speech to English
- ✂️ Merge small segments into large context-aware chunks
- 📦 Export structured JSON dataset
- 🔍 Generate embeddings using Nomic Embed Text
- ⚡ Fast inference using Cerebras API

---

🛠️ Tech Stack

- Python
- Faster-Whisper (Speech-to-Text)
- yt-dlp (Video Download)
- FFmpeg (Audio Processing)
- Nomic Embed Text (Embeddings)
- Cerebras API (LLM Inference)

---

📂 Project Workflow

YouTube Videos
      ↓
Download (yt-dlp)
      ↓
Convert to Audio (FFmpeg)
      ↓
Transcription (Faster-Whisper)
      ↓
Chunking (Merge Segments)
      ↓
JSON Dataset
      ↓
Embeddings (Nomic)
      ↓
Vector Store
      ↓
Cerebras LLM
      ↓
Answer Generation (RAG)

---

⚙️ Installation

pip install faster-whisper yt-dlp

Install FFmpeg:

sudo apt install ffmpeg

(Windows users: download FFmpeg and add it to PATH)

---

▶️ Usage

1. Download Videos

yt-dlp PLAYLIST_URL -o "videos/%(title)s.%(ext)s"

---

2. Convert Video → Audio

ffmpeg -i input.mp4 -vn -acodec libmp3lame output.mp3

---

3. Transcribe Audio

from faster_whisper import WhisperModel

model = WhisperModel("medium", device="cuda")

segments, info = model.transcribe("audio/file.mp3")

---

4. Chunking Strategy

Segments are merged into larger chunks for better context:

if len(chunk_text) > 1000:

Each chunk contains:

{
  "start": 0.0,
  "end": 35.2,
  "text": "Combined debate context..."
}

---

📊 Output Format

{
  "chunks": [
    {
      "number": 1,
      "title": "Messi vs Ronaldo Debate",
      "start": 0.0,
      "end": 35.2,
      "text": "Messi is the greatest player..."
    }
  ],
  "text": "Full transcript..."
}

---

🧠 Embeddings & LLM

- 🔍 Embeddings: Nomic Embed Text
- ⚡ LLM Inference: Cerebras API

---

🔗 RAG Pipeline

Chunks
   ↓
Embeddings (Nomic)
   ↓
Vector Database
   ↓
Query
   ↓
Retrieved Context
   ↓
Cerebras LLM
   ↓
Answer

---

⚡ Performance

Model| Speed| Accuracy
small| Fast| Medium
medium| Balanced| Good
large| Slow| Best

Recommended: medium (GPU, 4GB VRAM supported)

---

🧠 Use Cases

- Football debate chatbot
- RAG-based QA system
- NLP dataset creation
- Content summarization

---

📌 Key Highlights

- Fully offline transcription (no API key required)
- Handles long-form debate content
- Optimized chunking for better retrieval
- End-to-end RAG pipeline implementation

---

🔮 Future Improvements

- Speaker diarization
- Semantic chunking
- FAISS / vector DB optimization
- Web UI for querying

---
