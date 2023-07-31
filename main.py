#code developed by M.UDHAYAKUMAR
#-----------------------------------------------------MODULES,PACKAGES IMPORTING----------------------------------------
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#-----------------------------------------------------API ACCESSING-----------------------------------------------------
end_point="https://api.openweathermap.org/data/2.5/forecast"
api_key="8c81c4a2f6b7546cac7913f74b54311c"
weather_parmeter={
"lat":9.9261153,"lon":78.1140983,"appid":api_key,
}
res=requests.get(end_point,params=weather_parmeter)
weather_data=res.json()
full_data=weather_data["list"][:40]

print(full_data)
#-------------------------------------------------------WRITING WEATHER DATAS___________________________________________
with open(file="weather_data.csv", mode='w') as file:
    contents = file.write(f'temperature,date,weather,humidity,wind_speed\n')
data=0
for i in range(40):
    temperature=full_data[data]["main"]["temp"]
    celsius_temperature=round(temperature-273.15)
    weather_time = full_data[data]["dt_txt"]
    weather_name = full_data[data]["weather"][0]["description"]
    hum = full_data[data]["main"]["humidity"]
    wind =full_data[data]["wind"]["speed"]

    data+=1
    with open(file="weather_data.csv",mode='a') as file:
          contents=file.write(str(f'{celsius_temperature},{weather_time},{weather_name},{hum},{wind}\n'))

#-------------------------------------------------------DATA ANALYSIS & VISUALIZATATION---------------------------------
read_data=pd.read_csv("weather_data.csv")
plt.scatter(read_data["temperature"],read_data["date"],c="red")
plt.title("Scatter plot of  WEATHER temperature in coming days")
plt.xlabel("TEMPERATURE")
plt.ylabel("DATES")
plt.show()

sns.set(style="darkgrid")
sns.countplot(x="temperature",data=read_data,hue="weather")
plt.show()


read_data=pd.read_csv("weather_data.csv")
plt.plot(read_data["humidity"])
plt.title(" plot of  humidity days")
plt.xlabel("humidity")
plt.ylabel("counts")
plt.show()



read_data=pd.read_csv("weather_data.csv")
plt.plot(read_data["wind_speed"],c="red")
plt.title(" plot of wind speed days")
plt.xlabel("wind speed MPH")
plt.ylabel("counts")
plt.show()
print("code developed by UDHAYAKUMAR")