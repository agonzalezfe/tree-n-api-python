from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from model.n_tree import NaryTree

app = FastAPI()
tree = NaryTree()

class NodeData(BaseModel):
    data: str
    parent_data: Optional[str] = None
@app.post("/nodes/")
def add_node(node_data: NodeData):
    # verify if already exists
    if any(node.data == node_data.data for node in tree.nodes):
        raise HTTPException(status_code=400, detail="Node with this data already exists.")

    # try adding the node
    try:
        new_node = tree.add_node(node_data.data, node_data.parent_data)
        return {"data": new_node.data, "parent": new_node.parent.data if new_node.parent else None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/nodes/")
def get_tree():
    # show the tree
    return tree.display()
