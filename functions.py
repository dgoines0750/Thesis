#!/usr/bin/python

import numpy as np
import math

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def contingency_func(obs, model, threshold):
    """
    Calculates contingency table elements and Equitable Threat Score (ETS)
    """
    # boolean arrays based on threshold
    obs[obs < threshold]=0
    obs[obs >= threshold]=1
    model[model < threshold]=0
    model[model >= threshold]=1

    model_analyze = model + obs

    forecast_points = float((model==1).sum())
    obs_points = float((obs==1).sum())
    num_points = float((obs>=(-float("inf"))).sum())
    correct_forecast = float((model_analyze==2).sum())

    return (forecast_points, obs_points, num_points, CFA)
    
  
