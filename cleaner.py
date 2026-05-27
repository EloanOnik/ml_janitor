# cleaner.py
import pandas as pd

def find_empty_columns(df: pd.DataFrame, threshold: float = 0.70) -> list:
    """
    Находит столбцы, где доля пустых значений >= threshold.
    Возвращает список имен столбцов.
    """
    cols_to_drop = []
    for col in df.columns:
        if df[col].isnull().mean() >= threshold:
            cols_to_drop.append(col)
    return cols_to_drop


def drop_empty_columns(df: pd.DataFrame, threshold: float = 0.70) -> pd.DataFrame:
    """
    Удаляет столбцы с пустотами >= threshold и возвращает НОВЫЙ DataFrame.
    """
    cols = find_empty_columns(df, threshold)
    return df.drop(columns=cols)