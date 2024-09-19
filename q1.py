import numpy as np
import matplotlib.pyplot as plt

lions = np.array([15, 16, 17, 20, 19, 21, 23, 24, 25, 27])
elephants = np.array([50, 52, 54, 53, 55, 56, 57, 59, 60, 62])
zebras = np.array([100, 98, 95, 97, 96, 94, 95, 93, 92, 90])

def total_population(species_population):
    return np.sum(species_population)

def average_yearly_growth(species_population):
    yearly_growth = np.diff(species_population)
    return np.mean(yearly_growth)

lions_total = total_population(lions)
elephants_total = total_population(elephants)
zebras_total = total_population(zebras)

lions_avg_growth = average_yearly_growth(lions)
elephants_avg_growth = average_yearly_growth(elephants)
zebras_avg_growth = average_yearly_growth(zebras)

print(f"Lions total population over 10 years: {lions_total} thousand")
print(f"Elephants total population over 10 years: {elephants_total} thousand")
print(f"Zebras total population over 10 years: {zebras_total} thousand")

print(f"Lions average yearly population growth: {lions_avg_growth:.2f} thousand")
print(f"Elephants average yearly population growth: {elephants_avg_growth:.2f} thousand")
print(f"Zebras average yearly population growth: {zebras_avg_growth:.2f} thousand")

def yearly_growth_rate(species_population):
    return np.diff(species_population) / species_population[:-1] * 100

lions_growth_rate = yearly_growth_rate(lions)
elephants_growth_rate = yearly_growth_rate(elephants)
zebras_growth_rate = yearly_growth_rate(zebras)

print(f"Lions yearly growth rates: {lions_growth_rate}")
print(f"Elephants yearly growth rates: {elephants_growth_rate}")
print(f"Zebras yearly growth rates: {zebras_growth_rate}")

years = np.arange(1, 11)
plt.figure(figsize=(10, 6))
plt.plot(years, lions, label='Lions', marker='o')
plt.plot(years, elephants, label='Elephants', marker='s')
plt.plot(years, zebras, label='Zebras', marker='d')
plt.xlabel('Years')
plt.ylabel('Population (in thousands)')
plt.title('Population Trends of Lions, Elephants, and Zebras Over 10 Years')
plt.legend(
plt.grid(True)
plt.show()

def highest_avg_growth(species_growths):
    avg_growths = [average_yearly_growth(species) for species in species_growths]
    species_names = ['Lions', 'Elephants', 'Zebras']
    max_growth_species = species_names[np.argmax(avg_growths)]
    return max_growth_species

species_data = [lions, elephants, zebras]
best_species = highest_avg_growth(species_data)
print(f"Species with the highest average growth rate: {best_species}")

species_totals = [lions_total, elephants_total, zebras_total]
species_labels = ['Lions', 'Elephants', 'Zebras']

plt.figure(figsize=(8, 5))
plt.bar(species_labels, species_totals, color=['gold', 'gray', 'green'])
plt.xlabel('Species')
plt.ylabel('Total Population (in thousands)')
plt.title('Total Population of Each Species After 10 Years')
plt.show()
