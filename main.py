import numpy as np
import pandas as pd
from tabulate import tabulate

# Excel dosyasınından verileri al
data = pd.read_excel('C:\\Users\\Meltem\\Desktop\\soru1_2_data.xlsx', header=None)
image = data.values

# Minimum ve maksimum değerleri bul
I_min = np.min(image)
I_max = np.max(image)
L = 256

# Contrast stretching işlemini yap
contrast_stretched_image = np.zeros(image.shape, dtype=np.float64)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        contrast_stretched_image[i, j] = (image[i, j] - I_min) / (I_max - I_min) * (L - 1)

# Sonuçları tablo olarak yazdır
contrast_stretched_df = pd.DataFrame(contrast_stretched_image)
# Tabulate kullanarak tablo çıktısını yazdır
print("Contrast Stretched Image:")
print(tabulate(contrast_stretched_df, headers='keys', tablefmt='grid'))
