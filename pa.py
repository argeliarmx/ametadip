import polars as pl

# Sample data
data = {
    "name": ["Alice", None, "Charlie", "David"],
    "age": [25, 30, 35, None],
    "city": ["New York", "Los Angeles", None, "Chicago"]
}

# Create a Polars DataFrame
df = pl.DataFrame(data)

# Print original DataFrame
print("Original DataFrame:")
print(df)

# Filter the DataFrame to remove rows with null values in any string column
df = df.filter(~pl.any(pl.col(pl.Utf8).is_null()))

# Print filtered DataFrame
print("\nFiltered DataFrame:")
print(df)
