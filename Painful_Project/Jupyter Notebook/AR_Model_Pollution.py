data_predict_list = []
statelist = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI',
       'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI',
       'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV',
       'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX',
       'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

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



for i in range (0, len(statelist)):


    #!/usr/bin/env python
    # coding: utf-8

    # In[1]:


  
    yhat_list = []   

    choice = "../Data/pollution.csv"
    state= statelist[i]

    choice_df = pd.read_csv(choice)

    choice_df= choice_df.fillna(0)
    
    index = choice_df.Year.unique()
    CO = choice_df[choice_df['State']==state]["CO"].values
    NO2 = choice_df[choice_df['State']==state]["NO2"].values
    Ozone = choice_df[choice_df['State']==state]["Ozone"].values
    SO2 = choice_df[choice_df['State']==state]["SO2"].values
    Lead = choice_df[choice_df['State']==state]["Lead"].values
    PM10 = choice_df[choice_df['State']==state]["PM10"].values
    PM2_5 = choice_df[choice_df['State']==state]["PM2.5"].values
    
    pollution = [CO, NO2, Ozone, SO2, Lead, PM10, PM2_5]
    prediction_X = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]



    # def model_plots(series):
        
    #     # create a difference transform of the dataset
    #     def difference(dataset):
    #         diff = list()
    #         for i in range(1, len(dataset)):
    #             value = dataset[i] - dataset[i - 1]
    #             diff.append(value)
    #         return numpy.array(diff)

    #     # Make a prediction give regression coefficients and lag obs
    #     def predict(coef, history):
    #         yhat = coef[0]
    #         for i in range(1, len(coef)):
    #             yhat += coef[i] * history[-i]
    #         return yhat


    #     # split dataset
    #     X = difference(series.values)
    #     size = int(len(X) * 0.80)
    #     train, test = X[0:size], X[size:]
    #     # train autoregression
    #     model = AR(train)
    #     model_fit = model.fit(maxlag=3, disp=True)
    #     window = model_fit.k_ar
    #     coef = model_fit.params
    #     # walk forward over time steps in test
    #     history = [train[i] for i in range(len(train))]
    #     predictions = list()
    #     for t in range(len(test)):
    #         yhat = predict(coef, history)
    #         obs = test[t]
    #         predictions.append(yhat)
    #         history.append(obs)
    #     error = mean_squared_error(test, predictions)
    #     print('Test MSE: %.3f' % error)
    #     # plot
        


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
        model_fit = model.fit(maxlag=3, disp=False)
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
        window_size = 3
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

        
        yhat = []
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

    
    for j, poll in enumerate(pollution):
        
        print(f'poll {j}, statelist {i}: {len(poll)}')
        series = pd.Series(poll, index = index)
        ar_data(series)
        predict(series)
        

    for k in range(0, len(pollution)):
        pollution[k]= pd.Series(pollution[k])
        yhat_list[k]= pd.Series(yhat_list[k])
        pollution[k]= pollution[k].append(yhat_list[k])
        


    # In[16]:


    years = pd.Series(index)
    prediction_X = pd.Series(prediction_X)
    years = years.append(prediction_X)
    years=years.values


    # In[17]:




    # In[18]:


    data_predict = pd.DataFrame({"Year": years, "CO": pollution[0], "NO2":pollution[1], "Ozone":pollution[2], "SO2":pollution[3], "Lead": pollution[4], "PM10":pollution[5], "PM2_5":pollution[6]})


    # In[19]:


    data_predict


    # In[20]:


    data_predict[data_predict<0] = 0
    

    data_predict["State"] = statelist[i]
    # In[21]:


    data_predict_list.append(data_predict)


    # print(statelist[i])
for l in range (0, len(data_predict_list)):
    data_predict_list[l].to_csv("../Data/To_merge_pollution/Pollution" + str(statelist[l]) + ".csv",",")
