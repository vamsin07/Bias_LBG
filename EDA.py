import pandas as pd
from pydantic_settings import BaseSettings

from pandas_profiling import ProfileReport

df = pd.read_csv('Participant_data.csv')

profile = ProfileReport(df)

profile.to_file("report.html")