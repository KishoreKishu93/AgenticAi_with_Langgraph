from langgraph.graph import StateGraph, END, START, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.prompts import ChatPromptTemplate
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.chat_bot_node import ChatBotNode

class GraphBuilder:

    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def chat_bot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `ChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """
        self.chatbot_node = ChatBotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)


    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.chat_bot_build_graph()    
        return self.graph_builder.compile()    

