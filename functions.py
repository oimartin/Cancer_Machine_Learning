from keras.models import load_model
from sklearn.preprocessing import LabelEncoder, StandardScaler
from joblib import load
preprocess_pipeline = load('Model_Info/pipeline.joblib')
import pandas as pd
import numpy as np
from keras import backend as K

def NNpredict(values):
    
    values = values.reshape(1,-1)
    print(values.shape)
    
    cancer_pollution_model = load_model("Model_Info/neuralnetwork.h5")
    model = cancer_pollution_model
   
    values_scaled = preprocess_pipeline.transform(values)
    prediction = model.predict(values_scaled)

    NN_Dict = {"Larynx": f"{round(prediction[0][0]*100,2)}%", "Lung": f"{round(prediction[0][1]*100,2)}%",
                "Nasal": f"{round(prediction[0][2]*100,2)}%", "Trachea": f"{round(prediction[0][3]*100,2)}%"}

    K.clear_session()
    return NN_Dict    

def getNNvalues (state, race, year, gender):

    

    statelist = pd.Series(data=('AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI','IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI','MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV','NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX','UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'))
    racelist =pd.Series(data=("White", "Other Races and Unknown combined", "American Indian or Alaska Native", "Asian or Pacific Islander", "Black or African American"))     
    genderlist =pd.Series(data=("Male", "Female"))
    
    state_dummies=pd.get_dummies(statelist)
    race_dummies=pd.get_dummies(racelist)
    gender_dummies=pd.get_dummies(genderlist)

    state_dummies_select = state_dummies[state].values
    race_dummies_select = race_dummies[race].values
    gender_dummies_select = gender_dummies[gender].values

    state_dummy = state_dummies_select.tolist()
    race_dummy = race_dummies_select.tolist()
    gender_dummy = gender_dummies_select.tolist()
    
    data_cancer = race_dummy + gender_dummy + state_dummy

    pollution_data = pd.read_csv("Data/Data_for_Graphing/ARpollution.csv")
    pollution_data_clean= pollution_data[["State", "Year", "CO", "Lead", "NO2", "Ozone", "PM10", "PM2_5", "SO2"]]

    data_poll = pollution_data_clean.loc[(pollution_data_clean['Year']==year) & (pollution_data_clean["State"]==state)]


    data_pollution_dropped = data_poll.drop(["State", "Year"], axis = 1)
    data_pollution = data_pollution_dropped.values[0]
    data_pollution_list = data_pollution.tolist()

    data = data_pollution_list + data_cancer   
    print(data)
    print(np.array(data).shape)

    return np.array(data)