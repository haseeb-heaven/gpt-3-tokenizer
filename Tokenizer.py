""" Tokenizer is a simple GUI that allows you to tokenize text using the GPT-2 Tokenizer.
    It will output the tokens, token type IDs, attention mask.
    It also calculates the price per token based on the model you choose.
    Written by: @Haseeb Mir.
    Dated 2021-09-13.
"""

# Import modules
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter as tk
from transformers import GPT2TokenizerFast
from wonderwords import RandomSentence

# Fixed screen size
root = tk.Tk()
root.title("Tokenizer")
root.geometry("350x580")

# Disable maximize button
root.resizable(0, 0)
fonts_arial = "Arial 14 bold"

# Dictonary of prices for each token Davinci = 0.0200 / 1000 tokens, Curie = 0.0020/ 1000 tokens, Babbage = 0.0005 / 1000 tokens, Ada = 0.0004 / 1000 tokens
prices = {"davinci": (0.0200/ 1000), "curie": (0.0020/1000), "babbage": (0.0005/1000), "ada":(0.0004/1000)}

# This is helper method that updates the text box UI.
def update_text_box(text_box, font, value):
    text_box.configure(state="normal")
    text_box.delete(1.0, tk.END)
    text_box.configure(font=font)
    text_box.insert(tk.INSERT, value)
    text_box.configure(state="disabled")

# This method tokenizes the given text using the GPT-2 Tokenizer. It then outputs the tokens, token type IDs, attention mask, length and number of characters.
def tokenize_input():
    input_model = model_entry.get()
    tokenizer = GPT2TokenizerFast.from_pretrained(input_model)
    input_text = input_textbox.get("1.0", tk.END)
    token_dict = tokenizer(input_text)
    tokens = token_dict['input_ids']
    attention_mask = token_dict['attention_mask']
    token_length = len(tokens)
    characters = len(input_text)

    update_text_box(input_ids_output, fonts_arial, f"{tokens}")
    update_text_box(attention_mask_output, fonts_arial, f"{attention_mask}")
    update_text_box(token_output, fonts_arial, f"{token_length}")
    update_text_box(characters_output, fonts_arial, f"{characters}")

    price_per_token = token_length * prices["davinci"]
    update_text_box(price_output, fonts_arial, f"{price_per_token:.5f}")

def show_help():
    messagebox.showinfo("Help", "This application tokenizes the given text using the GPT-2 Tokenizer. It will output the tokens, token type IDs, attention mask information.")

# This method generates a random sentence using the Wonderwords module.
def generate_example():
    random_sentence = RandomSentence()
    example_text:str = ""
    
    for i in range(5):
        example_text += random_sentence.sentence() + "\n"
    input_textbox.delete("1.0", tk.END)
    input_textbox.insert(tk.INSERT, example_text)

# These are helper functions to add and delete data from the entry boxes
def add_data_entry(entry:tk.Entry, data):
    delete_data_entry(entry)
    entry.insert(0, data)

def delete_data_entry(entry:tk.Entry):
    entry.delete(0, tk.END)

# Setting up the GUI.
model_label = tk.Label(root, text="Model:")
model_label.pack()

model_entry = tk.Entry(root,font=fonts_arial)
model_entry.pack()

text_label = tk.Label(root, text="Enter text:")
text_label.pack()

input_textbox = scrolledtext.ScrolledText(root, width=50, height=5, font=fonts_arial)
input_textbox.pack()

button = tk.Button(root, text="Tokenize", command=tokenize_input)
button.pack()

help_button = tk.Button(root, text="Help", command=show_help)
help_button.pack()

example_button = tk.Button(root, text="Show Examples", command=generate_example)
example_button.pack()

input_ids_label = tk.Label(root, text="INPUT ID")
input_ids_label.pack()

input_ids_output = scrolledtext.ScrolledText(root, width=50, height=2, state="disabled")
input_ids_output.pack()

attention_mask_label = tk.Label(root, text="ATTENTION MASK:")
attention_mask_label.pack()

attention_mask_output = scrolledtext.ScrolledText(root, width=50, height=2, state="disabled")
attention_mask_output.pack()

token_label = tk.Label(root, text="TOKENS")
token_label.pack()

token_output = scrolledtext.ScrolledText(root, width=50, height=2, state="disabled")
token_output.pack()

characters_label = tk.Label(root, text="CHARACTERS")
characters_label.pack()

characters_output = scrolledtext.ScrolledText(root, width=50, height=2, state="disabled")
characters_output.pack()

price_label = tk.Label(root, text="PRICE")
price_label.pack()

price_output = scrolledtext.ScrolledText(root, width=50, height=2, state="disabled")
price_output.pack()

# Main method doing the GUI stuff. Note that GPT-2 is the default model.
if __name__ == "__main__":
    if model_entry.get() == "":
        add_data_entry(model_entry, "gpt2")
        
    root.mainloop()