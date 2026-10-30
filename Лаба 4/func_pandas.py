import pandas as pd
def create_simple_dataframe():
    return pd.DataFrame({"Ім'я": ["Олег", "Анна"], "Бал": [95, 88]}).to_string()
