# 🌍 AI Language Translation Tool

A desktop-based **AI Language Translation Tool** developed in Python as part of the **CodeAlpha Internship – Task 1**.

The application provides a simple graphical interface for translating text between multiple languages, detecting the source language automatically, saving translation history, copying translated text, saving translations, and converting translated text into speech.

---

## 📌 Project Overview

The AI Language Translation Tool is designed to make text translation simple and user-friendly.

Users can enter text, select a source and target language, translate the text, and use additional features such as text-to-speech, copy, save, swap, and translation history.

The application is built using Python with a graphical user interface created using CustomTkinter.

---

## ✨ Features

### 🌐 Text Translation

- Translate text between multiple supported languages.
- Supports languages including:
  - English
  - Urdu
  - French
  - German
  - Spanish
  - Italian
  - Hindi
  - Arabic
  - Chinese
  - Japanese
  - Korean
  - Russian
  - Turkish
  - Portuguese

### 🔍 Automatic Language Detection

- Automatically detects the source language when **Auto Detect** is selected.

### 🔄 Language Swap

- Swap the selected source and target languages.

### 📋 Copy Translation

- Copy translated text directly to the clipboard.

### 💾 Save Translation

- Save translated text as a `.txt` file.

### 🗂️ Translation History

- Translation records are automatically stored in:

```text
history/history.txt

The history contains:

* Date and time
* Original text
* Translated text

### 🔊 Text-to-Speech

* Convert translated text into speech.
* Supports multilingual speech generation.
* Uses text-to-speech functionality for supported languages.

### 🧹 Clear Function

* Clear both input and output text areas.
* Reset language selections.

### 🖥️ Graphical User Interface

* Built using **CustomTkinter**.
* Simple and user-friendly interface.
* Separate input and translated-output sections.
* Status messages provide feedback to the user.

---

## 🛠️ Technologies Used

* **Python**
* **CustomTkinter**
* **Google Translate / Translation Library**
* **gTTS (Google Text-to-Speech)**
* **pyttsx3**
* **SpeechRecognition**
* **Pyperclip**
* **Tkinter**
* **OS/File Handling**

---

## 📂 Project Structure

```text
Language-Translation-Tool/
│
├── app.py
├── translator.py
├── tts.py
├── speech.py
├── utils.py
├── voice_test.py
├── test_tts.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── history/
    └── history.txt
```

### File Description

| File               | Description                                      |
| ------------------ | ------------------------------------------------ |
| `app.py`           | Main application and graphical user interface    |
| `translator.py`    | Translation and language detection functionality |
| `tts.py`           | Multilingual text-to-speech functionality        |
| `speech.py`        | Speech-related functionality                     |
| `utils.py`         | Translation history management                   |
| `voice_test.py`    | Voice testing utility                            |
| `test_tts.py`      | Text-to-speech testing                           |
| `requirements.txt` | Required Python packages                         |
| `.gitignore`       | Prevents unnecessary files from being uploaded   |
| `README.md`        | Project documentation                            |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Haniya-Ramzan/CodeAlpha_LanguageTranslationTool.git
```

### 2. Open the Project Folder

```bash
cd CodeAlpha_LanguageTranslationTool
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

If you are installing packages individually, the main dependencies include:

```bash
pip install customtkinter
pip install pyperclip
pip install pyttsx3
pip install gTTS
pip install SpeechRecognition
```

---

## ▶️ How to Run

Run the main application using:

```bash
python app.py
```

The application window will open.

---

## 📝 How to Use

### Step 1 — Enter Text

Enter the text you want to translate in the **Enter Text** section.

### Step 2 — Select Source Language

Choose the source language.

You can select:

```text
Auto Detect
```

to automatically detect the source language.

### Step 3 — Select Target Language

Choose the language into which you want to translate the text.

### Step 4 — Translate

Click:

```text
🌐 Translate
```

The translated text will appear in the output section.

### Step 5 — Additional Actions

You can then use:

```text
📋 Copy
🗑 Clear
🔄 Swap
💾 Save
🔊 Speak
```

to perform additional actions on the translated text.

---

## 🔊 Text-to-Speech

The application provides text-to-speech functionality for translated text.

The speech functionality can generate speech for supported languages and open the generated audio when applicable.

The project uses:

* `gTTS`
* `pyttsx3`

for speech-related functionality.

---

## 🗂️ Translation History

Every completed translation can be stored in:

```text
history/history.txt
```

Example:

```text
======================================================================
Date & Time : 12-08-2026 05:30:00 PM
======================================================================

Original Text:
Hello

Translated Text:
Bonjour

----------------------------------------------------------------------
```

This allows previous translations to be recorded for reference.

---

## 🖥️ Application Interface

The application provides:

* Language selection controls
* Text input area
* Translation button
* Translation output area
* Copy button
* Clear button
* Swap button
* Save button
* Speak button
* Status information

---

## 🎯 Internship Task

This project was developed as part of the:

**CodeAlpha Internship**

### Task 1: Language Translation Tool

The objective of the project is to develop a Python-based translation application with a graphical user interface and supporting translation and speech functionality.

---

## 📚 Learning Outcomes

Through this project, the following concepts were practiced:

* Python GUI development
* Python functions and modules
* API/library integration
* Language detection
* Text translation
* File handling
* Translation history management
* Text-to-speech
* Exception handling
* Clipboard operations
* Git and GitHub
* Project documentation

---

## 🔐 Notes

* Internet connectivity may be required for online translation and Google Text-to-Speech functionality.
* Speech output depends on the available system voices and supported language configuration.
* Generated audio files should not be committed to the repository unnecessarily.

---

## 👩‍💻 Developer

**Haniya Ramzan**

BSIT Student

GitHub:

https://github.com/Haniya-Ramzan

---

## 📌 Repository

**CodeAlpha Language Translation Tool**

https://github.com/Haniya-Ramzan/CodeAlpha_LanguageTranslationTool

---

## ⭐ Acknowledgement
Developed as part of the CodeAlpha Internship Program.
