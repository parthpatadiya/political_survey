import random
import csv
from datetime import datetime, timedelta

# Extracted questions and options from the PDF
def get_questions_and_options():
    return [
        ("Were you able to vote in the recent Lok Sabha election?", ["Not able to vote", "Able to vote"]),
        ("When did you decide whom to vote for?", ["On the day of voting", "A day or two before voting", "During the campaign", "After announcement of candidates", "Even before announcement of candidates", "No response"]),
        ("What mattered more to you in this election – party or candidate?", ["Party", "Candidate", "PM candidate", "No response"]),
        ("Which party do you prefer overall?", ["BJP", "AAP", "INC", "BSP", "Not sure"]),
        ("Did you vote for this party because you really wanted to or due to lack of alternatives?", ["Really wanted to vote", "No good alternative", "No response"]),
        ("Whose opinion mattered the most while deciding whom to vote for?", ["No one, I voted on my own", "Family member", "Caste/community leader", "Religious leader", "Friends/neighbors", "Local political leader", "Other", "Don’t know"]),
        ("Why were you not able to vote in the recent Lok Sabha election?", ["Was not in village/city", "Was ill", "Did not feel like voting", "Did not have necessary documents", "Other", "No response"]),
        ("How interested were you in the election campaign this time?", ["Great deal", "Somewhat", "Not at all", "No response"]),
        ("Were you or a family member contacted by political parties through phone or social media?", ["Yes", "No", "Don’t know", "Did not respond"]),
        ("As compared to five years ago, how is the economic condition of your household today?", ["Much better", "Better", "Remained same", "Worse", "Much worse", "No response"]),
        ("Rate the effectiveness of the recent government policies (1 to 5)", ["1", "2", "3", "4", "5"]),
        ("What is your top issue for this election?", ["Economy", "Healthcare", "Education", "National Security", "Other"]),
        ("Do you think the government is handling inflation effectively?", ["Yes", "No", "Not sure"]),
        ("Has your trust in the judiciary improved over the last five years?", ["Yes", "No"]),
        ("Did a candidate or party member visit your house to ask for your vote?", ["Yes", "No", "Don’t know"]),
        ("How satisfied are you with the BJP-led NDA government’s performance over the last five years? Rate (1 to 5)",["1", "2", "3", "4", "5"]),
        ("Which government work in the last five years did you like the most?",["Employment opportunities", "Reducing poverty", "Improving infrastructure", "Global image", "Modi’s leadership", "Other", "No response"]),
        ("Do you think regular change of government promotes development?", ["Statement 1: Promotes development", "Statement 2: Important for the same party to remain", "No response"]),
        ("What is your opinion on the most suitable Prime Ministerial candidate?", ["Rahul Gandhi", "Narendra Modi", "Priyanka Gandhi", "Arvind Kejriwal", "Other", "No response"])
    ]

# Generate fake respondents
def generate_respondent():
    first_names = [
        "Aarav", "Vivaan", "Aditya", "Aryan", "Kabir", "Arjun", "Rohan", "Rahul", "Siddharth", "Kunal","Asha", "Vidya", "Anjali", "Sneha","Amit","Raj","Ravi","Suresh","Rajesh",
        "Ananya", "Aditi", "Ishita", "Meera", "Kavya", "Nisha", "Riya", "Simran", "Priya", "Pooja","sumit","sandeep","sachin","sagar","sahil","saurabh","sushant","sushil"
    ]
    last_names = [
        "Sharma", "Verma", "Gupta", "Singh", "Patel", "Chopra", "Mehta", "Malhotra", "Das", "Iyer","Kumar", "Gupta","Patil", 
        "Bose", "Reddy", "Nair", "Saxena", "Agarwal", "Joshi", "Pandey", "Mishra", "Ghosh", "Bhatia","yadav","ansari","khan"
    ]

    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    age = random.randint(18, 60)
    gender = random.choice(["Male", "Female", "Non-binary"])
    location = random.choice(["Urban", "Suburban", "Rural"])

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "location": location
    }

# Generate survey data with optional year tracking
def generate_survey_data(num_respondents, start_year=2020, end_year=2025):
    respondents = [generate_respondent() for _ in range(num_respondents)]
    questions_and_options = get_questions_and_options()
    years = [start_year + i for i in range(end_year - start_year + 1)]

    data = []
    for respondent in respondents:
        for year in years:
            answers = {
                question: random.choice(options) if options else "Free text response" for question, options in questions_and_options
            }
            answers.update({"year": year})
            data.append({**respondent, **answers})

    return data

# Save data to CSV
def save_to_csv(filename, data):
    fieldnames = ["name", "age", "gender", "location", "year"] + [question for question, _ in get_questions_and_options()]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Generate and save the dataset
survey_data = generate_survey_data(1000)
save_to_csv("dummy_survey_data_with_timeline.csv", survey_data)
print("Dummy survey data with yearly timeline for 1000 respondents has been saved to 'dummy_survey_data_with_timeline.csv'.")
