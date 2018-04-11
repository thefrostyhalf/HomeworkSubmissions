

```python
### Observable trends
##1) The higest and lowest performing schools are Charter and District, predictably
##2) The Budget Per Student is lower, on average. for Charter schools
##3) Percent of students passing both math and reading is higher for Charter Schools,
## despite lower spending per student. 
```


```python
import os
import csv
import pandas as pd
import numpy as np
```


```python
schoolfile = 'schools_complete.csv'
studentfile = 'students_complete.csv'
csvpath1 = os.path.join('raw_data', schoolfile)
csvpath2 = os.path.join('raw_data', studentfile)
school_df=pd.read_csv(csvpath1)
student_df=pd.read_csv(csvpath2)
print(school_df.columns)
print(student_df.columns)
school_df.head()
student_df.head()
student_df.fillna(value=0)
```

    Index(['School ID', 'name', 'type', 'size', 'budget'], dtype='object')
    Index(['Student ID', 'name', 'gender', 'grade', 'school', 'reading_score',
           'math_score'],
          dtype='object')





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
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Bryan Miranda</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>94</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Sheena Carter</td>
      <td>F</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>82</td>
      <td>80</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>Nicole Baker</td>
      <td>F</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>96</td>
      <td>69</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>Michael Roth</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>95</td>
      <td>87</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>Matthew Greene</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>96</td>
      <td>84</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>Andrew Alexander</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>70</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>Daniel Cooper</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>78</td>
      <td>77</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>Brittney Walker</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>64</td>
      <td>79</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>William Long</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>71</td>
      <td>79</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>Tammy Hebert</td>
      <td>F</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>85</td>
      <td>67</td>
    </tr>
    <tr>
      <th>15</th>
      <td>15</td>
      <td>Dr. Jordan Carson</td>
      <td>M</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>88</td>
    </tr>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>Donald Zamora</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>88</td>
      <td>55</td>
    </tr>
    <tr>
      <th>17</th>
      <td>17</td>
      <td>Kimberly Santiago</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>74</td>
      <td>75</td>
    </tr>
    <tr>
      <th>18</th>
      <td>18</td>
      <td>Kevin Stevens</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>64</td>
      <td>69</td>
    </tr>
    <tr>
      <th>19</th>
      <td>19</td>
      <td>Brandi Lyons</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>89</td>
      <td>80</td>
    </tr>
    <tr>
      <th>20</th>
      <td>20</td>
      <td>Lisa Davis</td>
      <td>F</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>91</td>
      <td>89</td>
    </tr>
    <tr>
      <th>21</th>
      <td>21</td>
      <td>Kristen Lopez</td>
      <td>F</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>77</td>
    </tr>
    <tr>
      <th>22</th>
      <td>22</td>
      <td>Kimberly Stewart</td>
      <td>F</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>99</td>
      <td>84</td>
    </tr>
    <tr>
      <th>23</th>
      <td>23</td>
      <td>Christopher Parker</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>81</td>
      <td>68</td>
    </tr>
    <tr>
      <th>24</th>
      <td>24</td>
      <td>Chelsea Griffith</td>
      <td>F</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>85</td>
      <td>73</td>
    </tr>
    <tr>
      <th>25</th>
      <td>25</td>
      <td>Cesar Morris</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>92</td>
      <td>70</td>
    </tr>
    <tr>
      <th>26</th>
      <td>26</td>
      <td>Melanie Decker</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>63</td>
      <td>85</td>
    </tr>
    <tr>
      <th>27</th>
      <td>27</td>
      <td>Tracey Oconnor</td>
      <td>F</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>80</td>
      <td>58</td>
    </tr>
    <tr>
      <th>28</th>
      <td>28</td>
      <td>Kelly James</td>
      <td>F</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>73</td>
      <td>55</td>
    </tr>
    <tr>
      <th>29</th>
      <td>29</td>
      <td>Nicole Brown</td>
      <td>F</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>88</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>39140</th>
      <td>39140</td>
      <td>Cheyenne Hernandez</td>
      <td>F</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>76</td>
      <td>99</td>
    </tr>
    <tr>
      <th>39141</th>
      <td>39141</td>
      <td>Jonathan Sullivan</td>
      <td>M</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>86</td>
      <td>93</td>
    </tr>
    <tr>
      <th>39142</th>
      <td>39142</td>
      <td>Deborah Higgins DDS</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>96</td>
      <td>83</td>
    </tr>
    <tr>
      <th>39143</th>
      <td>39143</td>
      <td>Steven Jackson</td>
      <td>M</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>71</td>
      <td>93</td>
    </tr>
    <tr>
      <th>39144</th>
      <td>39144</td>
      <td>Cristian Webster</td>
      <td>M</td>
      <td>12th</td>
      <td>Thomas High School</td>
      <td>77</td>
      <td>87</td>
    </tr>
    <tr>
      <th>39145</th>
      <td>39145</td>
      <td>Audrey Fry</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>94</td>
      <td>74</td>
    </tr>
    <tr>
      <th>39146</th>
      <td>39146</td>
      <td>Michael Carroll</td>
      <td>M</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>69</td>
      <td>95</td>
    </tr>
    <tr>
      <th>39147</th>
      <td>39147</td>
      <td>Raymond Hawkins</td>
      <td>M</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>88</td>
      <td>81</td>
    </tr>
    <tr>
      <th>39148</th>
      <td>39148</td>
      <td>Christopher Wilson</td>
      <td>M</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>89</td>
      <td>89</td>
    </tr>
    <tr>
      <th>39149</th>
      <td>39149</td>
      <td>Glenda Fletcher</td>
      <td>F</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>82</td>
      <td>93</td>
    </tr>
    <tr>
      <th>39150</th>
      <td>39150</td>
      <td>Jennifer Hamilton</td>
      <td>F</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>80</td>
      <td>75</td>
    </tr>
    <tr>
      <th>39151</th>
      <td>39151</td>
      <td>Shannon Williams</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>84</td>
      <td>73</td>
    </tr>
    <tr>
      <th>39152</th>
      <td>39152</td>
      <td>Lori Moore</td>
      <td>F</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>98</td>
      <td>84</td>
    </tr>
    <tr>
      <th>39153</th>
      <td>39153</td>
      <td>William Hubbard</td>
      <td>M</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>80</td>
      <td>75</td>
    </tr>
    <tr>
      <th>39154</th>
      <td>39154</td>
      <td>Bradley Johnson</td>
      <td>M</td>
      <td>12th</td>
      <td>Thomas High School</td>
      <td>91</td>
      <td>71</td>
    </tr>
    <tr>
      <th>39155</th>
      <td>39155</td>
      <td>John Brooks</td>
      <td>M</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>92</td>
      <td>98</td>
    </tr>
    <tr>
      <th>39156</th>
      <td>39156</td>
      <td>Stephanie Contreras</td>
      <td>F</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>79</td>
      <td>95</td>
    </tr>
    <tr>
      <th>39157</th>
      <td>39157</td>
      <td>Kristen Gonzalez</td>
      <td>F</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>79</td>
      <td>94</td>
    </tr>
    <tr>
      <th>39158</th>
      <td>39158</td>
      <td>Kari Holloway</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>87</td>
      <td>90</td>
    </tr>
    <tr>
      <th>39159</th>
      <td>39159</td>
      <td>Kimberly Cabrera</td>
      <td>F</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>85</td>
      <td>72</td>
    </tr>
    <tr>
      <th>39160</th>
      <td>39160</td>
      <td>Katie Weaver</td>
      <td>F</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>89</td>
      <td>86</td>
    </tr>
    <tr>
      <th>39161</th>
      <td>39161</td>
      <td>April Reyes</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>70</td>
      <td>84</td>
    </tr>
    <tr>
      <th>39162</th>
      <td>39162</td>
      <td>Derek Weeks</td>
      <td>M</td>
      <td>12th</td>
      <td>Thomas High School</td>
      <td>94</td>
      <td>77</td>
    </tr>
    <tr>
      <th>39163</th>
      <td>39163</td>
      <td>John Reese</td>
      <td>M</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>90</td>
      <td>75</td>
    </tr>
    <tr>
      <th>39164</th>
      <td>39164</td>
      <td>Joseph Anthony</td>
      <td>M</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>97</td>
      <td>76</td>
    </tr>
    <tr>
      <th>39165</th>
      <td>39165</td>
      <td>Donna Howard</td>
      <td>F</td>
      <td>12th</td>
      <td>Thomas High School</td>
      <td>99</td>
      <td>90</td>
    </tr>
    <tr>
      <th>39166</th>
      <td>39166</td>
      <td>Dawn Bell</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>95</td>
      <td>70</td>
    </tr>
    <tr>
      <th>39167</th>
      <td>39167</td>
      <td>Rebecca Tanner</td>
      <td>F</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>73</td>
      <td>84</td>
    </tr>
    <tr>
      <th>39168</th>
      <td>39168</td>
      <td>Desiree Kidd</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>99</td>
      <td>90</td>
    </tr>
    <tr>
      <th>39169</th>
      <td>39169</td>
      <td>Carolyn Jackson</td>
      <td>F</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>95</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
