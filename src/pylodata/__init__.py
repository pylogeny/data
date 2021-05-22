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
        "wichmannmixezoquean.tree": "(((ChiapasZoque,(SanMiguelChimalapaZoque,SantaMariaChimalapaZoque)),(SoteapanZoque,TexistepecZoque)),(OlutaPopoluca,(SayulaPopoluca,(NorthHighlandMixe,(LowlandMixe,SouthHighlandMixe)))));"
        }
