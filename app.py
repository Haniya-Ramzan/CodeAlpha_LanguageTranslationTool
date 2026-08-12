import customtkinter as ctk
from translator import translate_text, detect_language
from utils import save_history
from tts import speak_multilingual
import pyperclip
from tkinter import filedialog



# -------------------------
# Functions
# -------------------------

def translate_button_action():

    text = input_box.get("1.0", "end").strip()

    if text == "":
        output_box.delete("1.0", "end")
        output_box.insert("end", "Please enter text first.")
        status.configure(
            text="Status : Please enter some text."
        )
        return

    source = source_menu.get()
    target = target_menu.get()

    # -------------------------
    # Auto Detect
    # -------------------------

    if source == "Auto Detect":

        source = detect_language(text)

    # -------------------------
    # Same Language Check
    # -------------------------

    if source == target:

        output_box.delete("1.0", "end")
        output_box.insert("end", text)

        status.configure(
            text=f"Status : Source and Target are both {source}"
        )

        return

    # -------------------------
    # Translation
    # -------------------------

    result = translate_text(
        text,
        source,
        target
    )

    output_box.delete("1.0", "end")
    output_box.insert("end", result)

    save_history(
        text,
        result
    )

    status.configure(
        text=f"Status : {source} → {target} Translation Completed"
    )
# -------------------------
# Clear Text
# -------------------------

def clear_text():

    input_box.delete("1.0", "end")
    output_box.delete("1.0", "end")

    source_menu.set("Auto Detect")
    target_menu.set("English")

    status.configure(
        text="Status : Everything Cleared"
    )


# -------------------------
# Copy Translation
# -------------------------

def copy_text():

    translated_text = output_box.get("1.0", "end").strip()

    if translated_text == "":

        status.configure(
            text="Status : Nothing to Copy"
        )

        return

    pyperclip.copy(translated_text)

    status.configure(
        text="Status : Translation Copied Successfully"
    )


# -------------------------
# Swap Languages
# -------------------------

def swap_languages():

    source = source_menu.get()
    target = target_menu.get()

    if source == "Auto Detect":

        status.configure(
            text="Status : Auto Detect cannot be swapped."
        )

        return

    source_menu.set(target)
    target_menu.set(source)

    status.configure(
        text=f"Status : {target} ↔ {source}"
    )


# -------------------------
# Save Translation
# -------------------------

def save_translation():

    translated_text = output_box.get("1.0", "end").strip()

    if translated_text == "":

        status.configure(
            text="Status : Nothing to Save"
        )

        return

    filename = filedialog.asksaveasfilename(

        defaultextension=".txt",

        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]

    )

    if filename:

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(translated_text)

        status.configure(
            text="Status : Translation Saved Successfully"
        )

    else:

        status.configure(
            text="Status : Save Cancelled"
        )
# -------------------------
# Text To Speech
# -------------------------

def speak_translation():

    text = output_box.get("1.0", "end").strip()

    if text == "":

        status.configure(
            text="Status : Nothing to Speak"
        )

        return


    language = target_menu.get()


    success = speak_multilingual(
        text,
        language
    )


    if success:

        status.configure(
            text=f"Status : Speaking {language} Translation"
        )

    else:

        status.configure(
            text="Status : Speech Failed"
        )
# -------------------------
# Appearance
# -------------------------

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


# -------------------------
# Main Window
# -------------------------

app = ctk.CTk()

app.title("🌍 AI Language Translation Tool")

app.geometry("1100x900")

app.resizable(False, False)


# -------------------------
# Heading
# -------------------------

title = ctk.CTkLabel(
    app,
    text="🌍 AI Language Translation Tool",
    font=("Arial", 30, "bold")
)

title.pack(
    pady=(20, 5)
)


subtitle = ctk.CTkLabel(
    app,
    text="Translate text between multiple languages using Artificial Intelligence",
    font=("Arial", 15)
)

subtitle.pack(
    pady=(0, 15)
)


# -------------------------
# Language Selection
# -------------------------

language_frame = ctk.CTkFrame(app)

language_frame.pack(
    pady=10,
    padx=20,
    fill="x"
)


languages = [
    "Auto Detect",
    "English",
    "Urdu",
    "French",
    "German",
    "Spanish",
    "Italian",
    "Hindi",
    "Arabic",
    "Chinese",
    "Japanese",
    "Korean",
    "Russian",
    "Turkish",
    "Portuguese"
]


source_label = ctk.CTkLabel(
    language_frame,
    text="Source Language"
)

source_label.grid(
    row=0,
    column=0,
    padx=20,
    pady=10
)


source_menu = ctk.CTkComboBox(
    language_frame,
    values=languages,
    width=180
)

source_menu.set("Auto Detect")

source_menu.grid(
    row=0,
    column=1,
    padx=10
)


target_label = ctk.CTkLabel(
    language_frame,
    text="Target Language"
)

target_label.grid(
    row=0,
    column=2,
    padx=20
)


target_menu = ctk.CTkComboBox(
    language_frame,
    values=languages,
    width=180
)

target_menu.set("English")

target_menu.grid(
    row=0,
    column=3,
    padx=10
)

# -------------------------
# Input Section
# -------------------------

input_label = ctk.CTkLabel(
    app,
    text="Enter Text",
    font=("Arial", 18, "bold")
)
input_label.pack(anchor="w", padx=25)

input_box = ctk.CTkTextbox(
    app,
    width=1000,
    height=120
)
input_box.pack(padx=20, pady=5)


# -------------------------
# Translate Button
# -------------------------

translate_button = ctk.CTkButton(
    app,
    text="🌐 Translate",
    width=220,
    height=42,
    command=translate_button_action
)
translate_button.pack(pady=10)


# -------------------------
# Output Section
# -------------------------

output_label = ctk.CTkLabel(
    app,
    text="Translated Text",
    font=("Arial", 18, "bold")
)
output_label.pack(anchor="w", padx=25)

output_box = ctk.CTkTextbox(
    app,
    width=1000,
    height=120
)
output_box.pack(padx=20, pady=5)


# -------------------------
# Buttons Frame
# -------------------------

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=15)

copy_btn = ctk.CTkButton(
    button_frame,
    text="📋 Copy",
    width=130,
    command=copy_text
)
copy_btn.grid(row=0, column=0, padx=8)

clear_btn = ctk.CTkButton(
    button_frame,
    text="🗑 Clear",
    width=130,
    command=clear_text
)
clear_btn.grid(row=0, column=1, padx=8)

swap_btn = ctk.CTkButton(
    button_frame,
    text="🔄 Swap",
    width=130,
    command=swap_languages
)
swap_btn.grid(row=0, column=2, padx=8)

save_btn = ctk.CTkButton(
    button_frame,
    text="💾 Save",
    width=130,
    command=save_translation
)
save_btn.grid(row=0, column=3, padx=8)

speak_btn = ctk.CTkButton(
    button_frame,
    text="🔊 Speak",
    width=130,
    command=speak_translation
)

speak_btn.grid(
    row=0,
    column=4,
    padx=8
)
# -------------------------
# Status Bar
# -------------------------

status = ctk.CTkLabel(
    app,
    text="Status : Ready",
    font=("Arial", 14)
)
status.pack(pady=12)


# -------------------------
# Run Application
# -------------------------

app.mainloop()