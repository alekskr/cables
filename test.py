import provoda_montazhnye
import provoda_montazhnye_s_kombinirovannoy_izolyatsiey
import pandas as pd

all_lists = provoda_montazhnye.all_cables + provoda_montazhnye_s_kombinirovannoy_izolyatsiey.all_cables

data = pd.DataFrame({'Провод': [],
                     'Наружный диаметр': [],
                     'Минимальный радиус изгиба': [],
                     'Диапазон рабочих температур': [],
                     'Ссылка': [],
                     'Расшифровка': []})

# добавление в таблицу всех проводов
for i in all_lists:
    data = data.append(i, ignore_index=True)

# сохраняем в csv-файл
data.to_csv('D:\\Python projects\\Beautiful_soup\\cables\\provoda.csv', index=False)

