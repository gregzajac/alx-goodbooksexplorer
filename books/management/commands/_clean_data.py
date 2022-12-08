import pandas as pd


def clean(file_path):
    df = pd.read_csv(file_path, on_bad_lines="skip")

    dates = df.publication_date.str.split("/", expand=True)

    dates.columns = ["m", "d", "y"]
    dates = dates.astype(int)
    dates.d[(dates.m.isin([2, 4, 6, 9, 11])) & (dates.d == 31)] = 30
    dates = pd.to_datetime(dates.apply(
        lambda x: f"{x.y}-{x.m}-{x.d}", axis=1
    ), utc=True)
    df["publication_date"] = dates
    df.columns = [x.strip() for x in df.columns]
    return df.to_dict(orient="records")

# print(clean("../../../data/books.csv.zip"))
