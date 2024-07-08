import pandas as pd
from transformers import pipeline

# Load the Excel file
file_path = 'formatted_assets_details.xlsx'
data = pd.read_excel(file_path)

# Load a lightweight model
# Extract keywords from the first row (column headers) and first column (detail keys)
chatbot = pipeline("text-generation", model="gpt2")

# Extract keywords from the first row (column headers) and first column (detail keys)
# Extract keywords from the first row (column headers) and first column (detail keys)
column_keywords = list(data.columns)
detail_key_keywords = data.iloc[:, 0].dropna().tolist()

def preprocess_query(query):
    # Convert query to lowercase for case-insensitive matching
    query_lower = query.lower()
    # Remove common words to focus on keywords
    common_words = ["what", "is", "the", "of", "and", "in", "on"]
    query_words = query_lower.split()
    query_keywords = [word for word in query_words if word not in common_words]
    return " ".join(query_keywords)

def respond_to_query(query, data):
    query_keywords = preprocess_query(query)
    response = "I couldn't find an exact match in the data."
    
    # Check if the query matches any column keyword
    for col in column_keywords:
        if any(keyword in col.lower() for keyword in query_keywords.split()):
            matches = data[data[col].astype(str).str.contains("|".join(query_keywords.split()), case=False, na=False)]
            if not matches.empty:
                response_data = matches.to_dict(orient='records')
                response = f"Here is what I found for '{query}': {response_data}"
                return response
    
    # Check if the query matches any detail key keyword
    for key in detail_key_keywords:
        if any(keyword in key.lower() for keyword in query_keywords.split()):
            matches = data[data.iloc[:, 0].astype(str).str.contains("|".join(query_keywords.split()), case=False, na=False)]
            if not matches.empty:
                response_data = matches.to_dict(orient='records')
                response = f"Here is what I found for '{query}': {response_data}"
                return response
    
    return response

def chat_with_bot():
    print("Welcome to the 'Talk to Your File' chatbot! Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = respond_to_query(user_input, data)
        print("Bot:", response)

# Start the chatbot
chat_with_bot()