<p>39170 rows × 7 columns</p>
</div>




```python
## Rename school and student columns
school_df = school_df.rename(columns={
    "name": "School Name",
    "type": "School Type",
    "size": "School Size",
    "budget":"School Budget", 
})
student_df=student_df.rename(columns={
    "name": "Student Name",
    "gender" : "Student Gender",
    "grade" : "Student Grade",
    "school": "School Name",
    "reading_score":"Reading Score",
    "math_score":"Math Score"
})
```


```python
student_df.head()
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
      <th>Student ID</th>
      <th>Student Name</th>
      <th>Student Gender</th>
      <th>Student Grade</th>
      <th>School Name</th>
      <th>Reading Score</th>
      <th>Math Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_df.head()
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
      <th>School ID</th>
      <th>School Name</th>
      <th>School Type</th>
      <th>School Size</th>
      <th>School Budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
##District Summary - **District Summary**
##* Create a high level snapshot (in table form) of the district's key metrics, including:
 ## * Total Schools
totalschools = (len(school_df))
totalschools
  #* Total Students
totalstudents=(len(student_df))
totalstudents
  #* Total Budget
totalbudget = school_df["School Budget"].sum
totalbudget='${:,.2f}'.format(totalbudget())
totalbudget
  #* Average Math Score
mathavg=student_df["Math Score"].mean
mathavg='{:,.2f}%'.format(mathavg())
mathavg
  #* Average Reading Score
readavg=student_df["Reading Score"].mean
readavg='{:,.2f}%'.format(readavg())
readavg   
  #* % Passing Math
mathpass=student_df.loc[student_df['Math Score'] > 70]
nummathpass = mathpass["Math Score"].count()
pctmatpass= nummathpass/totalstudents * 100
fmtpctmatpass='{:,.2f}%'.format(pctmatpass)

  #* % Passing Reading
readpass=student_df.loc[student_df['Reading Score'] > 70]
numreadpass = readpass["Reading Score"].count()
pctreadpass= numreadpass/totalstudents * 100
fmtpctreadpass='{:,.2f}%'.format(pctreadpass)
print(fmtpctreadpass, fmtpctmatpass)
#* Overall Passing Rate (Average of the above two)
overallpass=(float(pctmatpass)+float(pctreadpass))/2
fmtoverallpass='{:,.2f}%'.format(overallpass)
print(fmtoverallpass)
district_breakdown = pd.DataFrame({
    "Total Schools": [totalschools],
    "Total  Students": [totalstudents],
    "Total Budget": [totalbudget],
    "Avg. Math Score": [mathavg],
    "Avg. Reading Score": [readavg],
    "% Passing Math":[fmtpctmatpass],
    "% Passing Reading":[fmtpctreadpass],
    "Overall Passing Rate": [fmtoverallpass]
})
district_breakdown.head()
```

    82.97% 72.39%
    77.68%





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
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Avg. Math Score</th>
      <th>Avg. Reading Score</th>
      <th>Overall Passing Rate</th>
      <th>Total  Students</th>
      <th>Total Budget</th>
      <th>Total Schools</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>72.39%</td>
      <td>82.97%</td>
      <td>78.99%</td>
      <td>81.88%</td>
      <td>77.68%</td>
      <td>39170</td>
      <td>$24,649,428.00</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
