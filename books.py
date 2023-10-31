# %%
import pandas as pd


def read():
    return (
        pd.read_csv("BL-Flickr-Images-Book.csv")
        .rename(columns=lambda header: header.lower().replace(" ", "_"))
        .rename(columns={"identifier": "id"})
    )


books = read()
# %%
