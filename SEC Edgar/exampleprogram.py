from secedgar.cik_lookup import get_cik_map
import pandas as pd

exampledict = dict(list(get_cik_map()["title"].items())[:9000])

df = pd.DataFrame(exampledict, index=range(1,9000))









