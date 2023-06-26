# Importing the important library.
from dotenv import load_dotenv
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()

hub_llm = HuggingFaceHub(
    repo_id="google/flan-t5-base",
    model_kwargs={'temperature': 0.7, 'max_length': 100}
)

# Creating prompt for the input and output.
prompt = PromptTemplate(
    input_variables=["profession"],
    template="you had one job ! 😠 you're the {profession} and you didn't have to be sarcastic."
)

hub_chain = LLMChain(prompt=prompt, llm=hub_llm, verbose=True)

# Generate responses for different professions
response1 = hub_chain.run("customer services agent")
response2 = hub_chain.run("politician")
response3 = hub_chain.run("Fintech")
response4 = hub_chain.run("Insurance agent")

# Your additional code goes here
# Write your code to perform further actions or process the generated responses
# based on your specific requirements.

# For example, you can print the generated responses:
print("Response 1:", response1)
print("Response 2:", response2)
print("Response 3:", response3)
print("Response 4:", response4)

# Or you can save the responses to a file:
with open("responses.txt", "w") as file:
    file.write("Response 1:\n" + response1 + "\n")
    file.write("Response 2:\n" + response2 + "\n")
    file.write("Response 3:\n" + response3 + "\n")
    file.write("Response 4:\n" + response4 + "\n")

# You can further process the responses or perform any other necessary operations based on your requirements.

