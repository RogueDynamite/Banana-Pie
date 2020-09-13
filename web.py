# File for managing the website for the bot.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def banana_pie():
        return '<img src="https://www.spendwithpennies.com/wp-content/uploads/2019/07/Banana-Cream-Pie01-SpendWithPennies-3.jpg">'

