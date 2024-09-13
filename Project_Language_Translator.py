from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox
import pyttsx3

root = Tk()
root.configure(bg="lightblue")
root.title("E-Translate (Language Translator)")

# List of Languages from GoogleTrans
languages = googletrans.LANGUAGES

# Capitalize the first letter of each item in the list
capitalized_languages = {key: value.capitalize() for key, value in languages.items()}
language_list = list(capitalized_languages.values())


# Functions
def translate():
    # Deletes any previous translations
    translated_text.delete(1.0, END)

    try:
        for key, value in capitalized_languages.items():
            if value == original_combo.get():
                original_language_key = key

        for key, value in capitalized_languages.items():
            if value == translated_combo.get():
                translated_language_key = key

        # Turns original text into a TextBlob
        words = textblob.TextBlob(original_text.get(1.0, END))

        # Translates text
        words = words.translate(original_language_key, translated_language_key)

        # Produces output of translated text to screen
        translated_text.insert(1.0, words)

    except Exception:
        if not original_text.get(1.0, END).strip():  # Checks if text box is empty
            messagebox.showerror("Error", "Please fill in text to be translated")


def original_speech():
    # Initialize the speech engine
    engine1 = pyttsx3.init()

    # Voice
    engine1.getProperty("voices")

    # Pass text to speech engine
    words = original_text.get(1.0, END)
    engine1.say(words)

    # Run to engine
    engine1.runAndWait()


def translated_speech():
    # Initialize the speech engine
    engine2 = pyttsx3.init()

    # Voice
    engine2.getProperty("voices")

    # Pass text to speech engine
    words = translated_text.get(1.0, END)
    engine2.say(words)

    # Run to engine
    engine2.runAndWait()


def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)


def exit_program():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?") is True:
        messagebox.showinfo("THANK YOU", "Hope you enjoyed our app! ")
        root.quit()
    else:
        pass


# Text Boxes and Labels
main_header = Label(root, text="E-Translate", fg="purple", bg="lightblue",
                    font=("Times New Roman", 35), anchor=N)
main_header.grid(row=0, column=2, pady=10)

header1 = Label(root, text="Original Text", bg="lightblue", font=("Times New Roman", 20))
header1.grid(row=1, column=1)

header2 = Label(root, text="Translated Text", bg="lightblue", font=("Times New Roman", 20))
header2.grid(row=1, column=3)

original_text = Text(root, width=50, bd=3)
original_text.grid(row=2, column=1, pady=10, padx=20)

translated_text = Text(root, width=50, bd=3)
translated_text.grid(row=2, column=3, pady=10, padx=20)

# Buttons
translateButton = Button(root, text="Translate", bd=5, width=10, font=5, command=translate)
translateButton.grid(row=2, column=2, padx=10)

clearButton = Button(root, text="Clear", command=clear)
clearButton.grid(row=3, column=2, pady=10)

exitButton = Button(root, text="Exit Program", bg="red", command=exit_program)
exitButton.grid(row=4, column=2, pady=20)

speech1 = Button(root, text="\U0001F50A", font=20, command=original_speech)
speech1.grid(row=3, column=0, padx=20)

speech2 = Button(root, text="\U0001F50A", font=20, command=translated_speech)
speech2.grid(row=3, column=4, padx=20)

# Combo Boxes
original_combo = ttk.Combobox(root, width=50, values=language_list)
original_combo.current(21)
original_combo.grid(row=3, column=1)

translated_combo = ttk.Combobox(root, width=50, values=language_list)
translated_combo.current(26)
translated_combo.grid(row=3, column=3)

root.mainloop()