#* Create an overview table that summarizes key metrics about each school, including:
#* School Name
  #* School Type
schooltype_df=school_df[["School Name","School Type", "School Size", "School Budget"]].copy()

#* Total Students
#schoolmetrics_df= pd.DataFrame(student_df["School Name"].value_counts())
#schoolmetrics_df.head()
  #* Total School Budget
  #* Per Student Budget
schooltype_df["Per Student Budget"] = schooltype_df["School Budget"]/schooltype_df["School Size"]
  #* Average Math Score
schoolmathscore = pd.DataFrame(student_df.groupby("School Name")["Math Score"].mean())
schoolmathscore.head()
schooltype_df=schooltype_df.join(schoolmathscore, on='School Name')
schooltype_df.head()
  #* Average Reading Score
schoolreadscore = pd.DataFrame(student_df.groupby("School Name")["Reading Score"].mean())
schoolreadscore.head()
schooltype_df=schooltype_df.join(schoolreadscore, on='School Name')
schooltype_df.head()
  #* % Passing Math
student_df_mathpass = (student_df.loc[(student_df["Math Score"]>70)].groupby
("School Name")["Math Score"].count())
student_df_mathpass.head()
schooltype_df=schooltype_df.merge(student_df_mathpass.to_frame(), left_on="School Name", right_index=True)
schooltype_df["% Passing Math"]=schooltype_df["Math Score_y"]/schooltype_df["School Size"]*100
schooltype_df.head()
student_df_mathpass.head()
#* % Passing Reding)
student_df_readpass = (student_df.loc[(student_df["Reading Score"]>70)].groupby
("School Name")["Reading Score"].count())
schooltype_df=schooltype_df.merge(student_df_readpass.to_frame(), left_on="School Name", right_index=True)
schooltype_df["% Passing Reading"]=schooltype_df["Reading Score_y"]/schooltype_df["School Size"]*100
schooltype_df.head()
student_df_mathpass.head()
  #* Overall Passing Rate (Average of the above two)
