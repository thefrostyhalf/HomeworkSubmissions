
# Ride Sharing Data Plotting
### Jackie McGuire 
** Observable trends: 
1. As trip number and city size increase, average fare decreases.
2. Several outliers exist where fare amount is significantly larger than expected.
3. Urban drivers make more trips than their counterparts, but earn lower fares

** Limitations:
1. Data does not include information on trip length, in time or miles. 
2. Data does not account for demand-based pricing changes.



```python
# import dependencies
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from matplotlib.backends.backend_pdf import PdfPages, PdfFile
```


```python
# Get city data from CSVs
cityfilename = os.path.join("raw_data", 'city_data.csv')
ridefilename = os.path.join("raw_data", 'ride_data.csv')
#convert city data to dataframes and check output
city_df = pd.read_csv(cityfilename)
city_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nguyenbury</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Douglas</td>
      <td>12</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>West Dawnfurt</td>
      <td>34</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rodriguezburgh</td>
      <td>52</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Repeat for ride data
ride_df = pd.read_csv(ridefilename)
ride_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South Roy</td>
      <td>2016-01-02 18:42:34</td>
      <td>17.49</td>
      <td>4036272335942</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wiseborough</td>
      <td>2016-01-21 17:35:29</td>
      <td>44.18</td>
      <td>3645042422587</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spencertown</td>
      <td>2016-07-31 14:53:22</td>
      <td>6.87</td>
      <td>2242596575892</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nguyenbury</td>
      <td>2016-07-09 04:42:44</td>
      <td>6.28</td>
      <td>1543057793673</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Merge dataframes and check output - note that value for driver_count is repeated 
merged_df=pd.merge(city_df, ride_df, on="city", how="left")
merged_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-08-19 04:27:52</td>
      <td>5.51</td>
      <td>6246006544795</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-04-17 06:59:50</td>
      <td>5.54</td>
      <td>7466473222333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-05-04 15:06:07</td>
      <td>30.54</td>
      <td>2140501382736</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-01-25 20:44:56</td>
      <td>12.08</td>
      <td>1896987891309</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-08-09 18:19:47</td>
      <td>17.91</td>
      <td>8784212854829</td>
    </tr>
  </tbody>
</table>
</div>




```python
average_fare = merged_df.groupby("city").fare.mean()
average_fare=pd.DataFrame(average_fare)
total_drivers = merged_df.groupby("city").driver_count.mean()
total_drivers=pd.DataFrame(total_drivers)
rides_total = merged_df.groupby("city").ride_id.count()
rides_total=pd.DataFrame(rides_total)
city_type = merged_df.groupby("city").type.value_counts()
city_type=pd.DataFrame(city_type)
total_fares = merged_df.groupby("city").fare.sum()
total_fares = pd.DataFrame(total_fares)
total_fares=total_fares.rename(columns={"fare": "total_fares"})
```


```python
city_summary_df = total_drivers.join(average_fare, how='outer')
city_summary_df = city_summary_df.join(rides_total, how='outer')
city_summary_df = city_summary_df.join(city_type, how='outer')
city_summary_df=city_summary_df.merge(total_fares, how='outer', right_index=True, left_index=True)
city_summary_df=city_summary_df.drop("type", axis=1)
city_summary_df=city_summary_df.rename(columns={"ride_id": "total_rides", "fare": "average_fare"})
city_summary_df = city_summary_df.reset_index()
city_summary_df=city_summary_df.round(decimals=2)
city_summary_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>type</th>
      <th>driver_count</th>
      <th>average_fare</th>
      <th>total_rides</th>
      <th>total_fares</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alvarezhaven</td>
      <td>Urban</td>
      <td>21</td>
      <td>23.93</td>
      <td>31</td>
      <td>741.79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alyssaberg</td>
      <td>Urban</td>
      <td>67</td>
      <td>20.61</td>
      <td>26</td>
      <td>535.85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anitamouth</td>
      <td>Suburban</td>
      <td>16</td>
      <td>37.32</td>
      <td>9</td>
      <td>335.84</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Antoniomouth</td>
      <td>Urban</td>
      <td>21</td>
      <td>23.62</td>
      <td>22</td>
      <td>519.75</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aprilchester</td>
      <td>Urban</td>
      <td>49</td>
      <td>21.98</td>
      <td>19</td>
      <td>417.65</td>
    </tr>
  </tbody>
</table>
</div>




```python
colors = ['Gold', 'Lightskyblue', 'Lightcoral']
citytypes = ['Urban', 'Suburban','Rural']
scatterfig=plt.figure(figsize = (7,7))
def scatterplot(citytype, facecolor):
    plt.scatter(city_summary_df['total_rides'][(city_summary_df["type"]==citytype)],city_summary_df['average_fare'][(city_summary_df["type"]==citytype)], marker="o", 
            facecolors=facecolor, edgecolors="black",
            sizes=city_summary_df['driver_count'], alpha=0.65, linewidths=1, label=citytypes)
for i, j in zip(citytypes, colors):
    scatterplot(i, j)
plt.title(" Average Fare and Total Rides by City Type \n(Circle Size Based On Driver Count per City)")
plt.xlim(0,40)
plt.xlabel("Total Rides")
plt.ylabel("Average Fare")
plt.ylim(15,45)
plt.legend(citytypes)
plt.show()
```


![png](output_7_0.png)



```python
city_pivot = city_summary_df.pivot_table(index="type", aggfunc='sum')
city_pivot=city_pivot.reset_index()
city_pivot
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>average_fare</th>
      <th>driver_count</th>
      <th>total_fares</th>
      <th>total_rides</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rural</td>
      <td>615.72</td>
      <td>104</td>
      <td>4255.09</td>
      <td>125</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Suburban</td>
      <td>1268.64</td>
      <td>629</td>
      <td>20335.69</td>
      <td>657</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Urban</td>
      <td>1623.89</td>
      <td>2607</td>
      <td>40078.34</td>
      <td>1625</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create function for pie chart
def piechart(key, title):
    explode=[0.05,0.05, 0.05]
    plt.pie(city_pivot[key], explode=explode, colors=colors, labels=city_pivot["type"], autopct='%.2f%%', shadow=True)
    plt.title("Percent of "+title+  " by City Type")
    legend = ['Rural', 'Suburban', 'Urban']
    plt.legend(legend)
    plt.show()
```


```python
# Store figure for print and save, call function for total fares
piefig1 = plt.figure(figsize=(7,7))
piechart("total_fares", "Total Fares")
```


![png](output_10_0.png)



```python
# Store figure for print and save, call function for total rides
piefig2 = plt.figure(figsize=(7,7))
piechart("total_rides", "Total Rides")
```


![png](output_11_0.png)



```python
# Store figure for print and save, call function for total drivers
piefig3 = plt.figure(figsize=(7,7))
piechart("driver_count", "Total Drivers")
```


![png](output_12_0.png)



```python
#Save Figures to PNG
scatterfig.savefig('faresandrides.png')
piefig1.savefig('totalfaresbycitytypepie.png')
piefig2.savefig('totalridesbycitytypepie.png')
piefig3.savefig('totaldriversbycitytypepie.png')
# Set output file for PDF
outputfile = 'pyber.pdf'
# Save files to PDF
with PdfPages(outputfile) as pdf:             
    pdf.savefig(scatterfig)
    pdf.savefig(piefig1)
    pdf.savefig(piefig2)
    pdf.savefig(piefig3)
```
