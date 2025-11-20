import pandas as pd


data = {
    'names': ["Abu Hurairah (radiyallāhu anhumā) and Abdur Rahmān bin Sakhr ad-Dawsi (radiyallāhu anhumā)", "Abdullah ibn Umar ibn al-Khattāb (radiyallāhu anhumā)",
             "Anas bin Mālik (radiyallāhu anhu)", "Aishah bint Abi Bakr, Umm ul-Mumineen (radiyallāhu anhumā)","Abdullah Ibn Abbās (radiyallāhu anhumā)","Jābir bin Abdillah al-Ansāri (radiyallāhu anhumā)", "Abu Saeed al-Khudri and Sa'd bin Mālik bin Sinān (radiyallāhu anhu)"],
    "number_of_hadiths_narrated": [5347,2630,2286,2210,1660,1540,1170]
}

df = pd.DataFrame(data)

df.to_csv('hadith_narrators.csv', index=False)












