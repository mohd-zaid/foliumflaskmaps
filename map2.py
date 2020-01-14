import folium
import os
import pandas as pd
from flask import Flask, render_template
import args

app = Flask(__name__)

@app.route('/')
def index():
    flag = 0 
    if flag:
        indianStates = os.path.join('data1', 'india_state.geojson')
        Protestf = os.path.join('data1', "geoMap.csv")

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

        map.save('templates/index1.html')
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)   
