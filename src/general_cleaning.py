import pandas as pd 
def first_step(data):
    # primer paso, deshacerme de las columnas que no quiero
    first_data = data.drop(['Case Number', 'Year', 'Type', 'Area', 'Location', 'Activity', 'Name', 'Sex ', 'Injury', 'Age', 'Time', 'Species ', 'pdf', 'href', 'Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22', 'Unnamed: 23'], axis=1)
    # segundo paso, quitarme todos los NaN, para ello establezco un umbral de 5, es decir
    # las filas que tengas mas de 5 NaN serán eliminadas
    second_data = first_data.dropna(axis=0, thresh=5)
    # tercer paso, cambio de nombre de las columnas por unos más adecuados
    data_back_up = second_data.copy()
    second_data = second_data.rename(columns={'Fatal (Y/N)':'Dead', 'Investigator or Source':'Source', 'href formula':'More_Info'})
    # cuarto paso, sobreescribo los NaN por UNKNOWN
    fourth_data = second_data.fillna("UNKNOWN")
    return fourth_data 