schooltype_df["Overall Pass Rate"]=(schooltype_df["% Passing Math"]+schooltype_df["% Passing Reading"])/2

```


```python
schooltype_df.head()
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
      <th>School Name</th>
      <th>School Type</th>
      <th>School Size</th>
      <th>School Budget</th>
      <th>Per Student Budget</th>
      <th>Math Score_x</th>
      <th>Reading Score_x</th>
      <th>Math Score_y</th>
      <th>% Passing Math</th>
      <th>Reading Score_y</th>
      <th>% Passing Reading</th>
      <th>Overall Pass Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>1847</td>
      <td>63.318478</td>
      <td>2299</td>
      <td>78.813850</td>
      <td>71.066164</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>1880</td>
      <td>63.750424</td>
      <td>2313</td>
      <td>78.433367</td>
      <td>71.091896</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>1583</td>
      <td>89.892107</td>
      <td>1631</td>
      <td>92.617831</td>
      <td>91.254969</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>3001</td>
      <td>64.746494</td>
      <td>3624</td>
      <td>78.187702</td>
      <td>71.467098</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>1317</td>
      <td>89.713896</td>
      <td>1371</td>
      <td>93.392371</td>
      <td>91.553134</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_breakdown = pd.DataFrame({
    "School Name": schooltype_df["School Name"],
    "School Type": schooltype_df["School Type"],
    "School Budget": schooltype_df["School Budget"],
    "Per Student Budget": schooltype_df["Per Student Budget"],
    "Avg. Math Score": schooltype_df["Math Score_x"],
     "Avg. Reading Score": schooltype_df["Reading Score_x"],
    "% Passing Math":schooltype_df["% Passing Math"],
    "% Passing Reading":schooltype_df["% Passing Reading"],
    "Overall Passing Rate": schooltype_df["Overall Pass Rate"]
})
```


```python
school_breakdown.head()
school_breakdown.set_index("School Name")
school_breakdown=school_breakdown[["School Name", "School Type", "School Budget", "Per Student Budget", "Avg. Math Score", "Avg. Reading Score", "% Passing Math", "% Passing Reading", "Overall Passing Rate"]]
```


```python
school_breakdown.head(25)
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
      <th>School Name</th>
      <th>School Type</th>
      <th>School Budget</th>
      <th>Per Student Budget</th>
      <th>Avg. Math Score</th>
      <th>Avg. Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>71.066164</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>71.091896</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>89.892107</td>
      <td>92.617831</td>
      <td>91.254969</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>71.467098</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>91.553134</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>92.093736</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>91.711518</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>64.630225</td>
      <td>79.300643</td>
      <td>71.965434</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>248087</td>
      <td>581.0</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>91.686183</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>585858</td>
      <td>609.0</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>91.943867</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>91.861111</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>70.905226</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>71.067003</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>65.753925</td>
      <td>77.510040</td>
      <td>71.631982</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>90.214067</td>
      <td>92.905199</td>
      <td>91.559633</td>
    </tr>
  </tbody>
