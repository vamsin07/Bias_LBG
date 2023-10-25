import pandas as pd
''' race : 1 -: White
           2 -: Black or African American
           3-: Asian
           4-: American Indian or Alaskan Native
           5-: Native Hawaiian or Other Pacific Islander
           6-: More than 1 race
           7-: participant refused to answer
           95-: Missing data form - form is not expected to be completed
           96-: Missing no response
           98-: Missing - form was submitted and the answer was left blank
           99-: Unknown/declined to answer'''


df = pd.read_csv('Participant_data.csv')

desired_column = df['race']

value_counts = desired_column.value_counts()

print(value_counts)