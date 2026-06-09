import pandas as pd
df = pd.read_csv('wild_boars.csv')

average_weight = df['weight_kg'].mean()
print(f"Boars average weight is {average_weight:.2f} kilos")
average_age = df['age_years'].mean()
print(f"Boars average age is {average_age:.2f} years")
average_length = df['length_cm'].mean()
print(f"Boars average length is {average_length:.2f} cm")
average_tusk_length = df['tusk_length_cm'].mean()
print(f"Boars average tusk_length is {average_tusk_length:.2f} cm")
average_litter_size = df['litter_size'].mean()
print(f"Boars average litter_size is {average_litter_size:.2f} ")
average_territory = df['territory_ha'].mean()
print(f"Boars average territory is {average_weight:.2f} ha")

with open ("boars_statistics.txt", "w") as f:
    f.write(f"Boars average age is {average_age:.2f} years \n")
    f.write(f"Boars average length is {average_length:.2f} cm \n")
    f.write(f"Boars average tusk_length is {average_tusk_length:.2f} cm \n")
    f.write(f"Boars average litter_size is {average_litter_size:.2f} \n")
    f.write(f"Boars average territory is {average_weight:.2f} ha")
