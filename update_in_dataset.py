# Re-import necessary libraries due to reset
import pandas as pd
from textblob import TextBlob
import random
# Load the re-uploaded dataset
file_path = 'dummy_survey_data_with_timeline.csv'
data = pd.read_csv(file_path)

# Preview the structure to ensure correct loading
data.head(), data.columns



# Generate a fixed list of unique responses for each question
def generate_unique_responses(question_type):
    if question_type == "challenge":
        return [
            "Unemployment among the youth is alarming.",
            "Access to quality education is a significant concern.",
            "Healthcare in rural areas is inadequate.",
            "Environmental degradation is becoming a crisis.",
            "Corruption is still pervasive in many sectors.",
            "Rising inflation is affecting middle-class families heavily.",
            "Women safety and empowerment need more focus.",
            "The lack of job security in the gig economy is troubling.",
            "Poverty alleviation programs are not reaching the grassroots.",
            "Digital literacy is critical for inclusive growth.",
            "Agriculture reforms are needed for farmer sustainability.",
            "Transportation infrastructure needs massive upgrades.",
            "Tax reforms should be simplified for small businesses.",
            "Skilled labor training is insufficient to meet industry demands.",
            "Judicial delays are denying timely justice.",
            "The divide between urban and rural areas is widening.",
            "Water scarcity is a growing challenge in arid regions.",
            "Public housing availability is still very low.",
            "The disparity in healthcare costs is concerning.",
            "Accessibility for the differently-abled is often ignored."
        ]
    elif question_type == "performance":
        return [
            "The infrastructure development has been remarkable.",
            "Healthcare schemes are ambitious but lack execution.",
            "Education initiatives are underfunded and overlooked.",
            "Economic growth is visible, but inflation persists.",
            "Policy implementation varies significantly by state.",
            "The push for renewable energy is commendable.",
            "Efforts on poverty alleviation show mixed results.",
            "Defense upgrades are a good move, but expensive.",
            "Social harmony remains a challenge for this government.",
            "Ease of doing business has improved visibly.",
            "Corruption scandals are less frequent but not eradicated.",
            "Employment generation has not kept up with promises.",
            "Technology integration in governance is appreciated.",
            "The crackdown on black money is partially effective.",
            "Global relations have strengthened under this government.",
            "Support for startups has been promising.",
            "Environmental conservation is not getting due priority.",
            "Budget allocations favor the wealthy over the poor.",
            "Skill development initiatives are showing results slowly.",
            "Public transport systems have improved drastically."
        ]
    elif question_type == "modi":
        return [
            "His leadership is visionary but divisive at times.",
            "Modi has brought India global recognition like never before.",
            "His communication skills are his strongest asset.",
            "Economic policies under him are bold but risky.",
            "He has a strong focus on national security.",
            "His governance style is centralized but effective.",
            "Social welfare programs have expanded under his tenure.",
            "There is a clear gap between his vision and execution.",
            "Modi's charisma has inspired millions across the nation.",
            "His policies have been harsh on small businesses.",
            "The Make in India initiative is gaining traction.",
            "Digital India is one of his landmark achievements.",
            "He has a polarizing effect on the electorate.",
            "His reforms are long-term but challenging in the short term.",
            "The focus on infrastructure is highly appreciated.",
            "Criticism on freedom of speech has grown under his tenure.",
            "His ability to connect with the masses is unmatched.",
            "The handling of economic crises is his weak point.",
            "Agricultural reforms under him are controversial but necessary.",
            "He has set a high bar for future leadership."
        ]

# Apply unique responses to each question
data["What do you think is the most important challenge facing the country today?"] = [
    random.choice(generate_unique_responses("challenge")) for _ in range(len(data))
]

data["Share your thoughts on the current government's performance."] = [
    random.choice(generate_unique_responses("performance")) for _ in range(len(data))
]

data["What is your opinion on Narendra Modi's leadership?"] = [
    random.choice(generate_unique_responses("modi")) for _ in range(len(data))
]

# Preview updated dataset
data[["What do you think is the most important challenge facing the country today?",
      "Share your thoughts on the current government's performance.",
      "What is your opinion on Narendra Modi's leadership?"]].head()


# Save the updated dataset to a new file
updated_file_path = "updated_survey_data.csv"
data.to_csv(updated_file_path, index=False)