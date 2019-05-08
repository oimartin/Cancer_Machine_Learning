data_predict_list = []

statelist = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI',
       'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI',
       'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV',
       'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX',
       'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
racelist = ["White", "Other Races and Unknown combined", "American Indian or Alaska Native", "Asian or Pacific Islander", "Black or African American"]       
sexlist =["Male", "Female"]
  #dependencies
import requests
import os
import pandas as pd
import statistics
from pandas import Series
from matplotlib import pyplot as plt
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
import numpy
from statsmodels.tsa.ar_model import AR
from statsmodels.tsa.ar_model import ARResults

for i in range (0, len(sexlist)):
    for j in range (0, len(racelist)):
        for k in range (0, len(statelist)):


            state =  statelist[k]
            choice = "../Data/cancer.csv"
            race = racelist[j]
            sex = sexlist[i]
            yhat_list=[]

            # In[3]:


            choice_df = pd.read_csv(choice)


            # In[4]:


            choice_df = choice_df.fillna(0)
            choice_df = choice_df.replace("Not Applicable", 0)
            choice_df["Crude Rate"] = choice_df["Crude Rate"].astype(float)


            # In[5]:


            index = choice_df.Year.unique()
            larynx = choice_df[(choice_df["Race"] == race ) & (choice_df["State"] == state) & (choice_df["Cancer Sites"]=="Larynx") & (choice_df["Sex"]==sex)]["Crude Rate"].values
            lung = choice_df[(choice_df["Race"] == race )&(choice_df["State"] == state) & (choice_df["Cancer Sites"]=="Lung and Bronchus")& (choice_df["Sex"]==sex)]["Crude Rate"].values
            nasal = choice_df[(choice_df["Race"] == race )&(choice_df["State"] == state) & (choice_df["Cancer Sites"]=="Nose, Nasal Cavity and Middle Ear")& (choice_df["Sex"]==sex)]["Crude Rate"].values
            trachea = choice_df[(choice_df["Race"] == race )&(choice_df["State"] == state) & (choice_df["Cancer Sites"]=="Trachea, Mediastinum and Other Respiratory Organs")& (choice_df["Sex"]==sex)]["Crude Rate"].values


            # In[6]:


            cancers = [larynx, lung, nasal, trachea]
            prediction_X = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]




            def ar_data(series):

                def difference(dataset):
                    diff = list()
                    for i in range(1, len(dataset)):
                        value = dataset[i] - dataset[i - 1]
                        diff.append(value)
                    return numpy.array(diff)

                # load dataset
                X = difference(series.values)
                # fit model
                model = AR(X)
                model_fit = model.fit(maxlag=5, disp=False)
                # save model to file
                model_fit.save('../Model_Info/ar_model.pkl')
                # save the differenced dataset
                numpy.save('../Model_Info/ar_data.npy', X)
                # save the last ob
                numpy.save('../Model_Info/ar_obs.npy', [series.values[-1]])# load the AR model from file
                loaded = ARResults.load('../Model_Info/ar_model.pkl')
                
                data = numpy.load('../Model_Info/ar_data.npy')
                
                last_ob = numpy.load('../Model_Info/ar_obs.npy')
                


        


            def predict(series):
            # load dataset
                def difference(dataset):
                    diff = list()
                    for i in range(1, len(dataset)):
                        value = dataset[i] - dataset[i - 1]
                        diff.append(value)
                    return numpy.array(diff)

                import numpy
                X = difference(series.values)
                # fit model
                window_size = 5
                model = AR(X)
                model_fit = model.fit(maxlag=window_size, disp=False)
                # save coefficients
                coef = model_fit.params
                numpy.save('../Model_Info/man_model.npy', coef)
                # save lag
                lag = X[-window_size:]
                numpy.save('../Model_Info/man_data.npy', lag)
                # save the last ob
                numpy.save('../Model_Info/man_obs.npy', [series.values[-1]])
                coef = numpy.load('../Model_Info/man_model.npy')
                lag = numpy.load('../Model_Info/man_data.npy')
                last_ob = numpy.load('../Model_Info/man_obs.npy')

                
                yhat=[]
                for prediction in prediction_X:
                    import numpy
                    def predict(coef, history):
                        yhat = coef[0]
                        for i in range(1, len(coef)):
                            yhat += coef[i] * history[-i]
                        return yhat

                    # load model
                    coef = numpy.load('../Model_Info/man_model.npy')
                    lag = numpy.load('../Model_Info/man_data.npy')
                    last_ob = numpy.load('../Model_Info/man_obs.npy')
                    # make prediction
                    prediction = predict(coef, lag)
                    # transform prediction
                    y_predict = prediction + last_ob[0]
                    yhat.append(y_predict)
                    # get real observation
                    observation = prediction
                    # update and save differenced observation
                    lag = numpy.load('../Model_Info/man_data.npy')
                    last_ob = numpy.load('../Model_Info/man_obs.npy')
                    diffed = observation - last_ob[0]
                    lag = numpy.append(lag[1:], [diffed], axis=0)
                    numpy.save('../Model_Info/man_data.npy', lag)
                    # update and save real observation
                    last_ob[0] = observation
                    numpy.save('../Model_Info/man_obs.npy', last_ob)

                
                yhat_list.append(yhat)


            # In[13]:

            for cancer in cancers:
                if len(cancer) > 6:
                    index = range(len(cancer))
                    series = pd.Series(cancer, index = index)  
                    ar_data(series)
                    predict(series)   


            for p in range (0, len(yhat_list)):
                cancers[p]= pd.Series(cancers[p])
                yhat_list[p]= pd.Series(yhat_list[p])
                cancers[p]= cancers[p].append(yhat_list[p])
                cancers[p].reset_index()
                

            years = pd.Series(choice_df.Year.unique())
            prediction_X = pd.Series(prediction_X)
            years = years.append(prediction_X)
            years=years.values
            
            print(sexlist[i], racelist[j],statelist[k])

            if len(cancers[0]) == len(years):
                lung_with_predict = pd.DataFrame({"Year": years, "Lung": cancers[0]})
                lung_with_predict[lung_with_predict<0]=0
                lung_with_predict["State"] = statelist[k]
                lung_with_predict.to_csv("../Data/Data " + str(statelist[k]) + str(racelist[j]) + str(sexlist[i]) + "LUNG.csv",",")

            if len(cancers[1]) == len(years):
                larynx_with_predict = pd.DataFrame({"Year": years, "Larynx": cancers[1]})
                larynx_with_predict[larynx_with_predict<0]=0
                larynx_with_predict["State"] = statelist[k]
                larynx_with_predict.to_csv("../Data/Data " + str(statelist[k]) + str(racelist[j]) + str(sexlist[i]) + "larynx.csv",",")

            if len(cancers[2]) == len(years):
                nasal_with_predict = pd.DataFrame({"Year": years, "Nasal": cancers[2]})
                nasal_with_predict[nasal_with_predict<0]=0
                nasal_with_predict["State"] = statelist[k]
                nasal_with_predict.to_csv("../Data/Data " + str(statelist[k]) + str(racelist[j]) + str(sexlist[i]) + "Nasal.csv",",")

            if len(cancers[3]) == len(years):
                trachea_with_predict = pd.DataFrame({"Year": years, "Trachea": cancers[3]})
                trachea_with_predict[trachea_with_predict<0]=0
                trachea_with_predict["State"] = statelist[k]
                trachea_with_predict.to_csv("../Data/Data " + str(statelist[k]) + str(racelist[j]) + str(sexlist[i]) + "Trach.csv",",")    

           

                

                   
            # data_with_predi
            # lung_with_predict.to_csv("../Data/Data " + str(statelist[k]) + str(racelist[j]) + str(sexlist[i]) + "LUNG.csv","w")   