# Importing the important library.


from dotenv import load_dotenv
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()

hub_llm=HuggingFaceHub(

    repo_id="anon8231489123/vicuna-13b-GPTQ-4bit-128g",
    model_kwargs={'temperature':0.7, 'max_length':100}
                       )

# Creating prompt for the input and output.

prompt=PromptTemplate(

    input_variables=["profession"],

    template="you had one job ! 😠 you're the {profession} and you didn't have to be sarcastic."

)



hub_chain=LLMChain(prompt=prompt,llm=hub_llm,verbose=True)

# printing
print(hub_chain.run(" customer services agent"))
print(hub_chain.run("politican"))
print(hub_chain.run("Fintech"))
print(hub_chain.run("Insureance agent"))

