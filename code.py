import pandas
import json


csv = pandas.read_csv("StudentsPerformance.csv")

average_in_math = (csv[['math score']].mean()).to_string(index=False)
reading_score = (csv[['reading score']].mean()).to_string(index=False)
writing_score = (csv[['writing score']].mean()).to_string(index=False)



unique_values = list(csv['parental level of education'].unique())


values_on_json ={
    "education_levels":unique_values,
    "scores" : {
        "average":{
            "math_score":average_in_math,
            "reading_score":reading_score,
            "writing_score":writing_score
        }
    }
}


with open("output.json","w") as json_file:
    json.dump(values_on_json,json_file)