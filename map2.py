import folium
import os
import pandas as pd
import flask

@app.route('/')
def index():
  indianStates = os.path.join('data1', 'indiaStates.json')
  Protestf = os.path.join('data1', 'geoMap.csv')

  searchRes = pd.read_csv(Protestf)

  # print(searchRes)
  map = folium.Map(location=[21.7679,  78.8718],
                   zoom_start=5.4, tiles='openstreetmap')
  folium.Choropleth(
      geo_data=indianStates,
      name='Protest Rate',
      data=searchRes,
      columns=['Region', 'Protest'],
      key_on='feature.properties.NAME_1',
      fill_color='PuBu',
      fill_opacity=1,
      line_opacity=1,
      nan_fill_color='#f2efe'
  ).add_to(map)
  map.save('index1.html')
  
return map._repr_html_()

if '__name__' == '__main__':
  app.run(debug=True)