</table>
</div>




```python
top_schools_df=school_breakdown.sort_values(by="Overall Passing Rate", ascending=False, inplace=False)
```


```python
top_schools_df = top_schools_df.head(5)
top_schools_df
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
      <th>School Name</th>
      <th>School Type</th>
      <th>School Budget</th>
      <th>Per Student Budget</th>
      <th>Avg. Math Score</th>
      <th>Avg. Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>92.093736</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>585858</td>
      <td>609.0</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>91.943867</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>91.861111</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>91.711518</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>248087</td>
      <td>581.0</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>91.686183</td>
    </tr>
  </tbody>
</table>
</div>




```python
bot_schools_df=school_breakdown.sort_values(by="Overall Passing Rate", ascending=True, inplace=False)
```


```python
bot_schools_df=bot_schools_df.head(5)
bot_schools_df
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
      <th>School Name</th>
      <th>School Type</th>
      <th>School Budget</th>
      <th>Per Student Budget</th>
      <th>Avg. Math Score</th>
      <th>Avg. Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>70.905226</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>71.066164</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>71.067003</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>71.091896</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>71.467098</td>
    </tr>
  </tbody>
</table>
</div>




```python
readstudentsbygrade = pd.DataFrame(student_df.groupby("Student Grade")["Reading Score"].mean())
readstudentsbygrade.head()
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
      <th>Reading Score</th>
    </tr>
    <tr>
      <th>Student Grade</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10th</th>
      <td>81.874410</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>81.885714</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>81.819851</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.914358</td>
    </tr>
  </tbody>
</table>
</div>




```python
mathstudentsbygrade = pd.DataFrame(student_df.groupby("Student Grade")["Math Score"].mean())
```


```python
mathstudentsbygrade.head()
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
      <th>Math Score</th>
    </tr>
    <tr>
      <th>Student Grade</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10th</th>
      <td>78.941483</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>79.083548</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>78.993164</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>78.935659</td>
    </tr>
  </tbody>
</table>
</div>




```python
bins = np.linspace(school_breakdown["Per Student Budget"].min(), 
                   school_breakdown["Per Student Budget"].max(), 4)
group_names= ["Low", "Med", "High"]
pd.cut(school_breakdown["Per Student Budget"], bins, labels=group_names)
```




    0     High
    1     High
    2      Low
    3     High
    4      Med
    5      NaN
    6      Low
    7      Med
    8      Low
    9      Med
    10     Low
    11    High
    12    High
    13    High
    14    High
    Name: Per Student Budget, dtype: category
    Categories (3, object): [Low < Med < High]




```python
binnedbudget_df = pd.DataFrame({
    "School Name": school_breakdown["School Name"],
    "Per Student Budget": school_breakdown["Per Student Budget"],
    "Avg. Math Score": school_breakdown["Avg. Math Score"],
     "Avg. Reading Score": school_breakdown["Avg. Reading Score"],
    "% Passing Math":school_breakdown["% Passing Math"],
    "% Passing Reading":school_breakdown["% Passing Reading"],
    "Overall Passing Rate": school_breakdown["Overall Passing Rate"]
})
```


