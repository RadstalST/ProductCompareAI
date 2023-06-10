# import langchain prompttemplate

from langchain import PromptTemplate

plan_prompt = PromptTemplate(
    input_variables=["input", "chat_history"],
    template="""Prepare plan for task execution. (e.g. retrieve current date to find weather forecast)

    things to keep in mind:
    1. the yask will be about finding 2 products on the internet and comparing them

    most of the time you will need to:
    1. you need to find the features of the products
    2. you need to compare them based on the features
    3. analyse relevant customer reviews
    
    Tools to use: wikipedia, web search

    REMEMBER: Keep in mind that you don't have information about current date, temperature, informations after September 2021. Because of that you need to use tools to find them.

    Task: {input}

    History: {chat_history}

    Output look like this:
    '''
        Question: {input}

        Execution plan: [execution_plan]

        Rest of needed information: [rest_of_needed_information]
    '''

    IMPORTANT: if there is no question, or plan is not need (YOU HAVE TO DECIDE!), just populate {input} (pass it as a result). Then output should look like this:
    '''
        input: {input}
    '''
    """,
)

prompt = PromptTemplate(
    template="""Plan: {input}

History: {chat_history}

Let's think about answer step by step.
If it's information retrieval task, solve it like a market research and content creator.""",
    input_variables=["input", "chat_history"],
)

