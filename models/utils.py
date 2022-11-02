
import pickle
import numpy as np
import json
#import config

class DiabetesModel():
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):

        self.Glucose= Glucose
        self.BloodPressure= BloodPressure
        self.SkinThickness= SkinThickness
        self.Insulin= Insulin
        self.BMI= BMI
        self.DiabetesPedigreeFunction= DiabetesPedigreeFunction
        self.Age= Age

    def load_model(self):
        with open(r"C:\Users\Rahul\Desktop\logictics\Diabetes1\Diabetes1\models\Diabetes_model.pkl", "rb") as f:
            self.model = pickle.load(f)

        with open(r"C:\Users\Rahul\Desktop\logictics\Diabetes1\Diabetes1\models\data.json", "r") as f:
            self.data =json.load(f) 

    def pred_patients(self):
        self.load_model()

        array = np.zeros(len(self.data["column_name"]))  

        array[0] = self.Glucose
        array[1] = self.BloodPressure
        array[2] = self.SkinThickness
        array[3] = self.Insulin
        array[4] = self.BMI
        array[5] = self.DiabetesPedigreeFunction
        array[6] = self.Age  

        Diabetes_model = self.model.predict([array])[0]
        print (Diabetes_model)

        if Diabetes_model == 1:
            return "Patient is Diabetic.Please take care!!"
    
        else:
            return "Patient is NOT diabetic. Have a great day♥♥"

if __name__ == "__main__":
    Glucose= 145
    BloodPressure= 60
    SkinThickness= 30
    Insulin= 35
    BMI= 24.5
    DiabetesPedigreeFunction= 0.55
    Age= 55

    obj = DiabetesModel(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    result = obj.pred_patients()
    print(f" {result} ")
