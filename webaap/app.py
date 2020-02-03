from flask import Flask, render_template, request, jsonify
import flask


# App defination
app = Flask(__name__,template_folder='templates')

# importing models
with open('webapp/model/model.pkl', 'rb') as f:
    classifier = pickle.load (f)

with open('webapp/model/model_columns.pkl', 'rb') as f:
    model_columns = pickle.load (f)


@app.route('/')
def welcome():
    return "Boston Housing Price Prediction"

if __name__ == "__main__":
    app.run()



    