import pandas as pd
df = pd.read_csv('wild_boars.csv')

average_weight = df['weight_kg'].median()
print(f"Boars median weight is {average_weight:.2f} kilos")
average_age = df['age_years'].median()
print(f"Boars median age is {average_age:.2f} years")
average_length = df['length_cm'].median()
print(f"Boars median length is {average_length:.2f} cm")
average_tusk_length = df['tusk_length_cm'].median()
print(f"Boars median tusk_length is {average_tusk_length:.2f} cm")
average_litter_size = df['litter_size'].median()
print(f"Boars median litter_size is {average_litter_size:.2f} ")
average_territory = df['territory_ha'].median()
print(f"Boars median territory is {average_weight:.2f} ha")

with open ("boars_statistics_median.txt", "w") as f:
    f.write(f"Boars median age is {average_age:.2f} years \n")
    f.write(f"Boars median length is {average_length:.2f} cm \n")
    f.write(f"Boars median tusk_length is {average_tusk_length:.2f} cm \n")
    f.write(f"Boars median litter_size is {average_litter_size:.2f} \n")
    f.write(f"Boars median territory is {average_weight:.2f} ha")
