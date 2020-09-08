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

class EigenPortfolioStrategy:
	def __init__(self):
		print("Eigen portfolio strategy has been created")
		
	def generate_portfolio(self, symbols, covariance_matrix, eigen_portfolio_number):
		"""
		Inspired by: https://srome.github.io/Eigenvesting-I-Linear-Algebra-Can-Help-You-Choose-Your-Stock-Portfolio/
		"""
		eig_values, eig_vectors = np.linalg.eigh(covariance_matrix)
		market_eigen_portfolio = eig_vectors[:,-1] / np.sum(eig_vectors[:,-1]) # We don't need this but in case someone wants to analyze
		eigen_portfolio = eig_vectors[:,-eigen_portfolio_number] / np.sum(eig_vectors[:,-eigen_portfolio_number]) # This is a portfolio that is uncorrelated to market and still yields good returns

		portfolio_weights_dictionary = dict([(symbols[x], eigen_portfolio[x]) for x in range(0, len(eigen_portfolio))])
		return portfolio_weights_dictionary
