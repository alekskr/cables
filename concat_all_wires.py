import provoda_montazhnye
import provoda_montazhnye_s_kombinirovannoy_izolyatsiey
import provoda_mpo

import pandas as pd

all_lists = provoda_mpo.all_cables + provoda_montazhnye.all_cables + provoda_montazhnye_s_kombinirovannoy_izolyatsiey.all_cables

data = pd.DataFrame({'Провод': [],
                     'Наружный диаметр': [],
                     'Минимальный радиус изгиба': [],
                     'Диапазон рабочих температур': [],
                     'Ссылка': [],
                     'Расшифровка': []})

# добавление в таблицу всех проводов
for i in all_lists:
    i_frame = pd.DataFrame([i])
    data = pd.concat([data, i_frame], ignore_index=True)

# сохраняем в csv-файл
data.to_csv('all_wires.csv', index=False)