```python
binnedbudget_df["School Spending Summary"]= pd.cut(school_breakdown["Per Student Budget"], bins, labels=group_names)
binnedbudget_df=binnedbudget_df.sort_values(by="School Spending Summary", ascending=True, inplace=False)
binnedbudget_df.set_index(binnedbudget_df["School Name"])
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
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Avg. Math Score</th>
      <th>Avg. Reading Score</th>
      <th>Overall Passing Rate</th>
      <th>Per Student Budget</th>
      <th>School Name</th>
      <th>School Spending Summary</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Wilson High School</th>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>92.093736</td>
      <td>578.0</td>
      <td>Wilson High School</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>89.892107</td>
      <td>92.617831</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>91.254969</td>
      <td>600.0</td>
      <td>Shelton High School</td>
      <td>Low</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>91.711518</td>
      <td>582.0</td>
      <td>Cabrera High School</td>
      <td>Low</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>91.686183</td>
      <td>581.0</td>
      <td>Holden High School</td>
      <td>Low</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>91.861111</td>
      <td>583.0</td>
      <td>Wright High School</td>
      <td>Low</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>91.553134</td>
      <td>625.0</td>
      <td>Griffin High School</td>
      <td>Med</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>64.630225</td>
      <td>79.300643</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>71.965434</td>
      <td>628.0</td>
      <td>Bailey High School</td>
      <td>Med</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>91.943867</td>
      <td>609.0</td>
      <td>Pena High School</td>
      <td>Med</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>71.066164</td>
      <td>655.0</td>
      <td>Huang High School</td>
      <td>High</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>71.091896</td>
      <td>639.0</td>
      <td>Figueroa High School</td>
      <td>High</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>71.467098</td>
      <td>652.0</td>
      <td>Hernandez High School</td>
      <td>High</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>70.905226</td>
      <td>637.0</td>
      <td>Rodriguez High School</td>
      <td>High</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>71.067003</td>
      <td>650.0</td>
      <td>Johnson High School</td>
      <td>High</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>65.753925</td>
      <td>77.510040</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>71.631982</td>
      <td>644.0</td>
      <td>Ford High School</td>
      <td>High</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>90.214067</td>
      <td>92.905199</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>91.559633</td>
      <td>638.0</td>
      <td>Thomas High School</td>
      <td>High</td>
    </tr>
  </tbody>
</table>
</div>




```python
bins = np.linspace(schooltype_df["School Size"].min(), 
                   schooltype_df["School Size"].max(), 4)
