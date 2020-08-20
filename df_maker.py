import pandas as pd
import re
from glob import glob
def squeeze(string_name):
    return sorted(glob(f'./Frets_photos/{string_name}/*'), key=lambda x:float(re.findall("(\d+)",x)[0]))
def string_into_rows(folder,root_note):
    notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#'] * 2
    ind = notes.index(root_note) + 1
    colxoz = []
    for (i,num) in zip(notes[ind:(ind + 12)], range(12)):
         colxoz.append({'name': folder[num][17:21], 'note': i, 'location': folder[num]})
    return colxoz
E_photos = squeeze("E")
A_photos = squeeze("A")
D_photos = squeeze("D")
G_photos = squeeze("G")
B_photos = squeeze("B")
all_strings = (string_into_rows(E_photos, 'E') +
              string_into_rows(A_photos, 'A') +
              string_into_rows(D_photos,'D') +
              string_into_rows(G_photos,'G') +
              string_into_rows(B_photos, 'B'))

df = pd.DataFrame(all_strings)



df.to_csv('Strings.csv')
