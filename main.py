from langchain_ollama.llms import OllamaLLM # allows you to use the ollama model
from langchain_core.prompts import ChatPromptTemplate # allows you to use the chat prompt template

model = OllamaLLM(model="gemma3") # loads the gemma3 model from ollama

# Define the template for the prompt
template = """ 
You are an British CCIE expert in the cisco networking field.
You are given a question and you need to answer it in a detailed manner. 
The question is: {question}
"""

# CReates a chat prompt using the template above, where the template is used to format the input for the model
prompt = ChatPromptTemplate.from_template(template)

# Chains the prompt and the model together allowing for the prompt to be used as input for the model
chain = prompt | model

#While loop to keep allow users to keep asking questions to the model on cisco networking
while True:
    print("\n\n")
    question = input("Enter your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    result = chain.invoke({'question': question}) # invokes the chain with the question, where question input will be fed back to the placeholder in the template
    print(result)