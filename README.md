# 🤖 ArabicaQA – Arabic Question Answering with a Fine-Tuned Language Model

This project provides an interactive Gradio-based interface to a fine-tuned Arabic language model capable of answering open-domain questions in Arabic.

---

## 📌 Project Overview

- **Objective**: Build a simple QA system for Arabic using a fine-tuned causal language model.
- **Interface**: Built with [Gradio](https://www.gradio.app/) for easy local testing and deployment.
- **Model**: Loaded from a local directory (`./arabicaqa_model-base22`) using Hugging Face Transformers.

---

## 🛠️ How It Works

The `test.py` script performs the following:
- Loads a tokenizer and model from a local directory
- Defines a `generate_answer(question)` function to tokenize input, run inference, and decode the output
- Wraps the function in a Gradio interface for real-time interaction

---

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/brahex123/arabicaqa.git
cd arabicaqa
```

2. Install required dependencies:

```bash
pip install gradio torch transformers
```

3. Run the app locally:

```bash
python test.py
```

Make sure the directory `./arabicaqa_model-base22` contains the trained model and tokenizer files.

---

## 📂 Files Included

```
arabicaqa/
├── test.py           # Main script to run the QA app using Gradio
├── test.ipynb        # Notebook version (for experimentation and testing)
├── arabicaqa_model-base22/   # Directory with fine-tuned model (not included)
└── README.md         # Project documentation
```

---

## 🧪 Example

Input:
```
ما هي عاصمة المغرب؟
```

Output:
```
الرباط
```

---

## 👨‍💻 Author

- **Brahim Mechaouat**  
  [Portfolio](https://brahex123.github.io/ibrahex123.github.io/)  
  [GitHub](https://github.com/brahex123)

---

## 📄 License

feel free to use and modify for research purposes.
