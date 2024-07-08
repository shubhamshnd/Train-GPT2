from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the fine-tuned model
model_path = "gpt2-finetuned"
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

def generate_answer(question):
    input_text = f"Question: {question} Answer:"
    inputs = tokenizer.encode_plus(input_text, return_tensors='pt', padding=True, truncation=True)
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']
    
    output = model.generate(input_ids, attention_mask=attention_mask, max_length=150, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    return answer.split("Answer:")[1].strip()

def chat_with_bot():
    print("Welcome to the 'Talk to Your File' chatbot! Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = generate_answer(user_input)
        print("Bot:", response)


chat_with_bot()
