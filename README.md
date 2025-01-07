# bookgpt
This program is intended to guide ChatGPT through prompts to make it write entire novels. Later updates will enable it to make series of novels.

The books it makes require some minor edits so that the chapters flow seemlessly. It outputs text files. The users have to make the bookfile themselves. 


Don't check the box for custom number of chapters. It doesn't work right yet. I only left that in the GUI because I dont feel like changing more of the GUI code right now.

In order to run the program, you have to get an API key from OpenAI, and you probably need to setup a virtual environment to run this. I use a virtual environment.

Open a directory that you want the text files to be stored in, and run this in a terminal:

python3 '/path/to/bookGPTgui.py'

using the full path from the root of your system to the python file.


# WARNING ON TOKENS
You have to buy tokens from OpenAI in order to use the program, unless you're using a local model on your hardware. I'm doing what I can to reduce the number of tokens that it uses. I just spent a bunch of money testing this program. Dont blame me if you don't like how many tokens it cost to make a book, or if you didn't have enough tokens for it to finish making a book, or if you don't like the book and your tokens went to waste. I don't like how much it costs, and I'm the one who made the program. The update I gave it to make the chapters bigger made it a lot more expensive per-book. If you want it to make a cheaper book, then just replace the call for make_chapter2 to make_chapter. That makes a way cheaper book, but its way shorter. Another way to reduce the cost is to downgrade which GPT model the program calls. It uses GPT 4 right now, but it might do ok with a weaker GPT model.


# WARNING ON BOOK QUALITY
The current quality of the books it produces is low. The quality will go up quite a bit once the issues I posted get resolved. Probably best not to spend any tokens on this program until this message is no longer in the readme, unless you want to contribute to the program, or just throw some money away to test the program. But make no mistake, the books are not good right now.

# LOCALLY RAN LLM MODEL
If you run a GPT model, or some other LLM on your own computer, this program should be pretty easy to modify to use with that, and it wouldn't cost you anymore than whatever electricity the model causes your hardware to consume. You could just pump out one book after another and it would probably cost you next to nothing.


# PROJECT GOAL
The goal of this project is to make books that are written well enough that readers would not suspect that they are written by artificial intelligence.
