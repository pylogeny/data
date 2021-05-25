from pathlib import Path

def data_path(*combs):
    return Path(__file__).parent.joinpath("data").joinpath(*combs).as_posix()

SAMPLES = {
        "ex1": {
            "tree": "(((A,B)NodeA1,(C,D)NodeA2)NodeA,((E,F)NodeB1,(G,H)NodeB2)NodeB)Root;",
            "patterns": {"1": {
                "A": "a", 
                "B": "b", 
                "C": "b", 
                "D": "c", 
                "E": "c", 
                "F": "a", 
                "G": "a", 
                "H": "a"}},
            "characters": ["a", "b", "c"],
            "taxa": ["A", "B", "C", "D", "E", "F", "G", "H"]
            },
        "ex2": {
            "tree": "(((A,B)NodeA1,(C,D)NodeA2)NodeA,((E,F)NodeB1,(G,H)NodeB2)NodeB)Root;",
            "patterns": {"2": {
                "A": "a", "B": ["a", "c"], "C": "b", "D": "c", "E": "c", "F": "a", 
                "G": ["a", "b"],
                "H": ["a", "c"]}},
            "characters": ["a", "b", "c"],
            "taxa": ["A", "B", "C", "D", "E", "F", "G", "H"]
            },
        "wichmannmixezoquean.tree": "(((ChiapasZoque,(SanMiguelChimalapaZoque,SantaMariaChimalapaZoque)),(SoteapanZoque,TexistepecZoque)),(OlutaPopoluca,(SayulaPopoluca,(NorthHighlandMixe,(LowlandMixe,SouthHighlandMixe)))));",
        "wichmannmixezoquean-nj.tree": "(((((LowlandMixe:0.22,SouthHighlandMixe:0.21):0.050,NorthHighlandMixe:0.23):0.050,SayulaPopoluca:0.27):0.030,OlutaPopoluca:0.30):0.052,((ChiapasZoque:0.24,(SanMiguelChimalapaZoque:0.23,SantaMariaChimalapaZoque:0.20):0.050):0.020,(SoteapanZoque:0.22,TexistepecZoque:0.32):0.060):0.078);"
        }
