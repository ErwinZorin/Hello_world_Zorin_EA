import pandas as pd

df = pd.read_csv('wild_boars.csv')
with open("boars_statistics_Percentiles.txt", 'w',) as f:
    f.write("for weight: \n")

    f.write(f"Percentile 25 (Q1):\t{df['weight_kg'].quantile(0.25):.1f} kg \n")

    f.write(f"Median 50 (Q2):\t{df['weight_kg'].quantile(0.50):.1f} kg \n")
    
    f.write(f"Percentile 75 (Q3):\t{df['weight_kg'].quantile(0.75):.1f} kg \n")

    f.write(f"Percentile 90:\t{df['weight_kg'].quantile(0.90):.1f} kg \n")

    f.write(f"Percentile 95:\t{df['weight_kg'].quantile(0.95):.1f} kg \n ")

    f.write(f"Max:\t{df['weight_kg'].quantile(1.00):.1f} kg \n")


    f.write(f"for length: \n" )
    f.write(f"Percentile 25 (Q1):\t{df['length_cm'].quantile(0.25):.1f} kg \n")

    f.write(f"Median 50 (Q2):\t{df['length_cm'].quantile(0.50):.1f} kg \n")

    f.write(f"Percentile 75 (Q3):\t{df['length_cm'].quantile(0.75):.1f} kg \n")

    f.write(f"Percentile 90:\t{df['length_cm'].quantile(0.90):.1f} kg \n")

    f.write(f"Percentile 95:\t{df['length_cm'].quantile(0.95):.1f} kg \n")

    f.write(f"Max:\t{df['length_cm'].quantile(1.00):.1f} kg")
