#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install transformers torch


# In[ ]:


from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
model_name = 'gpt2'  # You can use 'gpt2-medium', 'gpt2-large', etc. for larger models
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def predict_next_word(text, top_k=5):
    # Encode input text
    inputs = tokenizer.encode(text, return_tensors='pt')
    
    # Get model predictions
    outputs = model(inputs, labels=inputs)
    predictions = outputs.logits

    # Get the predicted next token
    next_token_logits = predictions[0, -1, :]
    top_k_tokens = next_token_logits.topk(top_k).indices

    # Decode the top-k tokens to words
    predicted_words = [tokenizer.decode(token.item()).strip() for token in top_k_tokens]
    return predicted_words

# Example usage
input_text = "The quick brown fox jumps"
predicted_words = predict_next_word(input_text, top_k=5)
print(f"Input text: '{input_text}'")
print("Predicted next words:", predicted_words)

