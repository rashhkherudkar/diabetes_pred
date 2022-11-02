from models.utils import DiabetesModel
from flask import Flask,jsonify,render_template,request
import config


app = Flask(__name__)

@app.route("/")

def hello_flask():
    print("We are in Flask API")
    return render_template("index.html")
    
@app.route("/diabetes_pred",methods=["POST"])

def get_predicted():

    Glucose = eval(request.form.get("Glucose"))
    BloodPressure =eval(request.form.get("BloodPressure"))
    SkinThickness = eval(request.form.get("SkinThickness"))
    Insulin = eval(request.form.get("Insulin"))
    BMI = eval(request.form.get("BMI"))
    DiabetesPedigreeFunction = eval(request.form.get("DiabetesPedigreeFunction"))
    Age = eval(request.form.get("Age"))

    print("Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age \n", Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)

    Obj=DiabetesModel(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    result1= Obj.pred_patients()
   
    return render_template("index.html",prediction=result1) 


if __name__ == "__main__":
    app.run(host="0.0.0.0",port = config.PORT_NUMBER, debug=True)