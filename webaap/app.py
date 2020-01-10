from flask import Flask, render_template, request, jsonify
import flask


# App defination
app = Flask(__name__,template_folder='templates')

@app.route('/')
def welcome():
    return "Boston Housing Price Prediction"

if __name__ == "__main__":
    app.run()



    