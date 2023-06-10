from langchain.agents import AgentType, Tool, initialize_agent
from langchain.tools import DuckDuckGoSearchRun
from langchain.utilities import WikipediaAPIWrapper




class Tools():
    def __init__(self):
        self.tools_engine = {
            "Web Search": DuckDuckGoSearchRun(),
            "Wikipedia": WikipediaAPIWrapper(),
        }

        self.tools = [
            Tool(
                name="Web Search",
                func=self.tools_engine["Web Search"].run,
                description="A web search tool is a software application or service that enables users to search for information on the internet. It is valuable for swiftly accessing a vast array of data and is widely used for research, learning, entertainment, and staying informed. With features like filters and personalized recommendations, users can easily find relevant results. However, web search tools may struggle with complex or specialized queries that require expert knowledge and can sometimes deliver biased or unreliable information. It is crucial for users to critically evaluate and verify the information obtained through web search tools, particularly for sensitive or critical topics.",
            ),Tool(
                name="Wikipedia",
                func=self.tools_engine["Wikipedia"].run,
                description="Wikipedia is an online encyclopedia that serves as a valuable web search tool. It is a collaborative platform where users can create and edit articles on various topics. Wikipedia provides a wealth of information on a wide range of subjects, making it a go-to resource for general knowledge and background information. It is particularly useful for getting an overview of a topic, understanding basic concepts, or exploring historical events. However, since anyone can contribute to Wikipedia, the accuracy and reliability of its articles can vary. It is recommended to cross-reference information found on Wikipedia with other reliable sources, especially for more specialized or controversial subjects.",
            )

        ]

    def get_tools(self):
        return self.tools
    

    
