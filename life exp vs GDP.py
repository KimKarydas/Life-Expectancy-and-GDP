
#Libraries
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import plotly.io as pio


#Importing the data
df = pd.read_csv('life exp and GDP.csv')
print(df.head())

#Statistical summary of the data
print(df.shape)
print(df.describe())

#Check for missing values within the df
df_miss = df.isnull().sum()
print(df_miss)

#Lookingg for duplicates
df_dupli = df.duplicated().sum()
print(df_dupli)

#Checking the data type
print(df.dtypes)

#Scatter Plot
fig1 = px.scatter(data_frame = df, 
                 x="life_exp", 
                 y="gdp_cap", 
                 size = "life_exp",
                 color= "continent"
                 )
                
fig1.show()


pio.write_html(fig1, file='figure1.html', auto_open=True)

#Scatter Plot with Trendline
fig2 = px.scatter(data_frame = df, 
                 x="life_exp", 
                 y="gdp_cap", 
                 size = "gdp_cap",
                 color= "life_exp",
                 trendline = "ols")
                
fig2.show()

pio.write_html(fig2, file='figure2.html', auto_open=True)

# Main Pie plot 
fig3 = px.pie(data_frame = df, 
        values = "gdp_cap",
        names = "continent")

fig3.show()

pio.write_html(fig3, file='figure3.html', auto_open=True)

# Multiple pie plot display 
europe = df.query("continent=='Europe'")
asia = df.query("continent=='Asia'")
africa = df.query("continent=='Africa'")
america = df.query("continent=='Americas'")
oceania = df.query("continent=='Oceania'")
fig = make_subplots(rows=3,
                    cols=2,
                    specs=[[{'type':'domain'}, {'type':'domain'}],
                        [{'type':'domain'}, {'type':'domain'}],
                       [{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=("Asia", "Africa", "Americas", "Europe"))

fig.add_trace(go.Pie(labels=asia["country"], values=asia["life_exp"], name="Asia" ),1,1)
fig.update_traces(textposition='inside')

fig.add_trace(go.Pie(labels=africa["country"], values=africa["life_exp"], name="Africa"), 1, 2)
fig.update_traces(textposition='inside')

fig.add_trace(go.Pie(labels=america["country"], values=america["life_exp"], name="Americas"), 2, 1)
fig.update_traces(textposition='inside')

fig.add_trace(go.Pie(labels=europe["country"], values=europe["life_exp"], name="Europe"), 2, 2)
fig.update_traces(textposition='inside')

fig.update_layout(height=1500, width=1000,
                  title_text="Pie Chart Subplot of Life Expectancy for each Continent per Country")
                  
fig.show()

pio.write_html(fig, file='figure4.html', auto_open=True)

# Check top 5 countries with the ighest life expectancy
life_exp_max = df.nlargest(n=3, columns=["life_exp"])
life_exp_min = df.nsmallest(n=3, columns=["life_exp"])
print(life_exp_max)
print(life_exp_min)

japan = df.query("country=='Japan'")
china = df.query("country=='Hong Kong, China'")
iceland = df.query("country=='Iceland'")
sawziland = df.query("country=='Swaziland'")
mozambique = df.query("country=='Mozambique'")
zambia = df.query("country=='Zambia'")

fig5 = make_subplots(rows=1,
                    cols=1)

fig5.add_trace(go.Bar(x= japan["country"], y= japan["life_exp"]),1,1)

fig5.add_trace(go.Bar(x= china["country"], y= china["life_exp"]),1,1)

fig5.add_trace(go.Bar(x= iceland["country"], y= iceland["life_exp"]),1,1)

fig5.add_trace(go.Bar(x= sawziland["country"], y= sawziland["life_exp"]),1,1)

fig5.add_trace(go.Bar(x= mozambique["country"], y= mozambique["life_exp"]),1,1)

fig5.add_trace(go.Bar(x= zambia["country"], y= zambia["life_exp"]),1,1)


fig5.update_layout(height=550, width=750, title_text = "Top 3 Highest and Lowest Life Expectancy Countries",showlegend=False
                  )

fig5.show()



pio.write_html(fig5, file='figure5.html', auto_open=True)


# Box plot
fig6 = px.box(df['life_exp'])
fig6.update_layout(height=1000, width=800)
fig6.show()


pio.write_html(fig6, file='figure6.html', auto_open=True)


#Map chart with colors 
df = px.data.gapminder().query("year == 2007")
avg_lifeExp = (df['lifeExp']*df['pop']).sum()/df['pop'].sum()

fig = px.choropleth(df, locations="iso_alpha", color="lifeExp",
                    color_continuous_scale=px.colors.diverging.Geyser,
                    color_continuous_midpoint=avg_lifeExp,
                    title="World Average Life Expectancy in 2007 " % avg_lifeExp)
fig.show()


pio.write_html(fig, file='figure7.html', auto_open=True)





