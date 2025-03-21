from typing_extensions import TypedDict
import random
from typing import Literal
from IPython.display import display, Image
from langgraph.graph import StateGraph, START, END

# define the state
class State(TypedDict):
    graph_state: str

# define nodes
def node_1(state):
    print("--Node 1--")
    return {"graph_state": state['graph_state'] + "I am"}

def node_2(state):
    print("--Node 2--")
    return {"graph_state": state['graph_state'] + " Happy!"}

def node_3(state):
    print("--Node 3--")
    return {"graph_state": state['graph_state'] + " Sad:(("}

# define edges
def decide_mood(state) -> Literal["node_2", "node_3"]:

    user_input = state['graph_state']

    # 50% time return node_2
    if random.random() < 0.5:

        return "node_2"
    
    return "node_3"

#build graph
builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

#logic
builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

#add
graph = builder.compile()


# View
# display(Image(graph.get_graph().draw_mermaid())) ## if you are running in jupyter notebook
print(graph.get_graph().draw_mermaid())

graph.invoke({"graph_state" : "Hi, this is hrithik."})
