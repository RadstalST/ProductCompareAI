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
    Output should be a table with product as header and features as rows and output will be in markdown format.
    Example:
    | Features | Product A | Product B |
    | -------- | --------- | --------- |
    | Feature1 |           |           |
    | Feature2 |           |           |
    | Feature3 |           |           |
    | Feature4 |           |           |
    | Price    |    122USD |    123USD |
    """
)

execute_specific_feature = PromptTemplate(
    input_variables=["input","chat_history"],
    template="""
    Make a comparison between two products based on 
    {chat_history}
    {input}
    Output should be a short summary of the feature asked to be compare.
    
	"""
)

pros_cons_compare = PromptTemplate(
    input_variables=["input","chat_history"],
    template="""Discuss the pros and cons of the given topic based on the chat history:
    Topic: 
    {chat_history}
    {input}
    Pros:
    - 

    Cons:
    - 
"""
)


title_prompt = PromptTemplate(
    input_variables=["topic", "chat_history"], # input = product name vs product name prompt
    template="""
    topic: {topic}
    Make a clickbait title for the topic
    based on:
    {chat_history}
    """
)

plan_review_product1 = PromptTemplate(
    input_variables=["input"],
    template="""Prepare plan for task execution. (e.g. retrieve current date to find weather forecast)
    base on:
    {input}
    things to keep in mind:
    1. Access customer reviews website such as amazon.com, facebook.com

    most of the time you will need to:
    1. search for descriptive reviews on website
    2. Retrieve the customer reviews with excerpts or quotes from actual reviews
	Tools to use:+""" + tools_str + """
	REMEMBER: Keep in mind that you don't have information about current date, temperature, informations after September 2021. Because of that you need to use tools to find them.

        Output look like this:
    '''
        Product: {input}
        Top reviews: [summary review of product]
    """)

plan_review_product = PromptTemplate(
    input_variables=["input"],
    template="""
    Your Objective is to find customer reviews based on {input}
    Instructions:
    1. Access customer reviews on website such as amazon.com
    2. Search for descriptive reviews of product on website
    3. Summarize key sentiment of customer about the product
    Tools to use:+""" + tools_str+ """
    REMEMBER: 
        1.Keep in mind that you don't have information about current date, temperature, informations after September 2021. Because of that you need to use tools to find them.
        2. You do not need to make purchase decisions.


        Output look like this:
		'''
		Product:{input}
		Reviews: [Summary reviews of product]
	"""
)

introduction_prompt = PromptTemplate(
    input_variables=["title", "chat_history"],
    template="""
    title: {title}
    Write an introduction paragraph for the title.
    based on:
    {chat_history}
    """
)

vs_paragraph_prompt = PromptTemplate(
    input_variables=["topic", "chat_history"],
    template="""
    topic: {topic}
    comparison paragraphs for the topic for each product features in the table in markdown format.

    Example:
    1. **Feature1**

    paragraph comparing Feature1 between product A and product B

    2. ....
    ...
    3. ....
    based on:
    {chat_history}
    """
)




consider_budget_prompt = PromptTemplate(
    input_variables=["budget", "chat_history"],
    template = """
    budget: {budget}
    Please compare Product A and Product B based on their features, quality, and price.
    What is the price of Product A and Product B? Which product is within my budget, and which one exceeds it?
    If one product exceeds my budget, please provide the reason for going over budget. What features or qualities justify the higher price? Can you highlight any specific advantages or additional benefits of the product that might justify going over budget?
    based on:
    {chat_history}
    """
)