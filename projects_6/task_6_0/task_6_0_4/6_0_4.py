import pandas as pd
df = pd.read_csv('wild_boars.csv')

average_weight = df['weight_kg'].mode()
print(f"Boars mode   weight is {average_weight:.2f} kilos")
average_age = df['age_years'].mode()
print(f"Boars mode   age is {average_age:.2f} years")
average_length = df['length_cm'].mode()
print(f"Boars mode  length is {average_length:.2f} cm")
average_tusk_length = df['tusk_length_cm'].mode()
print(f"Boars mode  tusk_length is {average_tusk_length:.2f} cm")
average_litter_size = df['litter_size'].mode()
print(f"Boars mode  litter_size is {average_litter_size:.2f} ")
average_territory = df['territory_ha'].mode()
print(f"Boars mode  territory is {average_weight:.2f} ha")

with open ("boars_statistics_median.txt", "w") as f:
    f.write(f"Boars mode age is {average_age:.2f} years \n")
    f.write(f"Boars mode  length is {average_length:.2f} cm \n")
    f.write(f"Boars mode  tusk_length is {average_tusk_length:.2f} cm \n")
    f.write(f"Boars mode  litter_size is {average_litter_size:.2f} \n")
    f.write(f"Boars mode  territory is {average_weight:.2f} ha")
