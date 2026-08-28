import pandas as pd


def sol(df):
    df_receipt = df["df_receipt"]
    df_store = df["df_store"]

    p003 = df_receipt[
        ["sales_ymd", "customer_id", "product_cd", "amount"]
    ].head(10).rename(
        columns={"sales_ymd": "sales_date"}
    )

    p023 = df_receipt.groupby("store_cd")[
        ["amount", "quantity"]
    ].sum().reset_index()

    p033 = df_receipt.groupby("store_cd")[
        "amount"
    ].mean().reset_index()

    p033 = p033[p033["amount"] >= 330]

    p034 = df_receipt[
        ~df_receipt["customer_id"].str.startswith("Z")
    ].groupby("customer_id")[
        "amount"
    ].mean().reset_index()

    p036 = pd.merge(
        df_receipt,
        df_store[["store_cd", "store_name"]],
        on="store_cd",
        how="left"
    ).head(10)

    print("P003")
    print(p003)

    print("P023")
    print(p023)

    print("P033")
    print(p033)

    print("P034")
    print(p034)

    print("P036")
    print(p036)

    return p003, p023, p033, p034, p036