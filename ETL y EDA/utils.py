import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import ast
import os


def load_json(json_path):
    """
    Carga un archivo json.

    Parametros:
    - json_path: arhivo json a cargar

    Retorna:
    - DataFrame cargado desde un archivo json.
    """
    # leer cada linea del archivo json
    rows = []
    with open(json_path, encoding='utf-8') as f:
        for line in f.readlines():
            rows.append(ast.literal_eval(line))
    
    df = pd.DataFrame(rows)
    return df


def save_to_csv(dfs, names):

    """
    Guarda un dataframe un archivo csv en un directorio especifico.
        Parametros:
        - dfs: DataFrame para guardar.
        - names: Nombre del archivo CSV.
    """
    for df, name in zip(dfs, names):
        archivo = f'data/csv/{name}.csv'
        df.to_csv(archivo, index=False, encoding='utf-8')
        print(f"DataFrame '{name}' guardado como '{archivo}'")


def save_to_pq(dfs, names):

    """
    Guarda un DataFrame en un archivo parquet en un directorio específico.
        Parametros:
        - dfs: DataFrame para guardar.
        - names: Nombre del archivo parquet.
    """
    for df, name in zip(dfs, names):
        archivo = f'data/parquet/{name}.parquet'
        pq.write_table(pa.Table.from_pandas(df), archivo)
        print(f"DataFrame '{name}' guardado como '{archivo}'")


def data_summ(df):
    '''
    Esta función proporciona información detallada sobre el tipo de dato y los valores nulos presentes en un marco de datos.
    '''

    info_dict = {"Columnas": [], "Tipo_Dato": [], "No_miss_Qty": [], "%Missing": [], "Missing_Qty": []}
    

    for column in df.columns:
        
        info_dict["Columnas"].append(column)
        info_dict["Tipo_Dato"].append(df[column].apply(type).unique())
        info_dict["No_miss_Qty"].append(df[column].count())
        info_dict["%Missing"].append(round(df[column].isnull().sum() * 100 / len(df), 2))
        info_dict['Missing_Qty'].append(df[column].isnull().sum())

    df_info = pd.DataFrame(info_dict)
    
    print("\nTotal filas: ", len(df))
    print("\nTotal filas nulas: ", df.isna().all(axis=1).sum())
    print("\nTotal filas duplicadas: ", df.duplicated().sum())
    
    
    return df_info


def duplicates(df, column):
    '''
    Comprueba y muestra filas duplicadas en un DataFrame según una columna específica.

    Esta función toma como entrada un DataFrame y el nombre de una columna específica.
    Luego, identifica filas duplicadas según el contenido de la columna especificada,
    los filtra y los clasifica para facilitar la comparación.

    Parametros:
        df (pandas.DataFrame):el DataFrame para buscar filas duplicadas.
        column (str):el nombre de la columna en función de la cual buscar duplicados.

    Returns:
        pandas.DataFrame or str: un DataFrame que contiene las filas duplicadas filtradas y ordenadas,
        listas para inspección y comparación, o el mensaje "No hay duplicados" si no se encuentran duplicados.
    '''
    # Se filtran las filas duplicadas
    duplicated_rows = df[df.duplicated(subset=column, keep=False)]
    if duplicated_rows.empty:
        return "No hay duplicados"
    
    # ordenar filas duplicadas para compararlas entre sí
    duplicated_rows_sorted = duplicated_rows.sort_values(by=column)
    return duplicated_rows_sorted


def drop_duplicates(df, column):
    '''
    Esta función cuenta los valores nulos en cada fila para organizar el marco de datos en orden de valores nulos,
    para eliminar registros duplicados que tengan el mismo valor
    sin afectar la fila que tiene más registros válidos.
    '''

    # columna temporaria 
    df['temp_index'] = range(len(df))

    # Contar valores nulos en cada fila
    df['num_null'] = df.isnull().sum(axis=1)

    # Ordenar por la columna especificada y el número de valores nulos
    df = df.sort_values(by=[column, 'num_null'])

    # Eliminar duplicados, mantener la primera aparición
    df = df.drop_duplicates(subset=column, keep='first')

    # Ordene nuevamente por la columna temporal y elimínela
    df = df.sort_values(by='temp_index').drop(['temp_index', 'num_null'], axis=1)

    # Resetea el índice
    df = df.reset_index(drop=True)

    return df


def count_value_per_column(dataframe, value_to_count):
    """
    Cuenta las apariciones de un valor específico en cada columna del DataFrame.

    Parametros:
    - dataframe: pd.DataFrame
        El marco de datos de entrada.
    - value_to_count: str
        El valor a contar en cada columna.
    Prints:
    - El recuento del valor especificado en cada columna.

    Ejemplo:
    - count_value_per_column(df, 'SD') # Reemplace 'df' con su nombre de DataFrame.
    """
    for column_name in dataframe.columns:
        count_value = dataframe[column_name].value_counts().get(value_to_count, 0)
        print(f"Cuenta de '{value_to_count}' en la columna {column_name}: {count_value}")

def replace_all_nulls(df):
    '''
    Recibe un df como parámetro y completa todos los valores nulos por columna dependiendo de su tipo de dato
    '''

    for column in df.columns:
        mask = df[column].notnull()
        dtype = df[column][mask].apply(type).unique()

        if dtype[0] == str: 
            df[column] = df[column].fillna('No data')
        elif dtype[0] == float:
            mean = df[column].mean()
            df[column] = df[column].fillna(mean)
        elif dtype[0] == list:
            df[column] = df[column].fillna('No data')