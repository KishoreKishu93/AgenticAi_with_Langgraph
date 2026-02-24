from typing import Annotated,Literal,Optional
from typing_extensions import TypedDict, List
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, AIMessage

class State(TypedDict):
    """
    Represents the structure of the state used in the graph
    """
    messages : Annotated[List, add_messages]
