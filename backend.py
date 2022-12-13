import requests
import datetime


API_KEY = '9069b38bca18dd5bf8199f67aca0cc16'


def get_data(place, forecast_days = 1, kind = 'Temperature'):
    URL_LINK = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url=URL_LINK,verify=False)
    result = response.json()

    date_local = []
    temp_local = []

    date_start = ''
    date_end = ''
    fmat = "%Y-%m-%d %H:%M:%S"

    if place != '' and kind == 'Temperature':
        items = result.get('list')
        
        for index, item in enumerate(items):
            if index == 0:
                date_start = datetime.datetime.strptime(item['dt_txt'], fmat)
                date_end = date_start + datetime.timedelta(days = forecast_days)
                temp_local.append(item['main'].get('temp')/10)
                date_local.append(item['dt_txt'])
            else:
                if datetime.datetime.strptime(item['dt_txt'], fmat) <= date_end:
                   temp_local.append(item['main'].get('temp')/10)
                   date_local.append(item['dt_txt'])
                else:
                    break
    elif place != '' and kind == 'Sky':
        items = result.get('list')
        
        for index, item in enumerate(items):
            if index == 0:
                date_start = datetime.datetime.strptime(item['dt_txt'], fmat)
                date_end = date_start + datetime.timedelta(days = forecast_days)
                temp_local.append(item['weather'][0].get('main'))
                date_local.append(item['dt_txt'])
            else:
                if datetime.datetime.strptime(item['dt_txt'], fmat) <= date_end:
                    temp_local.append(item['weather'][0].get('main'))
                    date_local.append(item['dt_txt'])
                else:
                    break      

    return date_local, temp_local


if __name__ == '__main__':
    print(get_data(place='Tokyo'))
