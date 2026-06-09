import pandas as pd

df = pd.read_csv('wild_boars.csv')
with open("boars_statistics_dyspercia.txt", 'w',) as f:

    f.write("for weight: \n")
    variance_weight = df['weight_kg'].var()

    f.write(f"Weight variance is {variance_weight:.2f} kg*kg \n")
 

    std_weight = df['weight_kg'].std()

    f.write(f"Standart deviation is {std_weight:.2f} kg \n")


    cv_weight = (df['weight_kg'].std() / df['weight_kg'].mean()) * 100
    
    f.write(f"Coefficient of variation is {cv_weight:.2f} % \n")
    f.write(f"for length: \n" )
    variance_weight = df['length_cm'].var()

    f.write(f"length variance is {variance_weight:.2f} cm*cm \n")
 

    std_weight = df['length_cm'].std()

    f.write(f"Standart deviation is {std_weight:.2f} cm \n")


    cv_weight = (df['length_cm'].std() / df['length_cm'].mean()) * 100
    
    f.write(f"Coefficient of variation is {cv_weight:.2f} % \n")

    f.write(f"for tusk_length: \n" )
    variance_weight = df['tusk_length_cm'].var()

    f.write(f"Tusk_length variance is {variance_weight:.2f} cm*cm \n")
 

    std_weight = df['tusk_length_cm'].std()

    f.write(f"Standart deviation is {std_weight:.2f} cm \n")


    cv_weight = (df['tusk_length_cm'].std() / df['tusk_length_cm'].mean()) * 100
    
    f.write(f"Coefficient of variation is {cv_weight:.2f} % \n")
