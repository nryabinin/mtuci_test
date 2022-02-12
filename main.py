import requests

city = 'Moscow,RU'
appid = 'ff12325a55a5aaf19e8a5525e3ea3383'

current_forecast = requests.get('http://api.openweathermap.org/data/2.5/weather', params={'q': city, 'units':'metric', 'lang':'ru', 'APPID':appid})
weather_forecast = requests.get('http://api.openweathermap.org/data/2.5/forecast', params={'q': city, 'units':'metric', 'lang':'ru', 'APPID':appid})

data_current = current_forecast.json()
data_forecast = weather_forecast.json()


print('Текущий прогноз:')
print('Город', city)
print('Погодные условия: ', data_current['weather'][0]['description'])
print('Температура: ', data_current['main']['temp'])
print('Минимальная температура: ', data_current['main']['temp_min'])
print('Максимальная температура: ', data_current['main']['temp_max'])
print('Скорость ветра: ', data_current['wind']['speed'])
print('Видимость: ', data_current['visibility'])

print('\n========================================\n')

print('Прогноз на неделю')
for i in data_forecast['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
          '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
          i['weather'][0]['description'], ">\r\nСкорость ветра: <",
          i['wind']['speed'], ">\r\nВидимость: <",
          i['visibility'], ">")
    print('-------------------------')
