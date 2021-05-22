from pylodata import data_path
from pylodata.wordlist import *
from lingpy import Wordlist

def test_get_binary_patterns():
    wl = Wordlist(data_path("wichmannmixezoquean.tsv"))
    pats = get_binary_patterns(wl, "cogid")
    print(pats)


def test_get_multistate_patterns():
    wl = Wordlist(data_path("wichmannmixezoquean.tsv"))
    pats = get_multistate_patterns(wl, "cogid")
    print(pats)



if __name__ == "__main__":
    pt = test_get_binary_patterns()
    pt = test_get_multistate_patterns()


