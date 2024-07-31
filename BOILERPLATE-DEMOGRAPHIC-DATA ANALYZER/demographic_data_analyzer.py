import pandas as pd

def calculate_demographic_data(print_data=True):
    # Leer datos del archivo
    df = pd.read_csv('adult.data.csv')

    # Cuántos de cada raza están representados en este conjunto de datos
    race_count = df['race'].value_counts()

    # Edad promedio de los hombres
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # Porcentaje de personas con un título de bachiller
    percentage_bachelors = ((df['education'] == 'Bachelors').mean() * 100).round(1)

    # Porcentaje de personas con educación avanzada que ganan más de 50K
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = ((higher_education['salary'] == '>50K').mean() * 100).round(1)

    # Porcentaje de personas sin educación avanzada que ganan más de 50K
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = ((lower_education['salary'] == '>50K').mean() * 100).round(1)

    # Número mínimo de horas trabajadas por semana
    min_work_hours = df['hours-per-week'].min()

    # Porcentaje de personas que trabajan el número mínimo de horas por semana que ganan más de 50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = ((num_min_workers['salary'] == '>50K').mean() * 100).round(1)

    # País con el porcentaje más alto de personas que ganan más de 50K
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    highest_earning_country = (country_salary['>50K'].idxmax())
    highest_earning_country_percentage = (country_salary['>50K'].max() * 100).round(1)

    # Ocupación más popular para aquellos que ganan >50K en India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # NO MODIFICAR A PARTIR DE AQUÍ
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Ejemplo de uso
if __name__ == "__main__":
    calculate_demographic_data()
