# ChatGPT-3-Tokenizer README

## Description

This is a tokenization application using the GPT-2 Tokenizer. It takes in an input string and outputs the tokens, token type IDs, attention mask, length and number of characters. The application also calculates the price of the tokenization based on the number of tokens generated.

## Requirements

python 3.6 or higher
tkinter
transformers
wonderwords
Installation

## Installing packages

Copy code
pip install tkinter
pip install transformers
pip install wonderwords
Usage

To run the application, run the script file in the terminal or command prompt.

## Copy code
python script.py
Functionalities

## Features
Tokenize input text using the GPT-2 Tokenizer.
Display tokens, token type IDs, attention mask, length and number of characters.
Display the price of tokenization based on the number of tokens generated.
Provide a help message box to assist users.
Generate random examples to be tokenized.

## Modules information
- **string**: By using string constants, the code is made more readable and maintainable.
tkinter: The tkinter library provides an easy way to create graphical interfaces. It is well-documented and widely used in the Python community.
- **scrolledtext**: The scrolledtext module provides a widget that can display a large amount of text and allows the user to scroll through it.
- **transformers**: The transformers library provides pre-trained models for NLP tasks. These models have been trained on large amounts of data and have achieved state-of-the-art performance on many NLP benchmarks.
- **GPT2TokenizerFast**: The GPT-2 tokenizer is a fast and efficient tokenizer for the GPT-2 transformer model. It provides the tokenized representation of the input text, which is used in the program.
- **wonderwords**: The wonderwords library provides a simple way to generate random sentences. This is useful for generating an example input for the tokenization.


## Note
The price calculation is based on the **Davinci token**, which is the default token used in the calculation. The prices of other tokens (_Curie, Babbage, Ada_) are also listed in the code for reference.

## GPT-3 Tokenizer Website:
[https://platform.openai.com/tokenizer](Chat-GPT Web based Tokenizer)

Written by Haseeb Mir having Apache License.