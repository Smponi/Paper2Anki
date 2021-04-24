<p align="center">
  <img src="logo.png">
</p>

## Introduction

Paper2Anki is your way to **write** your flashcards. Goodnotes 5 released a gamechanger in my opinion. You just write your flashcards,and you can study with them.
However, I don't like the idea of only learning in Goodnotes and their algorithm needs some work imo.
So I decided to create a way to make flashcards in Goodnotes (Or any other notes app) and export them to Anki!

## How to create flashcards

It's just as simple as writing!  
You just write on each page your Question on the top half of the page
and the answer on the bottom part.
Then you just need to export your document as a pdf.
So each of your page should look like this:

<p align="right">
<img width=150  src="templatepaper.png">
</p>

## Requirements

- Make sure you have **python3** installed.
- Run `pip install -r requirements.txt`  
   to install the packages required to run the script.

## Usage

This script is run within the terminal. 
### Windows
For Windows type _cmd_ in the search bar and then just follow the steps.
### Linux
You should know what the terminal is.

### MacOS
Open spotlight and search there for Terminal and then just follow the steps.

### Use

1. Run `python paper2anki.py YOURFILE.PDF NAME`  
   So you give the program 2 Arguments:
   1. The PDF file which contains the flash cards
   2. The name you wish the deck to have.
2. Import the .apkg file into Anki
3. Study

## Credits:

- Icon in logo: https://www.flaticon.com/free-icon/script_708922
- genanki (library to create anki cards in python): https://github.com/kerrickstaley/genanki
- pdfrw great pdf library: https://pypi.org/project/pdfrw/
