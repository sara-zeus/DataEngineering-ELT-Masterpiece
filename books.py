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

books.loc[:, "date_of_publication"].str.extract(r"(\d{4})").isna().sum()


# %%

books.loc[:, "date_of_publication"].str.extract(r"(\d{4})").fillna("0").sum()


# %%
pd.to_numeric(
    books.loc[:, "date_of_publication"].str.extract(r"(\d{4})", expand=False).fillna(0),
    downcast="unsigned",
)
