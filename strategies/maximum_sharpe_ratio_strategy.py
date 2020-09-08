# Basic libraries
import os
import ta
import sys
import json
import math
import pickle
import random
import requests
import collections
import numpy as np
from os import walk
import pandas as pd
import yfinance as yf
import datetime as dt
from tqdm import tqdm
from scipy.stats import linregress
from datetime import datetime, timedelta
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

class MaximumSharpeRatioStrategy:
	def __init__(self):
		print("Maximum sharpe ratio strategy has been created")
		
	def generate_portfolio(self, symbols, covariance_matrix, returns_vector):
		"""
		Inspired by: Eigen Portfolio Selection: A Robust Approach to Sharpe Ratio Maximization, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3070416
		"""
		inverse_cov_matrix = np.linalg.pinv(covariance_matrix)
		ones = np.ones(len(inverse_cov_matrix))

		numerator = np.dot(inverse_cov_matrix, returns_vector)
		denominator = np.dot(np.dot(ones.transpose(), inverse_cov_matrix), returns_vector)
		msr_portfolio_weights = numerator / denominator
		
		portfolio_weights_dictionary = dict([(symbols[x], msr_portfolio_weights[x]) for x in range(0, len(msr_portfolio_weights))])
		return portfolio_weights_dictionary