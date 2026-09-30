# ComicCraft - AI Comic Story Creator

This implementation follows the uploaded project document: FastAPI + Jinja2 frontend, Gemini Flash for a 5-panel outline, Gemini Pro for narration/dialogue, Stable Diffusion for images, and FPDF for PDF export.

## 1. Create environment

```bash
python -m venv comiccraft-env
```

Windows:
```bash
comiccraft-env\Scripts\activate
```

macOS/Linux:
```bash
source comiccraft-env/bin/activate
```

## 2. Install

```bash
pip install -r requirements.txt
```

## 3. Configure API keys

Copy `.env.example` to `.env` and add:

```text
GEMINI_API_KEY=your_key
HF_API_KEY=your_key
```

## 4. Run

```bash
uvicorn app.main:app --reload
```

Open:

http://127.0.0.1:8000

API docs:

http://127.0.0.1:8000/docs

## Main routes

- `/` - input form
- `/generate` - form-based comic generation
- `/generate-comic/json` - JSON API
- `/test-image` - image generation test
- `/export-success` - export success page
