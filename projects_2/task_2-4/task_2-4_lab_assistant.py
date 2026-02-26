 v = float(input("Введите нужный объем раствора (в мл): "))

with open("recipe.txt", "w", encoding='utf-8') as recipe:
    recipe.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:  \n   {23*'-'}\n") 
    recipe.write(f"  Общий объем: {v} мл  \n")
    recipe.write(f"  Масса соли: {(0.009*v):.2f}\n")
    recipe.write(f"  Объем воды: {v}")
