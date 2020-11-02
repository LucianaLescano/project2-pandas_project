import re
import pandas as pd

def deads_wrong(serie):
    # paso mi serie Dead a string para poder aplicar la
    # siguiente función
    string_serie = serie.to_string(index=False)
    # patrón que buscaré en el string
    pattern_one = (r'\d{4}')
    # findall() para encontrar ese patrón en el string
    matches_one = str(re.findall(pattern_one, string_serie))
    # debería devolver la posiciones en las cuales ha encontrado
    # dicho patrón
    return matches_one

def deads_def(serie, original):
    # paso mi serie Dead a string para poder aplicar la
    # siguiente función
    string_serie = serie.to_string(index=False)
    # función para reemplazar el valor encontrado antes por otro nuevo
    new_string_serie = string_serie.replace('2017', 'UNKNOWN', 1)
    new_string_serie1 = new_string_serie.replace('y', 'Y')
    new_string_serie2 = new_string_serie1.replace('n', 'N')
    # df desde el string anterior
    # obtenido de: https://www.tutorialspoint.com/construct-a-dataframe-in-pandas-using-string-data-in-python
    from io import StringIO
    shark_deads_string = StringIO(new_string_serie2)
    shark_deads = pd.read_csv(shark_deads_string,sep='\n', names=['Dead'])
    # devuelve el df anterior unido al original
    final = pd.merge(original, shark_deads, on=['Dead'], how='outer')
    final_1 = final.dropna(axis=0)
    final_2 = final_1.drop(5704,axis=0)
    return final_2


