from ollama import Client


system_prompt = "You are a helpful assistant that provides restaurant recommendations based on user queries. Please ensure your responses are well formatted and include the restaurant name, address, and a brief description."

def get_recommendation(question):
    url = "http://localhost:8000"
    headers = {"Content-Type": "application/json"}
    client = Client(host=url, headers=headers)

    response = client.chat(model='llama3.2:1b', messages=[
                            {
                                "role":"system","content": system_prompt},
                            {
                                "role":"user","content": question 
                            }
                            ])

    return response['message']['content']
    

# if __name__ == "__main__":
#     question = "What is a good restaurant nearby?"
#     recommendation = get_recommendation(question)
#     print(recommendation)