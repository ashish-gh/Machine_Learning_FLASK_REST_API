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
def main():
    return flask.render_template('predict.html')

    # return "Boston Housing Price Prediction"

@app.route('/predict', methods=['POST','GET'])
def predict():
    
    if flask.request.method == 'GET':
        return flask.render_template('predict.html' 
                                     )
            
    if flask.request.method == 'POST':
        try:
            CRIM = flask.request.form['CRIM']
            ZN = flask.request.form['ZN']
            INDUS = flask.request.form['INDUS']
            CHAS = flask.request.form['CHAS']
            NOX = flask.request.form['NOX']
            RM = flask.request.form['RM']
            AGE = flask.request.form['AGE']
            DIS = flask.request.form['DIS']
            RAD = flask.request.form['RAD']
            TAX = flask.request.form['TAX']
            PTRATIO = flask.request.form['PTRATIO']
            B = flask.request.form['B']
            LSTAT = flask.request.form['LSTAT']
            
            input_variables = pd.DataFrame([[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]],
                            columns=['CRIM', 'ZN', 'INDUX','CHAS', 'NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT'],
                                       dtype=float)
            
            
            prediction = classifier.predict(input_variables)[0]                        
            return flask.render_template('predict.html',
                                     result=prediction
                                     )
            
            
                                       
    
    
            # json_ = request.json
            # print(json_)
            # query_ = pd.get_dummies(pd.DataFrame(json_))
            # query = query_.reindex(columns = model_columns, fill_value= 0)
            # prediction = list(classifier.predict(query))
            
            # return jsonify({
            #     "prediction":str(prediction),
            # })

            



        except:
            return jsonify({
                "trace": traceback.format_exc()
                })

if __name__ == "__main__":
    app.run()



    