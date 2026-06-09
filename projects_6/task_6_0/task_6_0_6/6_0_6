import pandas as pd

with open("boars_statistics_IQR.txt", 'w',) as f:
    for gender in ['Male', 'Female']:
        number = df[df['gender'] == gender]['length_cm']

        q1 = number.quantile(0.25)
        q3 = number.quantile(0.75)
        iqr = q3 - q1

        f.write(f"{gender}:\n")
        f.write(f"  Q1 (25%): {q1:.1f} cm\n")
        f.write(f"  Q3 (75%): {q3:.1f} cm\n")
        f.write(f"  IQR: {iqr:.1f} cm\n")
