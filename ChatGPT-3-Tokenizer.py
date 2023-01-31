""" Tokenizer is a simple GUI that allows you to tokenize text using the GPT-2 Tokenizer.
    It will output the tokens, token type IDs, attention mask, length and number of characters.
    It also calculates the price per token based on the model you choose.
    Written by: @Haseeb Mir.
    Tools used: Python 3.9.7, PyCharm 2021.2.3, Tkinter, Transformers 4.11.3, Wonderwords 1.0.1.
    VSC Version: 1.60.2.
    Dated 2021-09-13.
"""

# Import modules
import string
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

# Create dictonary of prices for each token Davinci = 0.0200 / 1000 tokens, Curie = 0.0020/ 1000 tokens, Babbage = 0.0005 / 1000 tokens, Ada = 0.0004 / 1000 tokens
prices = {"davinci": (0.0200/ 1000), "curie": (0.0020/1000), "babbage": (0.0005/1000), "ada":(0.0004/1000)}

# This method tokenizes the given text using the GPT-2 Tokenizer. It then outputs the tokens, token type IDs, attention mask, length and number of characters.
def tokenize_input():
    
    '''
    This function tokenizes the given text using the GPT-2 Tokenizer. 
    It then outputs the tokens, token type IDs, attention mask, length and number of characters.
    '''
    
    tokenizer = GPT2TokenizerFast.from_pretrained(model_entry.get())
    input_text = input_textbox.get("1.0", tk.END)
    token_dict = tokenizer(input_text)
    tokens = token_dict['input_ids']
    attention_mask = token_dict['attention_mask']
    token_length = len(tokens)
    characters = len(input_text)
    input_ids_output.configure(state="normal")
    input_ids_output.delete(1.0, tk.END)
    input_ids_output.configure(font=fonts_arial)
    input_ids_output.insert(tk.INSERT, f"{tokens}")
    input_ids_output.configure(state="disabled")

    attention_mask_output.configure(state="normal")
    attention_mask_output.delete(1.0, tk.END)
    attention_mask_output.configure(font=fonts_arial)
    attention_mask_output.insert(tk.INSERT, f"{attention_mask}")
    attention_mask_output.configure(state="disabled")

    token_output.configure(state="normal")
    token_output.delete(1.0, tk.END)
    token_output.configure(font=fonts_arial)
    token_output.insert(tk.INSERT, f"{token_length}")
    token_output.configure(state="disabled")

    characters_output.configure(state="normal")
    characters_output.delete(1.0, tk.END)
    characters_output.configure(font=fonts_arial)
    characters_output.insert(tk.INSERT, f"{characters}")
    characters_output.configure(state="disabled")
    
    price_output.configure(state="normal")
    price_output.delete(1.0, tk.END)
    price_output.configure(font=fonts_arial)
    price_per_token = token_length * prices["davinci"]
    price_output.insert(tk.INSERT, f"{price_per_token:.8f} USD")
    price_output.configure(state="disabled")

def show_help():
    '''
    This function will show a help messagebox 
    '''
    messagebox.showinfo("Help", "This application tokenizes the given text using the GPT-2 Tokenizer. It will output the tokens, token type IDs, attention mask, length and number of characters.")

# This method generates a random sentence using the Wonderwords module.
def generate_example():
    '''
    This fuction will generate a random string of characters
    '''
    random_sentence = RandomSentence()
    example_text = random_sentence.sentence()
    input_textbox.delete("1.0", tk.END)
    input_textbox.insert(tk.INSERT, example_text)

# These are helper functions to add and delete data from the entry boxes
def add_data_entry(entry:tk.Entry, data):
    '''
    This function will add the given data to the entry
    '''
    delete_data_entry(entry)
    entry.insert(0, data)

def delete_data_entry(entry:tk.Entry):
    '''
    This function will delete the data from the given entry
    '''
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

input_ids_label = tk.Label(root, text="Input IDs:")
input_ids_label.pack()

input_ids_output = scrolledtext.ScrolledText(root, width=50, height=2, state="disabled")
input_ids_output.pack()

attention_mask_label = tk.Label(root, text="Attention Mask:")
attention_mask_label.pack()

attention_mask_output = scrolledtext.ScrolledText(root, width=50, height=2, state="disabled")
attention_mask_output.pack()

token_label = tk.Label(root, text="Tokens:")
token_label.pack()

token_output = scrolledtext.ScrolledText(root, width=50, height=2, state="disabled")
token_output.pack()

characters_label = tk.Label(root, text="Characters:")
characters_label.pack()

characters_output = scrolledtext.ScrolledText(root, width=50, height=2, state="disabled")
characters_output.pack()

price_label = tk.Label(root, text="Price in $:")
price_label.pack()

price_output = scrolledtext.ScrolledText(root, width=50, height=2, state="disabled")
price_output.pack()

# Main method doing the GUI stuff. Note that GPT-2 is the default model.
if __name__ == "__main__":
    if model_entry.get() == "":
        add_data_entry(model_entry, "gpt2")
        
    root.mainloop()