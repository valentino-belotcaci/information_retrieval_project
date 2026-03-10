from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import pyterrier as pt
import json

# Initialize a FastAPI application.
app = FastAPI(host="0.0.0.0")

# Configure CORS (Cross-Origin Resource Sharing) middleware to allow requests from any origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Function to initialize the PyTerrier index.
def initialize_index():
    # Initialize PyTerrier if it's not already started.
    if not pt.started():
        pt.init()

    # Path to the JSON file containing the data.
    json_file_path = '../tattoo_design/spiders/results.json'
    
    # Load the data from the JSON file.
    data = load_data_from_json(json_file_path)

    # Create a DataFrame from the loaded data.
    df = pd.DataFrame(data, columns=["docno", "link", "text"])

    # Path where the index will be stored.
    index_path = '../index_3docs'

    # Initialize a PyTerrier indexer with the specified index path and metadata fields.
    indexer = pt.DFIndexer(index_path, overwrite=True, meta=["docno", "link", "text"])
    print("Indexing...")

    # Create the index from the DataFrame.
    index_ref = indexer.index(df["text"], df[["docno", "link", "text"]])
    index = pt.IndexFactory.of(index_ref)

    # Optional: Print out the index's lexicon for debugging purposes.
    for kv in index.getLexicon():
        print("%s  -> %s " % (kv.getKey(), kv.getValue().toString()))

    print("Indexing completed.")

    # Return a PyTerrier BatchRetrieve object configured to use the created index.
    return pt.BatchRetrieve(index, wmodel="BM25", metadata=["docno", "link", "text"])

# Function to load data from a JSON file.
def load_data_from_json(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(len(data))
    except Exception as e:
        print(f"Error loading data from JSON file: {e}")

    return data

# Main block of the script.
if __name__ == "__main__":
    # Initialize the index when the script runs.
    initialize_index()

# FastAPI endpoint for handling search queries.
@app.get("/")
def read_root(query: str = ""):
    # Initialize the index and search for the query.
    results = initialize_index()
    results = results.search(query)

    # Convert the search results DataFrame to JSON.
    results_json = results.to_json(orient='records')

    # Return the JSON response.
    return JSONResponse(content=results_json)
