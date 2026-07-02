def generate_insights(profile):
    """
    Converts dataset profile into simple human-readable insights.
    """

    insights = []

    rows = profile["row_count"]
    cols = profile["column_count"]

    if rows < 100:
        insights.append("Dataset is very small. Good for testing or demos.")
    elif rows < 5000:
        insights.append("Dataset is small to medium sized. Suitable for analysis.")
    else:
        insights.append("Dataset is large. May require optimization.")

    missing = profile["missing_values"]
    total_missing = sum(missing.values())

    if total_missing == 0:
        insights.append("No missing values found.")
    elif total_missing < rows * 0.05:
        insights.append("Low missing values detected.")
    else:
        insights.append("High missing values detected. Cleaning recommended.")

    duplicates = profile["duplicate_rows"]

    if duplicates == 0:
        insights.append("No duplicate rows found.")
    elif duplicates < rows * 0.05:
        insights.append("Low duplicates detected.")
    else:
        insights.append("High duplicates detected.")

    insights.append(f"Dataset has {cols} columns with mixed data types.")

    return insights