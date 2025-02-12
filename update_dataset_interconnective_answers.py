import pandas as pd
from textblob import TextBlob
import random
# Load the re-uploaded dataset
file_path = 'updated_survey_data.csv'
data = pd.read_csv(file_path)


# Ensure consistency for interconnected questions

# Rule 1: If "Which party do you prefer overall?" is BJP, then "What is your opinion on the most suitable Prime Ministerial candidate?" should be Narendra Modi
data.loc[data["Which party do you prefer overall?"] == "BJP", 
         "What is your opinion on the most suitable Prime Ministerial candidate?"] = "Narendra Modi"

data.loc[data["Which party do you prefer overall?"] == "AAP", 
         "What is your opinion on the most suitable Prime Ministerial candidate?"] = "Arvind Kejriwal"


# Rule 2: If "Were you able to vote in the recent Lok Sabha election?" is "Able to vote",
# then "Why were you not able to vote in the recent Lok Sabha election?" should be "No response"
data.loc[data["Were you able to vote in the recent Lok Sabha election?"] == "Able to vote", 
         "Why were you not able to vote in the recent Lok Sabha election?"] = "No response"




# Save the updated dataset to a new file
updated_file_path = "updated_survey_data.csv"
data.to_csv(updated_file_path, index=False)