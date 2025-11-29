import os
from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from config.diagram_node_types import NODE_TYPES

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(os.path.dirname(BASE_DIR), "assets")

def get_valid_node_types():
    return list(NODE_TYPES.keys())

def generate_diagram(model, project_identifier: str, output_path="docs/Identifier_architecture_diagram.png", ):
    """
    Generates an architecture diagram using the `diagrams` library and saves it as a PNG.

    Args:
        model (dict): Architecture model following the structure. Example:
        model = {
            "nodes": [
                {"name": "Frontend", "type": "User"},
                {"name": "Game API", "type": "Nginx"},
                {"name": "MongoDB", "type": "MongoDB"},
            ],
            "connections": [
                {"from": "Frontend", "to": "Game API"},
                {"from": "Game API", "to": "MongoDB"},
            ],
            "clusters": [
                {"name": "Backend Services", "nodes": ["Game API", "MongoDB"]}
            ]
        }
        
        - nodes: list of all components/nodes in the system.  
            Each node should have:
                - name: Name of the component (str)
                - type: Type of the node (str), used to map to `diagrams` classes. 
                Use the get_valid_node_types() tool to check valid types; if no match is found, use the default 'User'.
        
        - connections: list of connections between nodes.
            Each connection should have:
                - from: name of the source node (str)
                - to: name of the destination node (str)

        - clusters: (optional) list of groupings/subsystems.
            Each cluster should have:
                - name: name of the cluster (str)
                - nodes: list of node names belonging to this cluster
        
        project_identifier (str): Identifier for the project.        

        output_path (str): Path to the output file, e.g., "docs/Identifier_architecture_diagram.png"

    Returns:
        dict: 
            - {"status": "ok", "file": path_to_file} on success
            - {"status": "error", "error": error_message} on failure
    """
    try:
        print(f"Generating architecture diagram for project: {project_identifier}")
        
        dir_path = os.path.dirname(output_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        with Diagram(
            "", 
            filename=output_path.replace(".png", ""), 
            outformat="png",
            direction="LR",
            graph_attr={"splines": "ortho", "nodesep": "0.8", "ranksep": "1.2", "labelloc": "t", "labeljust": "c"}
            ):
            nodes_dict = {}

            # 🔹 Create clusters and nodes

            for cluster in model.get("clusters", []):
                with Cluster(cluster["name"], graph_attr={"style": "rounded", "margin": "20", "labelloc": "t", "labeljust": "c", "fontsize": "16", "fontname": "Helvetica"}):
                    for node_name in cluster["nodes"]:
                        node_type = next((n["type"] for n in model["nodes"] if n["name"] == node_name), "User")
                        nodes_dict[node_name] = build_node(node_name, node_type)

            # 🔹 Create nodes that are not in clusters
            clustered_nodes = [n for c in model.get("clusters", []) for n in c["nodes"]]
            for node in model["nodes"]:
                if node["name"] not in clustered_nodes:
                    nodes_dict[node["name"]] = build_node(node["name"], node["type"])

            # 🔹 Create connections
            for conn in model.get("connections", []):
                src = nodes_dict.get(conn["from"])
                dst = nodes_dict.get(conn["to"])
                if src and dst:
                    src >> dst

        return {"status": "ok", "file": output_path}

    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        return {
            "code": "error",
            "error_message": "ERROR: Graphviz not found. Install Graphviz and add it to the system PATH."
        }
    except Exception as e:
        print(f"ERROR: {e}")
        return {"code": "error", "error_message": str(e)}
    
def build_node(node_name, node_type):
    node_type = node_type.strip()

    if node_type == "SwaggerUI" or node_type == "custom_swagger":
        return Custom(node_name, os.path.join(ASSETS_DIR, "Swagger.png"))
    
    node_class = NODE_TYPES.get(node_type, NODE_TYPES["Default"])
    return node_class(node_name)
