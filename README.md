# AUSFIRE

A visualization of 19/20 Australian Bushfires, part of the [Interactive Data Visualization (ECL MOS 5.5)](https://github.com/LyonDataViz/MOS5.5-Dataviz) course.

*Link :* https://melkarmo.github.io/AUSFIRE/

## Participants

* EL KAMEL Rima ([RimaElkamel](https://github.com/RimaElkamel))
* EL KARMOUDI Moncef ([melkarmo](https://github.com/melkarmo))
* MENARD Nicolas ([MENARDM](https://github.com/MENARDN))

## Description of the project

This project consists on the visualization of the 19/20 Australian Bushfires evolution from October 2019 to 11th January 2020 by state.  
* Each state is displayed as a grid which total area is defined according to its forest cover area. 
* Each cell of a grid shows a freshly-burning area, an already-burning area, or a sane area.

## Screenshot

![image](https://melkarmo.github.io/AUSFIRE/images/screenshot.PNG)

## Data

The main data source used for our project is the [Fires from Space: Australia](https://www.kaggle.com/carlosparadis/fires-from-space-australia-and-new-zeland#fire_nrt_M6_96619.csv) dataset which consists of fire starts detected by NASA MODIS satellite : the dataset includes the geolocalisation of these fire starts (latitude, longitude), and the mean temperature and the power of the fires at each location.

Australian states' data (name, area, forest cover, population) was found by a basic Wikipedia search.

We then processed the data to group the fire starts by Australian state. The final datasets are located in the `bystate` file, and states' data is included in the `index.html` code as it only consists of 7 states.

## Credits

Thank you for your help !

* NASA for making the data public, and kaggler [Carlos Paradis](https://www.kaggle.com/carlosparadis) for making it easy to access ([here](https://www.kaggle.com/carlosparadis/fires-from-space-australia-and-new-zeland#fire_nrt_M6_96619.csv));

* Wikipedia for Australian states' related [data](https://en.wikipedia.org/wiki/Forest_cover_by_state_or_territory_in_Australia);

* [Ajay Thampi](https://github.com/thampiman) for the [Reverse Geocoder](https://github.com/thampiman/reverse-geocoder) python package that allows offline and quick reverse geocoding on massive data;

* [Trifacta](https://www.trifacta.com/fr/) for their easy-to-use data wrangling tool, free for student;

* [Let's Make a Grid with D3.js](https://bl.ocks.org/cagrimmett/07f8c8daea00946b9e704e3efcbd5739);

* [D3 HTML Range Slider Play/Pause](https://jsfiddle.net/bfbun6cc/4/);

* [Rect Collision](http://bl.ocks.org/natebates/273b99ddf86e2e2e58ff);

* [Flaticon](https://www.flaticon.com/)'s flame icon;

* LyonDataViz and Centrale Lyon for the Interactive DataViz [course](https://github.com/LyonDataViz/MOS5.5-Dataviz).