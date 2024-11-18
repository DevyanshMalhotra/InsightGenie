from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model and tokenizer
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_response_with_context(entity, query_template, search_results):
    """
    Generate a response using Hugging Face Transformers, focusing on the query entity.
    """
    try:
        # Construct a focused prompt for the specific entity
        prompt = (
            f"You are tasked with extracting information for the entity '{entity}'.\n"
            f"Query: {query_template}\n"
            f"Search Results: {search_results}\n\n"
            f"Provide a concise and accurate response related to '{entity}'."
        )

        # Encode the prompt and generate a response
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        output_ids = model.generate(input_ids, max_length=150, num_beams=5, early_stopping=True)

        # Decode the response
        response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        return response
    except Exception as e:
        return f"Error generating response: {e}"
