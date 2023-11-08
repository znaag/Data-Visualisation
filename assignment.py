import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('unemployment analysis.csv')
china_data = data[data['Country Name'] == 'China'].values.tolist()
USA_data   = data[data['Country Name'] == 'United States'].values.tolist()
Japan_data = data[data['Country Name'] == 'Japan'].values.tolist()
print(china_data[0][2:])
print(USA_data[0][2:])
print(Japan_data[0][2:])

# Sample data (you'll need to replace this with your actual dataset)
data = {
    'Year': [1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017, 2018, 2019, 2020, 2021],
    'China': china_data[0][2:],
    'USA'  : USA_data[0][2:],
    'Japan': Japan_data[0][2:]
}

# Creating a DataFrame from the data
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

##################################### Line plot ########################################
plt.figure(figsize=(10, 6))

for country in df.columns:
    plt.plot(df.index, df[country], marker='o', label=country)

plt.title('Unemployment in Developed Countries')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.legend()
plt.grid(True)
plt.show()


##################################### Scatter plot ########################################
# Creating a DataFrame from the data
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Plotting the data as a scatter plot
plt.figure(figsize=(10, 6))

for country in df.columns:
    plt.scatter(df.index, df[country], label=country)

plt.title('Unemployment in Development Countries')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.legend()
plt.grid(True)
plt.show()


# Creating a DataFrame from the data
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

##################################### Pie Chart ########################################
country_name = 'China'

# Getting data for the chosen country
country_data = df.loc[:, country_name]

# Plotting a pie chart for the selected country
plt.figure(figsize=(8, 8))
plt.pie(country_data, labels=country_data.index, autopct='%1.1f%%', startangle=140)
plt.title(f'Unemployment Rates in {country_name}')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Choosing a country for the pie chart (e.g., China)
country_name = 'USA'

# Getting data for the chosen country
country_data = df.loc[:, country_name]

# Plotting a pie chart for the selected country
plt.figure(figsize=(8, 8))
plt.pie(country_data, labels=country_data.index, autopct='%1.1f%%', startangle=140)
plt.title(f'Unemployment Rates in {country_name}')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# Choosing a country for the pie chart (e.g., China)
country_name = 'Japan'

# Getting data for the chosen country
country_data = df.loc[:, country_name]

# Plotting a pie chart for the selected country
plt.figure(figsize=(8, 8))
plt.pie(country_data, labels=country_data.index, autopct='%1.1f%%', startangle=140)
plt.title(f'Unemployment Rates in {country_name}')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()



##################################### Histogram Chart ########################################
# Creating a DataFrame from the data
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Choosing a country for the histogram (e.g., China)
country_name = 'China'

# Getting data for the chosen country
country_data = df.loc[:, country_name]

# Plotting a histogram for the selected country
plt.figure(figsize=(8, 6))
plt.hist(country_data, bins=5, edgecolor='black')  # Adjust the number of bins as needed
plt.title(f'Unemployment Rates Distribution in {country_name}')
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Choosing a country for the histogram (e.g., USA)
country_name = 'USA'

# Getting data for the chosen country
country_data = df.loc[:, country_name]

# Plotting a histogram for the selected country
plt.figure(figsize=(8, 6))
plt.hist(country_data, bins=5, edgecolor='black')  # Adjust the number of bins as needed
plt.title(f'Unemployment Rates Distribution in {country_name}')
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Choosing a country for the histogram (e.g., Japan)
country_name = 'Japan'

# Getting data for the chosen country
country_data = df.loc[:, country_name]

# Plotting a histogram for the selected country
plt.figure(figsize=(8, 6))
plt.hist(country_data, bins=5, edgecolor='black')  # Adjust the number of bins as needed
plt.title(f'Unemployment Rates Distribution in {country_name}')
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()