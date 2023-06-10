# import langchain prompttemplate

from langchain import PromptTemplate
from AI.tools import Tools
tools_str = ",".join(list(Tools().tools_engine.keys()))
plan_prompt = PromptTemplate(
    input_variables=["input", "chat_history"],
    template="""Prepare plan for task execution. (e.g. retrieve current date to find weather forecast)

    things to keep in mind:
    1. the task will be about finding 2 products on the internet and comparing them

    most of the time you will need to:
    1. you need to find the features of each products
    2. you need to find what each feature means
    2. you need to compare them based on the features
    3. analyse relevant customer reviews
    
    Tools to use:+""" + tools_str + """

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
plan_features_compare = PromptTemplate(
    input_variables=["input","chat_history"],
    template="""Prepare plan for task execution. (e.g. retrieve current date to find weather forecast)
    base on:
    {input}
    things to keep in mind:
    1. the task will be about comparing 2 product features 

    most of the time you will need to:
    1. you need to find the features of each products
    2. you need to find what each feature means
    3. you need to compare them based on the features
    4. provide enough information to make a comparison table
    
    Tools to use:+""" + tools_str + """

    REMEMBER: Keep in mind that you don't have information about current date, temperature, informations after September 2021. Because of that you need to use tools to find them.

    History: {chat_history}

    Output look like this:
    '''
        Product: {input}

        Execution plan: [execution_plan]

        Rest of needed information: [rest_of_needed_information]
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

execute_features_compare = PromptTemplate(
    input_variables=["input","chat_history"],
    template="""
    Make a comparison table of features of two products based on
    {chat_history}
    {input}
    Output should be able to feed directly into json.loads() and to pd.DataFrame() function:
    '''
        <open_bracket_token>
            "product": [product A, product B,...],
            "eg. screen size": [10, 12,...],
            "features_2": [comparison A, comaprison B,...],
            "features_n-1": [comparison A, comaprison B,...],
            "features_n": [comparison A, comaprison B,...],
        <close_bracket_token>
    '''

    """
)



