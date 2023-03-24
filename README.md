# ChatGPT-3-Tokenizer README

## Description

This is a Token information application using the GPT-2 Tokenizer. It takes in an input string and outputs the information of tokens, token type IDs, attention mask. The application also calculates the price of the tokens based on the number of tokens generated.

## GUI Main Application:
![main_gui](https://raw.githubusercontent.com/haseeb-heaven/ChatGPT-3-Tokenizer/main/main_app_ui.png)

## Help section:
![main_gui](https://raw.githubusercontent.com/haseeb-heaven/ChatGPT-3-Tokenizer/main/main_app_help.png)

## Requirements

python 3.6 or higher
- tkinter
- transformers
- wonderwords

## Installation

## Installing packages
- pip install tkinter
- pip install transformers
- pip install wonderwords

## Features
- Tokenize input text using the GPT-2 Tokenizer.
- Display tokens, token type IDs, attention mask, length and number of characters.
- Display the price of tokenization based on the number of tokens generated.
- Provide a help message box to assist users.
- Generate random examples to be tokenized.

## Modules information
- **tkinter**: The tkinter library provides an easy way to create graphical interfaces. It is well-documented and widely used in the Python community.
- **transformers**: The transformers library provides pre-trained models for NLP tasks. These models have been trained on large amounts of data and have achieved state-of-the-art performance on many NLP benchmarks.
- **GPT2TokenizerFast**: The GPT-2 tokenizer is a fast and efficient tokenizer for the GPT-2 transformer model. It provides the tokenized representation of the input text, which is used in the program.
- **wonderwords**: The wonderwords library provides a simple way to generate random sentences. This is useful for generating an example input for the tokenization.


## Note
The price calculation is based on the **Davinci token**, which is the default token used in the calculation. The prices of other tokens (_Curie, Babbage, Ada_) are also listed in the code for reference.

## GPT-3 Tokenizer Website:
Visit [Chat-GPT3 Tokenizer](https://platform.openai.com/tokenizer) website for checking official Web-based Tokenizer.

Written by Haseeb Mir having Apache License.
