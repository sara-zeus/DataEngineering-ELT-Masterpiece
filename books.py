# %%
import pandas as pd


def read():
    return (
        pd.read_csv("BL-Flickr-Images-Book.csv")
        .rename(columns=lambda header: header.lower().replace(" ", "_"))
        .rename(columns={"identifier": "id"})
        .drop(
            columns=[
                "edition_statement",
                "contributors",
                "corporate_author",
                "corporate_contributors",
                "former_owner",
                "engraver",
                "issuance_type",
                "shelfmarks",
            ]
        )
        .set_index("id")
    )


books = read()
# %%
