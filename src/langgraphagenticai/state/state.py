from typing import List, Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class State(TypedDict):
    """Represent the structure of the state used in the graph.

    Use the key name `messages` (plural) because nodes and UI expect
    a `messages` field. The `add_messages` validator from langgraph is
    applied to validate the list of messages.
    """

    messages: Annotated[List, add_messages]


