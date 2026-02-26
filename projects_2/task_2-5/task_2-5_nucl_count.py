print("=== Анализ последовательности ДНК ===")
dna = input("Последовательность ДНК: ")
dna = dna.upper()
 
print(f"Последовательность в верхнем регистре: {dna}\n")
print()
print("Подсчёт нуклеотидов:")
print(f"A: {dna.count("A")}")
print(f"T: {dna.count("T")}")
print(f"G: {dna.count("G")}")
print(f"C: {dna.count("C")}")
print()

print(f"Общая длина: {len(dna)} нуклеотидов")
