import pandas as pd
import seaborn as sns

insurance = pd.read_csv('./data/insurance.csv')

insurance.head()

insurance.info()

insurance.describe()
