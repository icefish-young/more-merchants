import os
from dotenv import load_dotenv
from scrapegraphai.graphs import SearchGraph
from scrapegraphai.utils import prettify_exec_info

graph_config = {
   "llm": {
        "api_key": "xxx",
        "model": "gpt-3.5-turbo",
    },
   "max_results": 10,
   "verbose": True
}

# Create the SearchGraph instance
search_graph = SearchGraph(
   prompt="List me some cross-border e-commerce small merchant website which is selling goods from China to America",
   config=graph_config,
#    schema=schema
)

# Run the graph
result = search_graph.run()
print(result)