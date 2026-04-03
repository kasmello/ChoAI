# ChoAI

A fine-tuned LLM that generates executable Python/matplotlib visualisation code from natural language queries over K-pop album sales data (Square POS + photo-booth machines).

> Masters project (COMP6002) — revived and productionised.

---

## What it does

1. You type: *"How many BTS albums sold in July, broken down by machine?"*
2. The model outputs valid Python that queries the sales DataFrame and renders a labelled matplotlib chart.

---

## Architecture

```
Local machine                    Google Colab (GPU)              Production (future)
─────────────────                ──────────────────              ───────────────────
square_extract.py                Training_Notebook.ipynb         FastAPI server
  └─ fetches Square POS data       └─ git pull from GitHub         └─ loads adapter
                                   └─ fine-tunes LLM (QLoRA)          from HF Hub
generate_common_file_from_data.py  └─ pushes adapter to HF Hub    └─ vLLM serving
  └─ joins sales + roster + machines
  └─ produces final_file.json    Inference_Notebook.ipynb
     (training data)               └─ loads adapter from HF Hub
                                   └─ runs eval prompts
                                   └─ logs scores to W&B
```

---

## Repo layout

```
ChoAI/
├── new_data.py                  # main dataset generation pipeline
├── classes_and_functions.py     # data transformation helpers
├── code_scrambler.py            # AST rewriter: converts OOP matplotlib → functional
├── generate_common_file_from_data.py  # joins Square + roster + machine data
├── square_extract.py            # Square POS API client
├── roster.py                    # staff roster processing
├── machine_payments.py          # photo-booth machine data processing
├── values.json                  # colour palettes, entity lists, date ranges
├── Training_Notebook.ipynb      # Colab fine-tuning notebook
├── Inference_Notebook.ipynb     # Colab evaluation + scoring notebook
├── font/                        # Manjari font (used in generated charts)
├── Media/                       # brand assets (logo)
├── requirements.txt             # local dev dependencies
└── requirements-train.txt       # Colab/GPU training dependencies (see notes)
```

Not in git (generated or sensitive):
- `ProcessedData/` — joined CSVs produced by the data pipeline
- `Training/final_file.json` — instruction–output pairs for SFT
- `RawData/` — raw Square exports and roster files
- `.env` — Square API credentials

---

## Local setup

```bash
git clone https://github.com/kasmello/ChoAI.git
cd ChoAI
pip install -r requirements.txt
cp .env.example .env   # fill in SQUARE_ACCESS_TOKEN and SQUARE_LOCATION_ID
```

### Generate training data

```bash
# 1. Pull latest sales data from Square
python square_extract.py

# 2. Join Square + roster + machine data → ProcessedData/Joined_DF_*.csv
python generate_common_file_from_data.py

# 3. Build instruction–output pairs → Training/final_file.json
python new_data.py
```

---

## Training on Google Colab

1. Upload `ProcessedData/` and `Training/final_file.json` to **Google Drive → ChoAI/**.
2. Open `Training_Notebook.ipynb` in Colab.
3. Add secrets in **Runtime → Secrets**:
   - `WANDB_API_KEY`
   - `HF_TOKEN` (HuggingFace write token)
4. Run all cells. The notebook will:
   - `git pull` the latest code from this repo
   - Fine-tune the selected model (Llama / Gemma / Qwen) with QLoRA via Unsloth
   - Push the LoRA adapter to HuggingFace Hub: `kasmello/ChoAI-<model>-adapter`
   - Log metrics to W&B project `ChoAI`

### Switching models

In `Training_Notebook.ipynb`, change `MODEL_KEY`:

```python
MODEL_KEY = "gemma"   # or "llama", "qwen", "mistral"
```

| Key | Model | Notes |
|---|---|---|
| `llama` | Llama-3.2-3B-Instruct | original baseline |
| `mistral` | Mistral-7B-Instruct-v0.3 | strong general model |
| `gemma` | Gemma-3-4B-it | efficient, Google-backed |
| `qwen` | Qwen2.5-Coder-7B-Instruct | code-specialised |

---

## Evaluation

Open `Inference_Notebook.ipynb` and set `EVAL_KEY` to the model you want to score. Metrics logged to W&B:

- **Syntax score** — does the generated code execute without error?
- **Title similarity** — cosine similarity between prompt and chart title (sentence-transformers)
- **Elements score** — does the chart include the Manjari font and logo?
- **Inference time** — seconds per generation

---

## Experiment tracking

W&B project: [kasmello/ChoAI](https://wandb.ai/kasmello/ChoAI)
