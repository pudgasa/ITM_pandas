import pandas as pdimport matplotlib.pyplot as pltimport pathlibfrom pathlib import Pathimport numpy as npdef download_weather_month(year, month):    url = url_template.format(year=year, month=month)    weather_data = pd.read_csv(url, sep=',', encoding='latin1', index_col=['Date/Time (LST)'], parse_dates=True)    weather_data = weather_data.dropna(axis=1)    weather_data.columns = [col.replace('\xb0', '') for col in weather_data.columns]    weather_data = weather_data.drop(['Year', 'Month', 'Day'], axis=1)    return weather_datawork_path = pathlib.Path.cwd()pd.options.display.max_rows = 7plt.style.use('ggplot')plt.rcParams['figure.figsize'] = (15, 3)plt.rcParams['font.family'] = 'sans-serif'url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"url = url_template.format(month=3, year=2012)weather_mar2012 = pd.read_csv(url, sep=',', encoding='latin1', index_col=['Date/Time (LST)'], parse_dates=True)#print(weather_mar2012)weather_mar2012["Temp (Â°C)"].plot(figsize=(15, 5))weather_mar2012.columns = [    u'Year', u'Month', u'Day', u'Time', u'Data Quality', u'Temp (C)',    u'Temp Flag', u'Dew Point Temp (C)', u'Dew Point Temp Flag',    u'Rel Hum (%)', u'Rel Hum Flag', u'Wind Dir (10s deg)', u'Wind Dir Flag',    u'Wind Spd (km/h)', u'Wind Spd Flag', u'Visibility (km)', u'Visibility Flag',    u'Stn Press (kPa)', u'Stn Press Flag', u'Hmdx', u'Hmdx Flag', u'Wind Chill',    u'Wind Chill Flag', u'Weather', u'', u'', u'', u'', u'']weather_mar2012 = weather_mar2012.dropna(axis=1, how='any')weather_mar2012 = weather_mar2012.drop(['Year', 'Month', 'Day'], axis=1)#print(weather_mar2012[:5])temperatures = weather_mar2012[[u'Temp (C)']].copy()temperatures.loc[:, 'Hour'] = weather_mar2012.index.hourtemperatures.groupby('Hour').aggregate(np.median).plot()#plt.show()print(download_weather_month(2012, 1)[:5])data_by_month = [download_weather_month(2012, i) for i in range(1, 13)]weather_2012 = pd.concat(data_by_month)print(weather_2012)weather_2012.to_csv(work_path, 'datasets', 'weather_2012.csv')