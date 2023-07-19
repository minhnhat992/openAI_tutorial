# to clean up raw data from json dbt artifacts
# https://docs.getdbt.com/reference/artifacts/manifest-json
import json

import pandas as pd

raw_data_path = "/home/data/raw/"

with open(raw_data_path + "manifest.json", "rb") as f:
    manifest_json = json.loads(f.read())
    # just need to get nodes as its has full metadata of all dbt assets
    nodes_df = (
        pd.DataFrame(manifest_json["nodes"])
        .transpose()
        .rename_axis("nodes")
        .reset_index()
    )

    # filter out for colmuns
    nodes_df.to_csv("/home/data/cleaned/dbt_nodes.csv", index=False)