group_names= ["Small", "Med", "Large"]
pd.cut(schooltype_df["School Size"], bins, labels=group_names)
```




    0       Med
    1       Med
    2     Small
    3     Large
    4     Small
    5       Med
    6     Small
    7     Large
    8       NaN
    9     Small
    10    Small
    11    Large
    12    Large
    13      Med
    14    Small
    Name: School Size, dtype: category
    Categories (3, object): [Small < Med < Large]




```python
binnedsize_df = pd.DataFrame({
    "School Name": school_breakdown["School Name"],
    "School Type": school_breakdown["School Type"],
    "School Size": school_df["School Size"],
    "Avg. Math Score": school_breakdown["Avg. Math Score"],
     "Avg. Reading Score": school_breakdown["Avg. Reading Score"],
    "% Passing Math":school_breakdown["% Passing Math"],
    "% Passing Reading":school_breakdown["% Passing Reading"],
    "Overall Passing Rate": school_breakdown["Overall Passing Rate"]
})
binnedsize_df.set_index(binnedsize_df["School Name"])
binnedsize_df["School Size Summary"]= pd.cut(schooltype_df["School Size"], bins, labels=group_names)
```


```python
binnedsize_df.head(25)
binned_group=binnedsize_df.groupby("School Size Summary", as_index=True, sort=True)
binned_group.head()
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
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Avg. Math Score</th>
      <th>Avg. Reading Score</th>
      <th>Overall Passing Rate</th>
      <th>School Name</th>
      <th>School Size</th>
      <th>School Type</th>
      <th>School Size Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>71.066164</td>
      <td>Huang High School</td>
      <td>2917</td>
      <td>District</td>
      <td>Med</td>
    </tr>
    <tr>
      <th>1</th>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>71.091896</td>
      <td>Figueroa High School</td>
      <td>2949</td>
      <td>District</td>
      <td>Med</td>
    </tr>
    <tr>
      <th>2</th>
      <td>89.892107</td>
      <td>92.617831</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>91.254969</td>
      <td>Shelton High School</td>
      <td>1761</td>
      <td>Charter</td>
      <td>Small</td>
    </tr>
    <tr>
      <th>3</th>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>71.467098</td>
      <td>Hernandez High School</td>
      <td>4635</td>
      <td>District</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>4</th>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>91.553134</td>
      <td>Griffin High School</td>
      <td>1468</td>
      <td>Charter</td>
      <td>Small</td>
    </tr>
    <tr>
      <th>5</th>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>92.093736</td>
      <td>Wilson High School</td>
      <td>2283</td>
      <td>Charter</td>
      <td>Med</td>
    </tr>
    <tr>
      <th>6</th>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>91.711518</td>
      <td>Cabrera High School</td>
      <td>1858</td>
      <td>Charter</td>
      <td>Small</td>
    </tr>
    <tr>
      <th>7</th>
      <td>64.630225</td>
      <td>79.300643</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>71.965434</td>
      <td>Bailey High School</td>
      <td>4976</td>
      <td>District</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>8</th>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>91.686183</td>
      <td>Holden High School</td>
      <td>427</td>
      <td>Charter</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>91.943867</td>
      <td>Pena High School</td>
      <td>962</td>
      <td>Charter</td>
      <td>Small</td>
    </tr>
    <tr>
      <th>10</th>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>91.861111</td>
      <td>Wright High School</td>
      <td>1800</td>
      <td>Charter</td>
      <td>Small</td>
    </tr>
    <tr>
      <th>11</th>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>70.905226</td>
      <td>Rodriguez High School</td>
      <td>3999</td>
      <td>District</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>12</th>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>71.067003</td>
      <td>Johnson High School</td>
      <td>4761</td>
      <td>District</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>13</th>
      <td>65.753925</td>
      <td>77.510040</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>71.631982</td>
      <td>Ford High School</td>
      <td>2739</td>
      <td>District</td>
      <td>Med</td>
    </tr>
  </tbody>
</table>
</div>




```python
binnedtype_df = pd.DataFrame({
    "School Name": school_breakdown["School Name"],
    "School Type": school_df["School Type"],
    "Avg. Math Score": school_breakdown["Avg. Math Score"],
     "Avg. Reading Score": school_breakdown["Avg. Reading Score"],
    "% Passing Math":school_breakdown["% Passing Math"],
    "% Passing Reading":school_breakdown["% Passing Reading"],
    "Overall Passing Rate": school_breakdown["Overall Passing Rate"]
})

binnedtype_df.head()
binned_group=binnedtype_df.groupby("School Type")
binned_group.head()
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
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Avg. Math Score</th>
      <th>Avg. Reading Score</th>
      <th>Overall Passing Rate</th>
      <th>School Name</th>
      <th>School Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>71.066164</td>
      <td>Huang High School</td>
      <td>District</td>
    </tr>
    <tr>
      <th>1</th>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>71.091896</td>
      <td>Figueroa High School</td>
      <td>District</td>
    </tr>
    <tr>
      <th>2</th>
      <td>89.892107</td>
      <td>92.617831</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>91.254969</td>
      <td>Shelton High School</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>3</th>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>71.467098</td>
      <td>Hernandez High School</td>
      <td>District</td>
    </tr>
    <tr>
      <th>4</th>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>91.553134</td>
      <td>Griffin High School</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>5</th>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>92.093736</td>
      <td>Wilson High School</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>6</th>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>91.711518</td>
      <td>Cabrera High School</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>7</th>
      <td>64.630225</td>
      <td>79.300643</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>71.965434</td>
      <td>Bailey High School</td>
      <td>District</td>
    </tr>
    <tr>
      <th>8</th>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>91.686183</td>
      <td>Holden High School</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>11</th>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>70.905226</td>
      <td>Rodriguez High School</td>
      <td>District</td>
    </tr>
  </tbody>
</table>
</div>


