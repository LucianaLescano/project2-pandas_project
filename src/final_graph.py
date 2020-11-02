import matplotlib.pyplot as plt
import seaborn as sns

def my_graph(serie):  
    g =  sns.histplot(x=serie)
    return g