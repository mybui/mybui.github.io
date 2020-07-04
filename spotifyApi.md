## Spotify is a digital music, podcast, and video streaming service that gives you access to millions of songs and other content from artists all over the world. This data set explores Spotify API of a specific artist, and her artwork.


```python
import requests
import pandas as pd
import numpy as np
```


```python
headers = {"Authorization": "Bearer BQCFC1O8XU3m2gR6ho7QPGRq8nBPfiE08yd5etPAl-vJ9lmVkP0w4xVmA0c_cHe-rT6GhLtGtyp89cPTSH4"}
```

### Looking for artist Adele


```python
adele_info = requests.get('https://api.spotify.com/v1/search?q=adele&type=artist', headers=headers)
```

The get request resulted in all artists matching search keyword 'adele' 


```python
adele_results = adele_info.json()
adele_results
```




    {'artists': {'href': 'https://api.spotify.com/v1/search?query=adele&type=artist&offset=0&limit=20',
      'items': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY'},
        'followers': {'href': None, 'total': 21880591},
        'genres': ['british soul', 'pop', 'uk pop'],
        'href': 'https://api.spotify.com/v1/artists/4dpARuHxo51G3z768sgnrY',
        'id': '4dpARuHxo51G3z768sgnrY',
        'images': [{'height': 1000,
          'url': 'https://i.scdn.co/image/ccbe7b4fef679f821988c78dbd4734471834e3d9',
          'width': 1000},
         {'height': 640,
          'url': 'https://i.scdn.co/image/f8737f6fda048b45efe91f81c2bda2b601ae689c',
          'width': 640},
         {'height': 200,
          'url': 'https://i.scdn.co/image/df070ad127f62d682596e515ac69d5bef56e0897',
          'width': 200},
         {'height': 64,
          'url': 'https://i.scdn.co/image/cbbdfb209cc38b2999b1882f42ee642555316313',
          'width': 64}],
        'name': 'Adele',
        'popularity': 86,
        'type': 'artist',
        'uri': 'spotify:artist:4dpARuHxo51G3z768sgnrY'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/5yUp79jSBSGdkbufl2hmcY'},
        'followers': {'href': None, 'total': 805},
        'genres': ['violin'],
        'href': 'https://api.spotify.com/v1/artists/5yUp79jSBSGdkbufl2hmcY',
        'id': '5yUp79jSBSGdkbufl2hmcY',
        'images': [{'height': 1000,
          'url': 'https://i.scdn.co/image/f872ff81d488a571190f9e3ab162db15361f7060',
          'width': 1000},
         {'height': 640,
          'url': 'https://i.scdn.co/image/cdc5a89e78fff546f1939e7dd68904bd061b36f9',
          'width': 640},
         {'height': 200,
          'url': 'https://i.scdn.co/image/1edaaef2eaefbf2bfb6a530e5464e40e5f398819',
          'width': 200},
         {'height': 64,
          'url': 'https://i.scdn.co/image/4cab46ac52af13c19ecf94b9b36197fc4c09e664',
          'width': 64}],
        'name': 'Adele Anthony',
        'popularity': 27,
        'type': 'artist',
        'uri': 'spotify:artist:5yUp79jSBSGdkbufl2hmcY'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/4AEv9RpfPAr67W04LqWLDb'},
        'followers': {'href': None, 'total': 119},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/4AEv9RpfPAr67W04LqWLDb',
        'id': '4AEv9RpfPAr67W04LqWLDb',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273178aa240560f208a694b5717',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02178aa240560f208a694b5717',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851178aa240560f208a694b5717',
          'width': 64}],
        'name': 'Adele Roberts',
        'popularity': 30,
        'type': 'artist',
        'uri': 'spotify:artist:4AEv9RpfPAr67W04LqWLDb'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/4z6kZb2cYPUxzVyzpNCKDj'},
        'followers': {'href': None, 'total': 182},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/4z6kZb2cYPUxzVyzpNCKDj',
        'id': '4z6kZb2cYPUxzVyzpNCKDj',
        'images': [],
        'name': 'Adele Haenel',
        'popularity': 34,
        'type': 'artist',
        'uri': 'spotify:artist:4z6kZb2cYPUxzVyzpNCKDj'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/6bE0b3Rf90szzcwv0qs227'},
        'followers': {'href': None, 'total': 327},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/6bE0b3Rf90szzcwv0qs227',
        'id': '6bE0b3Rf90szzcwv0qs227',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273165c9c33710fddf07428e6e0',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02165c9c33710fddf07428e6e0',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851165c9c33710fddf07428e6e0',
          'width': 64}],
        'name': 'Adele Kraic',
        'popularity': 21,
        'type': 'artist',
        'uri': 'spotify:artist:6bE0b3Rf90szzcwv0qs227'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/1ZxfPXwVNFPWZHWs5EyGNB'},
        'followers': {'href': None, 'total': 2},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/1ZxfPXwVNFPWZHWs5EyGNB',
        'id': '1ZxfPXwVNFPWZHWs5EyGNB',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b27314067d5c18573cf54e3f62cd',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e0214067d5c18573cf54e3f62cd',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d0000485114067d5c18573cf54e3f62cd',
          'width': 64}],
        'name': 'Adele K',
        'popularity': 17,
        'type': 'artist',
        'uri': 'spotify:artist:1ZxfPXwVNFPWZHWs5EyGNB'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/0UhoqhbYoPuORgj24VBUcp'},
        'followers': {'href': None, 'total': 205},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/0UhoqhbYoPuORgj24VBUcp',
        'id': '0UhoqhbYoPuORgj24VBUcp',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273f6a15fc6db4a2038a4059b82',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02f6a15fc6db4a2038a4059b82',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851f6a15fc6db4a2038a4059b82',
          'width': 64}],
        'name': 'Adèle Anderson',
        'popularity': 20,
        'type': 'artist',
        'uri': 'spotify:artist:0UhoqhbYoPuORgj24VBUcp'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/7wm3zwQUO1hPk4m4sOUz1E'},
        'followers': {'href': None, 'total': 53},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/7wm3zwQUO1hPk4m4sOUz1E',
        'id': '7wm3zwQUO1hPk4m4sOUz1E',
        'images': [],
        'name': 'Adèle Carlier',
        'popularity': 21,
        'type': 'artist',
        'uri': 'spotify:artist:7wm3zwQUO1hPk4m4sOUz1E'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/2qS6cYzM5ajhprcxQa1Ilc'},
        'followers': {'href': None, 'total': 31203},
        'genres': ['norwegian pop', 'scandipop'],
        'href': 'https://api.spotify.com/v1/artists/2qS6cYzM5ajhprcxQa1Ilc',
        'id': '2qS6cYzM5ajhprcxQa1Ilc',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/e609d6033b6150755f26a1c31d74c25d0a238ddb',
          'width': 640},
         {'height': 320,
          'url': 'https://i.scdn.co/image/538aca539b7e2cc0476913270b27174cf0eba76e',
          'width': 320},
         {'height': 160,
          'url': 'https://i.scdn.co/image/5800cb8f767751161ea3265694f8d900c824137c',
          'width': 160}],
        'name': 'Adelén',
        'popularity': 43,
        'type': 'artist',
        'uri': 'spotify:artist:2qS6cYzM5ajhprcxQa1Ilc'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/6HZ5IH5ksF7cs4mg0HQlSN'},
        'followers': {'href': None, 'total': 1468},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/6HZ5IH5ksF7cs4mg0HQlSN',
        'id': '6HZ5IH5ksF7cs4mg0HQlSN',
        'images': [],
        'name': 'Adele Adkins',
        'popularity': 23,
        'type': 'artist',
        'uri': 'spotify:artist:6HZ5IH5ksF7cs4mg0HQlSN'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/19RHMn8FFkEFmhPwyDW2ZC'},
        'followers': {'href': None, 'total': 31595},
        'genres': ['cabaret'],
        'href': 'https://api.spotify.com/v1/artists/19RHMn8FFkEFmhPwyDW2ZC',
        'id': '19RHMn8FFkEFmhPwyDW2ZC',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ca1b7900859930a1ffd8bde7d67647ea3d141b26',
          'width': 640},
         {'height': 320,
          'url': 'https://i.scdn.co/image/fc6cb619b190b271c6fedffd3eb028224f649e32',
          'width': 320},
         {'height': 160,
          'url': 'https://i.scdn.co/image/312f2f048d0516d3d24afd3c761855ebab0a4083',
          'width': 160}],
        'name': 'Robyn Adele Anderson',
        'popularity': 48,
        'type': 'artist',
        'uri': 'spotify:artist:19RHMn8FFkEFmhPwyDW2ZC'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/06wuY3VLVdOEyRLGGpHIqK'},
        'followers': {'href': None, 'total': 2997},
        'genres': ['lovers rock'],
        'href': 'https://api.spotify.com/v1/artists/06wuY3VLVdOEyRLGGpHIqK',
        'id': '06wuY3VLVdOEyRLGGpHIqK',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/d99231d0b262f95807efb39c7b356eac1270f01f',
          'width': 640},
         {'height': 320,
          'url': 'https://i.scdn.co/image/c1e4ac429079dd88ddf34e0f00e7b61288026c91',
          'width': 320},
         {'height': 160,
          'url': 'https://i.scdn.co/image/4b556c170676b2bb1bac9d318a58d15d787080c6',
          'width': 160}],
        'name': 'Adele Harley',
        'popularity': 21,
        'type': 'artist',
        'uri': 'spotify:artist:06wuY3VLVdOEyRLGGpHIqK'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/1kivdQIreUXoEYFwEuf8FP'},
        'followers': {'href': None, 'total': 1869},
        'genres': ['didgeridoo'],
        'href': 'https://api.spotify.com/v1/artists/1kivdQIreUXoEYFwEuf8FP',
        'id': '1kivdQIreUXoEYFwEuf8FP',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273f17a4246033ab974acfbe586',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02f17a4246033ab974acfbe586',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851f17a4246033ab974acfbe586',
          'width': 64}],
        'name': 'Adèle & Zalem',
        'popularity': 17,
        'type': 'artist',
        'uri': 'spotify:artist:1kivdQIreUXoEYFwEuf8FP'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/0Snj97D6oJSBTqBePPLmOt'},
        'followers': {'href': None, 'total': 3},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/0Snj97D6oJSBTqBePPLmOt',
        'id': '0Snj97D6oJSBTqBePPLmOt',
        'images': [],
        'name': 'Adele Ange',
        'popularity': 5,
        'type': 'artist',
        'uri': 'spotify:artist:0Snj97D6oJSBTqBePPLmOt'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/0efwUZapTfJs8BJHoJKUke'},
        'followers': {'href': None, 'total': 68},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/0efwUZapTfJs8BJHoJKUke',
        'id': '0efwUZapTfJs8BJHoJKUke',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b2732fe1c5901e207da0e87543c5',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e022fe1c5901e207da0e87543c5',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d000048512fe1c5901e207da0e87543c5',
          'width': 64}],
        'name': 'Adele Addison',
        'popularity': 10,
        'type': 'artist',
        'uri': 'spotify:artist:0efwUZapTfJs8BJHoJKUke'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/1fneR6LDxl9hclxo1OP2BP'},
        'followers': {'href': None, 'total': 381},
        'genres': ['spiritual jazz'],
        'href': 'https://api.spotify.com/v1/artists/1fneR6LDxl9hclxo1OP2BP',
        'id': '1fneR6LDxl9hclxo1OP2BP',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b27325c8d3d053610c860774dfc5',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e0225c8d3d053610c860774dfc5',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d0000485125c8d3d053610c860774dfc5',
          'width': 64}],
        'name': 'Adele Sebastian',
        'popularity': 10,
        'type': 'artist',
        'uri': 'spotify:artist:1fneR6LDxl9hclxo1OP2BP'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/5zEh5XsQAkg0iUY3vPNU0l'},
        'followers': {'href': None, 'total': 440},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/5zEh5XsQAkg0iUY3vPNU0l',
        'id': '5zEh5XsQAkg0iUY3vPNU0l',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/e1f6bd76a8b250b4c017d4401f5926d9a15a8b23',
          'width': 640},
         {'height': 320,
          'url': 'https://i.scdn.co/image/89f855a6de811cbc8bfa178964a8c2e943c82395',
          'width': 320},
         {'height': 160,
          'url': 'https://i.scdn.co/image/553691a82a096e04cca9374da60ebd21c69a1e56',
          'width': 160}],
        'name': 'Ester Adele',
        'popularity': 28,
        'type': 'artist',
        'uri': 'spotify:artist:5zEh5XsQAkg0iUY3vPNU0l'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/6j7j0we7GM2loyhC0C59Zs'},
        'followers': {'href': None, 'total': 3},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/6j7j0we7GM2loyhC0C59Zs',
        'id': '6j7j0we7GM2loyhC0C59Zs',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b2734f6a622618eb207e48e26bf4',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e024f6a622618eb207e48e26bf4',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d000048514f6a622618eb207e48e26bf4',
          'width': 64}],
        'name': 'Adele Legge',
        'popularity': 12,
        'type': 'artist',
        'uri': 'spotify:artist:6j7j0we7GM2loyhC0C59Zs'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/71gkxf3mxb8HEupKuGYMGm'},
        'followers': {'href': None, 'total': 291},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/71gkxf3mxb8HEupKuGYMGm',
        'id': '71gkxf3mxb8HEupKuGYMGm',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273c776a7976ce3af1c2a968015',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02c776a7976ce3af1c2a968015',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851c776a7976ce3af1c2a968015',
          'width': 64}],
        'name': 'Adele Erichsen',
        'popularity': 7,
        'type': 'artist',
        'uri': 'spotify:artist:71gkxf3mxb8HEupKuGYMGm'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/47QUMjUHSLtvWMvqfr0DoM'},
        'followers': {'href': None, 'total': 6},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/47QUMjUHSLtvWMvqfr0DoM',
        'id': '47QUMjUHSLtvWMvqfr0DoM',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273df907b4821ff007a9b74ec2b',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02df907b4821ff007a9b74ec2b',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851df907b4821ff007a9b74ec2b',
          'width': 64}],
        'name': 'Adele Bardazzi',
        'popularity': 8,
        'type': 'artist',
        'uri': 'spotify:artist:47QUMjUHSLtvWMvqfr0DoM'}],
      'limit': 20,
      'next': 'https://api.spotify.com/v1/search?query=adele&type=artist&offset=20&limit=20',
      'offset': 0,
      'previous': None,
      'total': 278}}



There are 278 artist names that match 'adele'. We're only interested in Adele who sings pop and r&b from the U.K., and presumably the most famous of all.


```python
adele_results['artists']['total']
```




    278




```python
adele_results['artists']['items'][0]
```




    {'external_urls': {'spotify': 'https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY'},
     'followers': {'href': None, 'total': 21880591},
     'genres': ['british soul', 'pop', 'uk pop'],
     'href': 'https://api.spotify.com/v1/artists/4dpARuHxo51G3z768sgnrY',
     'id': '4dpARuHxo51G3z768sgnrY',
     'images': [{'height': 1000,
       'url': 'https://i.scdn.co/image/ccbe7b4fef679f821988c78dbd4734471834e3d9',
       'width': 1000},
      {'height': 640,
       'url': 'https://i.scdn.co/image/f8737f6fda048b45efe91f81c2bda2b601ae689c',
       'width': 640},
      {'height': 200,
       'url': 'https://i.scdn.co/image/df070ad127f62d682596e515ac69d5bef56e0897',
       'width': 200},
      {'height': 64,
       'url': 'https://i.scdn.co/image/cbbdfb209cc38b2999b1882f42ee642555316313',
       'width': 64}],
     'name': 'Adele',
     'popularity': 86,
     'type': 'artist',
     'uri': 'spotify:artist:4dpARuHxo51G3z768sgnrY'}



Adele has id '4dpARuHxo51G3z768sgnrY'. This is the information we need to proceed with all api queries related to Adele.

### List all Adele albums and singles


```python
i = requests.get('https://api.spotify.com/v1/artists/4dpARuHxo51G3z768sgnrY/albums', headers=headers)
holder = ['https://api.spotify.com/v1/artists/4dpARuHxo51G3z768sgnrY/albums']
while i.json()['next'] != None:
    holder.append(i.json()['next'])
    i = requests.get(i.json()['next'], headers=headers)
```


```python
n = [requests.get(i, headers=headers).json() for i in holder]
```


```python
everything = pd.DataFrame([[i['name'] for m in n for i in m['items']], 
                           [i['album_type'] for m in n for i in m['items']],
                           [len(i['available_markets']) for m in n for i in m['items']]]).T
```


```python
everything.columns = ['name', 'type', 'countries released']
everything
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>type</th>
      <th>countries released</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>album</td>
      <td>18</td>
    </tr>
    <tr>
      <th>1</th>
      <td>25</td>
      <td>album</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21</td>
      <td>album</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>album</td>
      <td>18</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21</td>
      <td>album</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>21</td>
      <td>album</td>
      <td>61</td>
    </tr>
    <tr>
      <th>6</th>
      <td>19</td>
      <td>album</td>
      <td>18</td>
    </tr>
    <tr>
      <th>7</th>
      <td>19</td>
      <td>album</td>
      <td>61</td>
    </tr>
    <tr>
      <th>8</th>
      <td>19</td>
      <td>album</td>
      <td>3</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19</td>
      <td>album</td>
      <td>54</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Water Under the Bridge</td>
      <td>single</td>
      <td>18</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Water Under the Bridge</td>
      <td>single</td>
      <td>61</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Send My Love (To Your New Lover)</td>
      <td>single</td>
      <td>18</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Send My Love (To Your New Lover)</td>
      <td>single</td>
      <td>61</td>
    </tr>
    <tr>
      <th>14</th>
      <td>When We Were Young</td>
      <td>single</td>
      <td>18</td>
    </tr>
    <tr>
      <th>15</th>
      <td>When We Were Young</td>
      <td>single</td>
      <td>61</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Hello</td>
      <td>single</td>
      <td>18</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Hello</td>
      <td>single</td>
      <td>61</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Skyfall</td>
      <td>single</td>
      <td>79</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Set Fire to the Rain</td>
      <td>single</td>
      <td>61</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Rolling In The Deep</td>
      <td>single</td>
      <td>61</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Rolling In The Deep</td>
      <td>single</td>
      <td>1</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Make You Feel My Love</td>
      <td>single</td>
      <td>18</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Make You Feel My Love</td>
      <td>single</td>
      <td>61</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Hometown Glory</td>
      <td>single</td>
      <td>61</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Cold Shoulder</td>
      <td>single</td>
      <td>2</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Cold Shoulder</td>
      <td>single</td>
      <td>4</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Cold Shoulder</td>
      <td>single</td>
      <td>2</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Cold Shoulder</td>
      <td>single</td>
      <td>18</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Cold Shoulder</td>
      <td>single</td>
      <td>2</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Cold Shoulder</td>
      <td>single</td>
      <td>58</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Chasing Pavements</td>
      <td>single</td>
      <td>18</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Chasing Pavements</td>
      <td>single</td>
      <td>61</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Hometown Glory</td>
      <td>single</td>
      <td>18</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Say Something</td>
      <td>single</td>
      <td>76</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Passion for Life and Cello</td>
      <td>album</td>
      <td>79</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Sing A Cappella!</td>
      <td>album</td>
      <td>79</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Cover Stories: Brandi Carlile Celebrates 10 Ye...</td>
      <td>compilation</td>
      <td>79</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Movie Sound</td>
      <td>single</td>
      <td>79</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Lo Esencial de 1 Año de Éxitos, Vol. 5</td>
      <td>compilation</td>
      <td>1</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Pay Close Attention : XL Recordings</td>
      <td>compilation</td>
      <td>79</td>
    </tr>
    <tr>
      <th>41</th>
      <td>50 Pop Sensations</td>
      <td>compilation</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Simply the Best Ballads</td>
      <td>compilation</td>
      <td>8</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Sólo Pop</td>
      <td>compilation</td>
      <td>8</td>
    </tr>
    <tr>
      <th>44</th>
      <td>2013 GRAMMY Nominees</td>
      <td>compilation</td>
      <td>79</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Hits del Año</td>
      <td>compilation</td>
      <td>1</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Chimes Of Freedom: The Songs Of Bob Dylan Hono...</td>
      <td>compilation</td>
      <td>66</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Chimes Of Freedom: The Songs Of Bob Dylan Hono...</td>
      <td>compilation</td>
      <td>3</td>
    </tr>
    <tr>
      <th>48</th>
      <td>The BRIT Awards 2012</td>
      <td>compilation</td>
      <td>2</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Now! 18</td>
      <td>compilation</td>
      <td>1</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Love &amp; War</td>
      <td>album</td>
      <td>1</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Water And A Flame</td>
      <td>single</td>
      <td>75</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Love &amp; War</td>
      <td>album</td>
      <td>1</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Love &amp; War</td>
      <td>album</td>
      <td>76</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Love &amp; War</td>
      <td>album</td>
      <td>2</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Love &amp; War (Nokia Exclusive)</td>
      <td>album</td>
      <td>1</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Women</td>
      <td>compilation</td>
      <td>1</td>
    </tr>
    <tr>
      <th>57</th>
      <td>The Story &amp; Cover Stories</td>
      <td>album</td>
      <td>79</td>
    </tr>
  </tbody>
</table>
</div>




```python
everything_gb = everything.groupby('name').sum().replace(['albumalbumalbumalbum', 
                                          'albumalbum', 'singlesingle', 
                                          'compilationcompilation', 
                                          'singlesinglesinglesinglesinglesingle'],
                                         ['album', 'album', 'single', 'complication', 'single']).reset_index()
everything_gb
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>type</th>
      <th>countries released</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>19</td>
      <td>album</td>
      <td>136</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013 GRAMMY Nominees</td>
      <td>compilation</td>
      <td>79</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21</td>
      <td>album</td>
      <td>81</td>
    </tr>
    <tr>
      <th>3</th>
      <td>25</td>
      <td>album</td>
      <td>79</td>
    </tr>
    <tr>
      <th>4</th>
      <td>50 Pop Sensations</td>
      <td>compilation</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Chasing Pavements</td>
      <td>single</td>
      <td>79</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Chimes Of Freedom: The Songs Of Bob Dylan Hono...</td>
      <td>complication</td>
      <td>69</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Cold Shoulder</td>
      <td>single</td>
      <td>86</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Cover Stories: Brandi Carlile Celebrates 10 Ye...</td>
      <td>compilation</td>
      <td>79</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Hello</td>
      <td>single</td>
      <td>79</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Hits del Año</td>
      <td>compilation</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Hometown Glory</td>
      <td>single</td>
      <td>79</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Lo Esencial de 1 Año de Éxitos, Vol. 5</td>
      <td>compilation</td>
      <td>1</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Love &amp; War</td>
      <td>album</td>
      <td>80</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Love &amp; War (Nokia Exclusive)</td>
      <td>album</td>
      <td>1</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Make You Feel My Love</td>
      <td>single</td>
      <td>79</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Movie Sound</td>
      <td>single</td>
      <td>79</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Now! 18</td>
      <td>compilation</td>
      <td>1</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Passion for Life and Cello</td>
      <td>album</td>
      <td>79</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Pay Close Attention : XL Recordings</td>
      <td>compilation</td>
      <td>79</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Rolling In The Deep</td>
      <td>single</td>
      <td>62</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Say Something</td>
      <td>single</td>
      <td>76</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Send My Love (To Your New Lover)</td>
      <td>single</td>
      <td>79</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Set Fire to the Rain</td>
      <td>single</td>
      <td>61</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Simply the Best Ballads</td>
      <td>compilation</td>
      <td>8</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Sing A Cappella!</td>
      <td>album</td>
      <td>79</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Skyfall</td>
      <td>single</td>
      <td>79</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Sólo Pop</td>
      <td>compilation</td>
      <td>8</td>
    </tr>
    <tr>
      <th>28</th>
      <td>The BRIT Awards 2012</td>
      <td>compilation</td>
      <td>2</td>
    </tr>
    <tr>
      <th>29</th>
      <td>The Story &amp; Cover Stories</td>
      <td>album</td>
      <td>79</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Water And A Flame</td>
      <td>single</td>
      <td>75</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Water Under the Bridge</td>
      <td>single</td>
      <td>79</td>
    </tr>
    <tr>
      <th>32</th>
      <td>When We Were Young</td>
      <td>single</td>
      <td>79</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Women</td>
      <td>compilation</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Adele albums and singles number of countries released


```python
import plotly.express as px

fig = px.bar(everything_gb, everything_gb['type'], everything_gb['countries released'])
fig.update_layout(title='Adele work types number of countries released')

fig.show()
```


```python
import plotly.express as px

fig = px.bar(everything_gb, everything_gb['name'], everything_gb['countries released'])
fig.update_layout(title='Adele albums and single number of countries released')

fig.show()
```

### Top Adele tracks in USA


```python
top_tracks = requests.get('https://api.spotify.com/v1/artists/4dpARuHxo51G3z768sgnrY/top-tracks?country=US', headers=headers).json()
```


```python
tracks_df = pd.DataFrame([[i['album']['name'] for i in top_tracks['tracks']],
                          [i['album']['album_type'] for i in top_tracks['tracks']],
                          [i['name'] for i in top_tracks['tracks']],
                          [i['album']['release_date'] for i in top_tracks['tracks']],
                          [i['popularity'] for i in top_tracks['tracks']]]).T
```


```python
tracks_df.columns = ['name', 'type', 'track', 'release date', 'popularity']
```


```python
tracks_df_sort = tracks_df.sort_values('release date')
tracks_df_sort
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>type</th>
      <th>track</th>
      <th>release date</th>
      <th>popularity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>19</td>
      <td>album</td>
      <td>Make You Feel My Love</td>
      <td>2008-01-28</td>
      <td>72</td>
    </tr>
    <tr>
      <th>0</th>
      <td>21</td>
      <td>album</td>
      <td>Someone Like You</td>
      <td>2011-01-19</td>
      <td>78</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>album</td>
      <td>Rolling in the Deep</td>
      <td>2011-01-19</td>
      <td>75</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>album</td>
      <td>Set Fire to the Rain</td>
      <td>2011-01-19</td>
      <td>75</td>
    </tr>
    <tr>
      <th>9</th>
      <td>21</td>
      <td>album</td>
      <td>Turning Tables</td>
      <td>2011-01-19</td>
      <td>66</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Skyfall</td>
      <td>single</td>
      <td>Skyfall</td>
      <td>2012-10-04</td>
      <td>73</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25</td>
      <td>album</td>
      <td>When We Were Young</td>
      <td>2016-06-24</td>
      <td>72</td>
    </tr>
    <tr>
      <th>6</th>
      <td>25</td>
      <td>album</td>
      <td>Hello</td>
      <td>2016-06-24</td>
      <td>72</td>
    </tr>
    <tr>
      <th>7</th>
      <td>25</td>
      <td>album</td>
      <td>Send My Love (To Your New Lover)</td>
      <td>2016-06-24</td>
      <td>71</td>
    </tr>
    <tr>
      <th>8</th>
      <td>25</td>
      <td>album</td>
      <td>All I Ask</td>
      <td>2016-06-24</td>
      <td>69</td>
    </tr>
  </tbody>
</table>
</div>



### Adele tracks popularity by year in the U.S


```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(x=tracks_df_sort['release date'], y=tracks_df_sort['popularity'],
                         line=dict(color='firebrick', width=2)))
fig.update_layout(title='Adele tracks popularity by year',
                   xaxis_title='year',
                   yaxis_title='popularity')

fig.show()
```


```python

fig = go.Figure()

fig.add_trace(go.Scatter(x=tracks_df_sort['track'], y=tracks_df_sort['popularity'],
                         line=dict(color='firebrick', width=2)))
fig.update_layout(title='Adele tracks popularity by track',
                   xaxis_title='track',
                   yaxis_title='popularity')

fig.show()
```

### Get a list of recommendation for one song of Adele


```python
# track 'When We Were Young' and minimum popularity of recommended songs is 50
recomm = requests.get('https://api.spotify.com/v1/recommendations?seed_artists=4dpARuHxo51G3z768sgnrY&seed_tracks=7IWkJwX9C0J7tHurTD7ViL&min_popularity=50&market=US', headers=headers).json()
recomm
```




    {'tracks': [{'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/2feDdbD5araYcm6JhFHHw7'},
          'href': 'https://api.spotify.com/v1/artists/2feDdbD5araYcm6JhFHHw7',
          'id': '2feDdbD5araYcm6JhFHHw7',
          'name': 'Labrinth',
          'type': 'artist',
          'uri': 'spotify:artist:2feDdbD5araYcm6JhFHHw7'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/3eXbGItoetZbAKx5gxKcq8'},
        'href': 'https://api.spotify.com/v1/albums/3eXbGItoetZbAKx5gxKcq8',
        'id': '3eXbGItoetZbAKx5gxKcq8',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b2736544e23424a001cc58210e80',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e026544e23424a001cc58210e80',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d000048516544e23424a001cc58210e80',
          'width': 64}],
        'name': 'Beneath Your Beautiful',
        'release_date': '2013-08-27',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:3eXbGItoetZbAKx5gxKcq8'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/2feDdbD5araYcm6JhFHHw7'},
         'href': 'https://api.spotify.com/v1/artists/2feDdbD5araYcm6JhFHHw7',
         'id': '2feDdbD5araYcm6JhFHHw7',
         'name': 'Labrinth',
         'type': 'artist',
         'uri': 'spotify:artist:2feDdbD5araYcm6JhFHHw7'},
        {'external_urls': {'spotify': 'https://open.spotify.com/artist/7sfgqEdoeBTjd8lQsPT3Cy'},
         'href': 'https://api.spotify.com/v1/artists/7sfgqEdoeBTjd8lQsPT3Cy',
         'id': '7sfgqEdoeBTjd8lQsPT3Cy',
         'name': 'Emeli Sandé',
         'type': 'artist',
         'uri': 'spotify:artist:7sfgqEdoeBTjd8lQsPT3Cy'}],
       'disc_number': 1,
       'duration_ms': 271813,
       'explicit': False,
       'external_ids': {'isrc': 'GBHMU1200008'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/1wVcLKdJ4AFKPhKucNvEpy'},
       'href': 'https://api.spotify.com/v1/tracks/1wVcLKdJ4AFKPhKucNvEpy',
       'id': '1wVcLKdJ4AFKPhKucNvEpy',
       'is_local': False,
       'is_playable': True,
       'linked_from': {'external_urls': {'spotify': 'https://open.spotify.com/track/2EcsgXlxz99UMDSPg5T8RF'},
        'href': 'https://api.spotify.com/v1/tracks/2EcsgXlxz99UMDSPg5T8RF',
        'id': '2EcsgXlxz99UMDSPg5T8RF',
        'type': 'track',
        'uri': 'spotify:track:2EcsgXlxz99UMDSPg5T8RF'},
       'name': 'Beneath Your Beautiful',
       'popularity': 56,
       'preview_url': 'https://p.scdn.co/mp3-preview/5717e185b79fdca2cb5dccf6b1fd27818cc4f8f2?cid=f3e46ecaa544412cad663d349be1f137',
       'track_number': 1,
       'type': 'track',
       'uri': 'spotify:track:1wVcLKdJ4AFKPhKucNvEpy'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY'},
          'href': 'https://api.spotify.com/v1/artists/4dpARuHxo51G3z768sgnrY',
          'id': '4dpARuHxo51G3z768sgnrY',
          'name': 'Adele',
          'type': 'artist',
          'uri': 'spotify:artist:4dpARuHxo51G3z768sgnrY'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/1azUkThwd2HfUDdeNeT147'},
        'href': 'https://api.spotify.com/v1/albums/1azUkThwd2HfUDdeNeT147',
        'id': '1azUkThwd2HfUDdeNeT147',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b2736d4056466fc11f6408be2566',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e026d4056466fc11f6408be2566',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d000048516d4056466fc11f6408be2566',
          'width': 64}],
        'name': '21',
        'release_date': '2011-01-19',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:1azUkThwd2HfUDdeNeT147'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY'},
         'href': 'https://api.spotify.com/v1/artists/4dpARuHxo51G3z768sgnrY',
         'id': '4dpARuHxo51G3z768sgnrY',
         'name': 'Adele',
         'type': 'artist',
         'uri': 'spotify:artist:4dpARuHxo51G3z768sgnrY'}],
       'disc_number': 1,
       'duration_ms': 243200,
       'explicit': False,
       'external_ids': {'isrc': 'GBBKS1000344'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/24cKN8P2uGWypxTw5WaNlq'},
       'href': 'https://api.spotify.com/v1/tracks/24cKN8P2uGWypxTw5WaNlq',
       'id': '24cKN8P2uGWypxTw5WaNlq',
       'is_local': False,
       'is_playable': True,
       'name': "Don't You Remember",
       'popularity': 64,
       'preview_url': 'https://p.scdn.co/mp3-preview/087339b8fc037b9ee5e84e143a4c19a533ac62d0?cid=f3e46ecaa544412cad663d349be1f137',
       'track_number': 4,
       'type': 'track',
       'uri': 'spotify:track:24cKN8P2uGWypxTw5WaNlq'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6Q192DXotxtaysaqNPy5yR'},
          'href': 'https://api.spotify.com/v1/artists/6Q192DXotxtaysaqNPy5yR',
          'id': '6Q192DXotxtaysaqNPy5yR',
          'name': 'Amy Winehouse',
          'type': 'artist',
          'uri': 'spotify:artist:6Q192DXotxtaysaqNPy5yR'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/097eYvf9NKjFnv4xA9s2oV'},
        'href': 'https://api.spotify.com/v1/albums/097eYvf9NKjFnv4xA9s2oV',
        'id': '097eYvf9NKjFnv4xA9s2oV',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b2738f52f321140e4a76ea720c52',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e028f52f321140e4a76ea720c52',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d000048518f52f321140e4a76ea720c52',
          'width': 64}],
        'name': 'Back To Black',
        'release_date': '2006-10-27',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:097eYvf9NKjFnv4xA9s2oV'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6Q192DXotxtaysaqNPy5yR'},
         'href': 'https://api.spotify.com/v1/artists/6Q192DXotxtaysaqNPy5yR',
         'id': '6Q192DXotxtaysaqNPy5yR',
         'name': 'Amy Winehouse',
         'type': 'artist',
         'uri': 'spotify:artist:6Q192DXotxtaysaqNPy5yR'}],
       'disc_number': 1,
       'duration_ms': 185186,
       'explicit': True,
       'external_ids': {'isrc': 'GBUM70603494'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/6yLX8QnxlnEqZfs3YKCfjF'},
       'href': 'https://api.spotify.com/v1/tracks/6yLX8QnxlnEqZfs3YKCfjF',
       'id': '6yLX8QnxlnEqZfs3YKCfjF',
       'is_local': False,
       'is_playable': True,
       'name': 'Tears Dry On Their Own',
       'popularity': 66,
       'preview_url': None,
       'track_number': 7,
       'type': 'track',
       'uri': 'spotify:track:6yLX8QnxlnEqZfs3YKCfjF'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6JL8zeS1NmiOftqZTRgdTz'},
          'href': 'https://api.spotify.com/v1/artists/6JL8zeS1NmiOftqZTRgdTz',
          'id': '6JL8zeS1NmiOftqZTRgdTz',
          'name': 'Meghan Trainor',
          'type': 'artist',
          'uri': 'spotify:artist:6JL8zeS1NmiOftqZTRgdTz'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/5W98Ab4VvQEuFEE4TIe5fE'},
        'href': 'https://api.spotify.com/v1/albums/5W98Ab4VvQEuFEE4TIe5fE',
        'id': '5W98Ab4VvQEuFEE4TIe5fE',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b2733b11178cccd78ec77fc12dbc',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e023b11178cccd78ec77fc12dbc',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d000048513b11178cccd78ec77fc12dbc',
          'width': 64}],
        'name': 'Title (Deluxe)',
        'release_date': '2015-01-09',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:5W98Ab4VvQEuFEE4TIe5fE'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6JL8zeS1NmiOftqZTRgdTz'},
         'href': 'https://api.spotify.com/v1/artists/6JL8zeS1NmiOftqZTRgdTz',
         'id': '6JL8zeS1NmiOftqZTRgdTz',
         'name': 'Meghan Trainor',
         'type': 'artist',
         'uri': 'spotify:artist:6JL8zeS1NmiOftqZTRgdTz'},
        {'external_urls': {'spotify': 'https://open.spotify.com/artist/5y2Xq6xcjJb2jVM54GHK3t'},
         'href': 'https://api.spotify.com/v1/artists/5y2Xq6xcjJb2jVM54GHK3t',
         'id': '5y2Xq6xcjJb2jVM54GHK3t',
         'name': 'John Legend',
         'type': 'artist',
         'uri': 'spotify:artist:5y2Xq6xcjJb2jVM54GHK3t'}],
       'disc_number': 1,
       'duration_ms': 225053,
       'explicit': False,
       'external_ids': {'isrc': 'USSM11408374'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/2YlZnw2ikdb837oKMKjBkW'},
       'href': 'https://api.spotify.com/v1/tracks/2YlZnw2ikdb837oKMKjBkW',
       'id': '2YlZnw2ikdb837oKMKjBkW',
       'is_local': False,
       'is_playable': True,
       'name': "Like I'm Gonna Lose You (feat. John Legend)",
       'popularity': 78,
       'preview_url': 'https://p.scdn.co/mp3-preview/f0572ce757b4ded30a1a9ce5bd3edc368ee175f0?cid=f3e46ecaa544412cad663d349be1f137',
       'track_number': 6,
       'type': 'track',
       'uri': 'spotify:track:2YlZnw2ikdb837oKMKjBkW'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1l7ZsJRRS8wlW3WfJfPfNS'},
          'href': 'https://api.spotify.com/v1/artists/1l7ZsJRRS8wlW3WfJfPfNS',
          'id': '1l7ZsJRRS8wlW3WfJfPfNS',
          'name': 'Christina Aguilera',
          'type': 'artist',
          'uri': 'spotify:artist:1l7ZsJRRS8wlW3WfJfPfNS'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/2USigX9DhGuAini71XZEEK'},
        'href': 'https://api.spotify.com/v1/albums/2USigX9DhGuAini71XZEEK',
        'id': '2USigX9DhGuAini71XZEEK',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b2737cd872c7701c4737b2f81d87',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e027cd872c7701c4737b2f81d87',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d000048517cd872c7701c4737b2f81d87',
          'width': 64}],
        'name': 'Stripped',
        'release_date': '2002-07-19',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:2USigX9DhGuAini71XZEEK'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1l7ZsJRRS8wlW3WfJfPfNS'},
         'href': 'https://api.spotify.com/v1/artists/1l7ZsJRRS8wlW3WfJfPfNS',
         'id': '1l7ZsJRRS8wlW3WfJfPfNS',
         'name': 'Christina Aguilera',
         'type': 'artist',
         'uri': 'spotify:artist:1l7ZsJRRS8wlW3WfJfPfNS'}],
       'disc_number': 1,
       'duration_ms': 245960,
       'explicit': False,
       'external_ids': {'isrc': 'USRC10201072'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/7nXq1vaZiz7PdbfojpPjW5'},
       'href': 'https://api.spotify.com/v1/tracks/7nXq1vaZiz7PdbfojpPjW5',
       'id': '7nXq1vaZiz7PdbfojpPjW5',
       'is_local': False,
       'is_playable': True,
       'name': 'Fighter',
       'popularity': 68,
       'preview_url': 'https://p.scdn.co/mp3-preview/b1d94df0bb89a656665c83971170e9fa9fce4cc8?cid=f3e46ecaa544412cad663d349be1f137',
       'track_number': 4,
       'type': 'track',
       'uri': 'spotify:track:7nXq1vaZiz7PdbfojpPjW5'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6S2OmqARrzebs0tKUEyXyp'},
          'href': 'https://api.spotify.com/v1/artists/6S2OmqARrzebs0tKUEyXyp',
          'id': '6S2OmqARrzebs0tKUEyXyp',
          'name': 'Demi Lovato',
          'type': 'artist',
          'uri': 'spotify:artist:6S2OmqARrzebs0tKUEyXyp'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/6Kssm2LosQ0WyLukFZkEG5'},
        'href': 'https://api.spotify.com/v1/albums/6Kssm2LosQ0WyLukFZkEG5',
        'id': '6Kssm2LosQ0WyLukFZkEG5',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273aadb13ae608f6af20528409b',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02aadb13ae608f6af20528409b',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851aadb13ae608f6af20528409b',
          'width': 64}],
        'name': 'Demi',
        'release_date': '2013-01-01',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:6Kssm2LosQ0WyLukFZkEG5'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6S2OmqARrzebs0tKUEyXyp'},
         'href': 'https://api.spotify.com/v1/artists/6S2OmqARrzebs0tKUEyXyp',
         'id': '6S2OmqARrzebs0tKUEyXyp',
         'name': 'Demi Lovato',
         'type': 'artist',
         'uri': 'spotify:artist:6S2OmqARrzebs0tKUEyXyp'}],
       'disc_number': 1,
       'duration_ms': 210840,
       'explicit': False,
       'external_ids': {'isrc': 'USHR11334249'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/1V6gIisPpYqgFeWbMLI0bA'},
       'href': 'https://api.spotify.com/v1/tracks/1V6gIisPpYqgFeWbMLI0bA',
       'id': '1V6gIisPpYqgFeWbMLI0bA',
       'is_local': False,
       'is_playable': True,
       'name': 'Heart Attack',
       'popularity': 74,
       'preview_url': None,
       'track_number': 1,
       'type': 'track',
       'uri': 'spotify:track:1V6gIisPpYqgFeWbMLI0bA'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3FUY2gzHeIiaesXtOAdB7A'},
          'href': 'https://api.spotify.com/v1/artists/3FUY2gzHeIiaesXtOAdB7A',
          'id': '3FUY2gzHeIiaesXtOAdB7A',
          'name': 'Train',
          'type': 'artist',
          'uri': 'spotify:artist:3FUY2gzHeIiaesXtOAdB7A'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/5zseibu9WEsPaZmkJUMkz1'},
        'href': 'https://api.spotify.com/v1/albums/5zseibu9WEsPaZmkJUMkz1',
        'id': '5zseibu9WEsPaZmkJUMkz1',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273bde344cc54eedc35050f4c61',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02bde344cc54eedc35050f4c61',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851bde344cc54eedc35050f4c61',
          'width': 64}],
        'name': 'California 37',
        'release_date': '2012-04-17',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:5zseibu9WEsPaZmkJUMkz1'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3FUY2gzHeIiaesXtOAdB7A'},
         'href': 'https://api.spotify.com/v1/artists/3FUY2gzHeIiaesXtOAdB7A',
         'id': '3FUY2gzHeIiaesXtOAdB7A',
         'name': 'Train',
         'type': 'artist',
         'uri': 'spotify:artist:3FUY2gzHeIiaesXtOAdB7A'}],
       'disc_number': 1,
       'duration_ms': 195973,
       'explicit': False,
       'external_ids': {'isrc': 'USSM11106876'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/0KAiuUOrLTIkzkpfpn9jb9'},
       'href': 'https://api.spotify.com/v1/tracks/0KAiuUOrLTIkzkpfpn9jb9',
       'id': '0KAiuUOrLTIkzkpfpn9jb9',
       'is_local': False,
       'is_playable': True,
       'name': 'Drive By',
       'popularity': 74,
       'preview_url': 'https://p.scdn.co/mp3-preview/865f82fe864c025256b3871e0317d5d2229be147?cid=f3e46ecaa544412cad663d349be1f137',
       'track_number': 2,
       'type': 'track',
       'uri': 'spotify:track:0KAiuUOrLTIkzkpfpn9jb9'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1HY2Jd0NmPuamShAr6KMms'},
          'href': 'https://api.spotify.com/v1/artists/1HY2Jd0NmPuamShAr6KMms',
          'id': '1HY2Jd0NmPuamShAr6KMms',
          'name': 'Lady Gaga',
          'type': 'artist',
          'uri': 'spotify:artist:1HY2Jd0NmPuamShAr6KMms'},
         {'external_urls': {'spotify': 'https://open.spotify.com/artist/4VIvfOurcf0vuLRxLkGnIG'},
          'href': 'https://api.spotify.com/v1/artists/4VIvfOurcf0vuLRxLkGnIG',
          'id': '4VIvfOurcf0vuLRxLkGnIG',
          'name': 'Bradley Cooper',
          'type': 'artist',
          'uri': 'spotify:artist:4VIvfOurcf0vuLRxLkGnIG'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/4sLtOBOzn4s3GDUv3c5oJD'},
        'href': 'https://api.spotify.com/v1/albums/4sLtOBOzn4s3GDUv3c5oJD',
        'id': '4sLtOBOzn4s3GDUv3c5oJD',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273e2d156fdc691f57900134342',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02e2d156fdc691f57900134342',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851e2d156fdc691f57900134342',
          'width': 64}],
        'name': 'A Star Is Born Soundtrack',
        'release_date': '2018-10-05',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:4sLtOBOzn4s3GDUv3c5oJD'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1HY2Jd0NmPuamShAr6KMms'},
         'href': 'https://api.spotify.com/v1/artists/1HY2Jd0NmPuamShAr6KMms',
         'id': '1HY2Jd0NmPuamShAr6KMms',
         'name': 'Lady Gaga',
         'type': 'artist',
         'uri': 'spotify:artist:1HY2Jd0NmPuamShAr6KMms'},
        {'external_urls': {'spotify': 'https://open.spotify.com/artist/4VIvfOurcf0vuLRxLkGnIG'},
         'href': 'https://api.spotify.com/v1/artists/4VIvfOurcf0vuLRxLkGnIG',
         'id': '4VIvfOurcf0vuLRxLkGnIG',
         'name': 'Bradley Cooper',
         'type': 'artist',
         'uri': 'spotify:artist:4VIvfOurcf0vuLRxLkGnIG'}],
       'disc_number': 1,
       'duration_ms': 215733,
       'explicit': False,
       'external_ids': {'isrc': 'USUM71813192'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/2VxeLyX666F8uXCJ0dZF8B'},
       'href': 'https://api.spotify.com/v1/tracks/2VxeLyX666F8uXCJ0dZF8B',
       'id': '2VxeLyX666F8uXCJ0dZF8B',
       'is_local': False,
       'is_playable': True,
       'name': 'Shallow',
       'popularity': 86,
       'preview_url': None,
       'track_number': 12,
       'type': 'track',
       'uri': 'spotify:track:2VxeLyX666F8uXCJ0dZF8B'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY'},
          'href': 'https://api.spotify.com/v1/artists/4dpARuHxo51G3z768sgnrY',
          'id': '4dpARuHxo51G3z768sgnrY',
          'name': 'Adele',
          'type': 'artist',
          'uri': 'spotify:artist:4dpARuHxo51G3z768sgnrY'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/1ydnyXPdmHrWXqXDgtQCPf'},
        'href': 'https://api.spotify.com/v1/albums/1ydnyXPdmHrWXqXDgtQCPf',
        'id': '1ydnyXPdmHrWXqXDgtQCPf',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273f407037aabc6dffe5abb3bf8',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02f407037aabc6dffe5abb3bf8',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851f407037aabc6dffe5abb3bf8',
          'width': 64}],
        'name': '19',
        'release_date': '2008-01-28',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:1ydnyXPdmHrWXqXDgtQCPf'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY'},
         'href': 'https://api.spotify.com/v1/artists/4dpARuHxo51G3z768sgnrY',
         'id': '4dpARuHxo51G3z768sgnrY',
         'name': 'Adele',
         'type': 'artist',
         'uri': 'spotify:artist:4dpARuHxo51G3z768sgnrY'}],
       'disc_number': 1,
       'duration_ms': 197346,
       'explicit': False,
       'external_ids': {'isrc': 'GBBKS0700587'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/2IF2XQ095Qqf6tBL9Y4vZn'},
       'href': 'https://api.spotify.com/v1/tracks/2IF2XQ095Qqf6tBL9Y4vZn',
       'id': '2IF2XQ095Qqf6tBL9Y4vZn',
       'is_local': False,
       'is_playable': True,
       'name': 'Right As Rain',
       'popularity': 51,
       'preview_url': 'https://p.scdn.co/mp3-preview/557e6f8f6094648dd1d91641d1887c4c68ba86da?cid=f3e46ecaa544412cad663d349be1f137',
       'track_number': 8,
       'type': 'track',
       'uri': 'spotify:track:2IF2XQ095Qqf6tBL9Y4vZn'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6jJ0s89eD6GaHleKKya26X'},
          'href': 'https://api.spotify.com/v1/artists/6jJ0s89eD6GaHleKKya26X',
          'id': '6jJ0s89eD6GaHleKKya26X',
          'name': 'Katy Perry',
          'type': 'artist',
          'uri': 'spotify:artist:6jJ0s89eD6GaHleKKya26X'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/5MQBzs5YlZlE28mD9yUItn'},
        'href': 'https://api.spotify.com/v1/albums/5MQBzs5YlZlE28mD9yUItn',
        'id': '5MQBzs5YlZlE28mD9yUItn',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b27347f930accd8ac01686401fa2',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e0247f930accd8ac01686401fa2',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d0000485147f930accd8ac01686401fa2',
          'width': 64}],
        'name': 'PRISM (Deluxe)',
        'release_date': '2013-10-18',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:5MQBzs5YlZlE28mD9yUItn'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6jJ0s89eD6GaHleKKya26X'},
         'href': 'https://api.spotify.com/v1/artists/6jJ0s89eD6GaHleKKya26X',
         'id': '6jJ0s89eD6GaHleKKya26X',
         'name': 'Katy Perry',
         'type': 'artist',
         'uri': 'spotify:artist:6jJ0s89eD6GaHleKKya26X'}],
       'disc_number': 1,
       'duration_ms': 223546,
       'explicit': False,
       'external_ids': {'isrc': 'USUM71308669'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/6F5c58TMEs1byxUstkzVeM'},
       'href': 'https://api.spotify.com/v1/tracks/6F5c58TMEs1byxUstkzVeM',
       'id': '6F5c58TMEs1byxUstkzVeM',
       'is_local': False,
       'is_playable': True,
       'name': 'Roar',
       'popularity': 75,
       'preview_url': None,
       'track_number': 1,
       'type': 'track',
       'uri': 'spotify:track:6F5c58TMEs1byxUstkzVeM'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3BmGtnKgCSGYIUhmivXKWX'},
          'href': 'https://api.spotify.com/v1/artists/3BmGtnKgCSGYIUhmivXKWX',
          'id': '3BmGtnKgCSGYIUhmivXKWX',
          'name': 'Kelly Clarkson',
          'type': 'artist',
          'uri': 'spotify:artist:3BmGtnKgCSGYIUhmivXKWX'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/5gDAEao3VxFdbm8vS0koQq'},
        'href': 'https://api.spotify.com/v1/albums/5gDAEao3VxFdbm8vS0koQq',
        'id': '5gDAEao3VxFdbm8vS0koQq',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b27303dadde4d9d305c1c3e0d91c',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e0203dadde4d9d305c1c3e0d91c',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d0000485103dadde4d9d305c1c3e0d91c',
          'width': 64}],
        'name': 'Breakaway',
        'release_date': '2004-01-17',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:5gDAEao3VxFdbm8vS0koQq'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3BmGtnKgCSGYIUhmivXKWX'},
         'href': 'https://api.spotify.com/v1/artists/3BmGtnKgCSGYIUhmivXKWX',
         'id': '3BmGtnKgCSGYIUhmivXKWX',
         'name': 'Kelly Clarkson',
         'type': 'artist',
         'uri': 'spotify:artist:3BmGtnKgCSGYIUhmivXKWX'}],
       'disc_number': 1,
       'duration_ms': 188960,
       'explicit': False,
       'external_ids': {'isrc': 'GBCTA0400231'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/3xrn9i8zhNZsTtcoWgQEAd'},
       'href': 'https://api.spotify.com/v1/tracks/3xrn9i8zhNZsTtcoWgQEAd',
       'id': '3xrn9i8zhNZsTtcoWgQEAd',
       'is_local': False,
       'is_playable': True,
       'name': 'Since U Been Gone',
       'popularity': 73,
       'preview_url': 'https://p.scdn.co/mp3-preview/6e39adc77aba227544f11251414bd89824e0eb96?cid=f3e46ecaa544412cad663d349be1f137',
       'track_number': 2,
       'type': 'track',
       'uri': 'spotify:track:3xrn9i8zhNZsTtcoWgQEAd'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4ScCswdRlyA23odg9thgIO'},
          'href': 'https://api.spotify.com/v1/artists/4ScCswdRlyA23odg9thgIO',
          'id': '4ScCswdRlyA23odg9thgIO',
          'name': 'Jess Glynne',
          'type': 'artist',
          'uri': 'spotify:artist:4ScCswdRlyA23odg9thgIO'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/7o6j8wph7fvEcAL67jLVGN'},
        'href': 'https://api.spotify.com/v1/albums/7o6j8wph7fvEcAL67jLVGN',
        'id': '7o6j8wph7fvEcAL67jLVGN',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b27377179b6ddeb4b4f4757e7a10',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e0277179b6ddeb4b4f4757e7a10',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d0000485177179b6ddeb4b4f4757e7a10',
          'width': 64}],
        'name': "I'll Be There",
        'release_date': '2018-05-03',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:7o6j8wph7fvEcAL67jLVGN'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4ScCswdRlyA23odg9thgIO'},
         'href': 'https://api.spotify.com/v1/artists/4ScCswdRlyA23odg9thgIO',
         'id': '4ScCswdRlyA23odg9thgIO',
         'name': 'Jess Glynne',
         'type': 'artist',
         'uri': 'spotify:artist:4ScCswdRlyA23odg9thgIO'}],
       'disc_number': 1,
       'duration_ms': 193923,
       'explicit': False,
       'external_ids': {'isrc': 'GBAHS1800322'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/083Qf6hn6sFL6xiOHlZUyn'},
       'href': 'https://api.spotify.com/v1/tracks/083Qf6hn6sFL6xiOHlZUyn',
       'id': '083Qf6hn6sFL6xiOHlZUyn',
       'is_local': False,
       'is_playable': True,
       'name': "I'll Be There",
       'popularity': 71,
       'preview_url': 'https://p.scdn.co/mp3-preview/50b537f9f475abff638562ae8806391009d24d43?cid=f3e46ecaa544412cad663d349be1f137',
       'track_number': 1,
       'type': 'track',
       'uri': 'spotify:track:083Qf6hn6sFL6xiOHlZUyn'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1KCSPY1glIKqW2TotWuXOR'},
          'href': 'https://api.spotify.com/v1/artists/1KCSPY1glIKqW2TotWuXOR',
          'id': '1KCSPY1glIKqW2TotWuXOR',
          'name': 'P!nk',
          'type': 'artist',
          'uri': 'spotify:artist:1KCSPY1glIKqW2TotWuXOR'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/6WlnnRa9jAPXhZEbvBvdxB'},
        'href': 'https://api.spotify.com/v1/albums/6WlnnRa9jAPXhZEbvBvdxB',
        'id': '6WlnnRa9jAPXhZEbvBvdxB',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273decc33d60395deec6d465b01',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02decc33d60395deec6d465b01',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851decc33d60395deec6d465b01',
          'width': 64}],
        'name': "I'm Not Dead",
        'release_date': '2006-04-04',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:6WlnnRa9jAPXhZEbvBvdxB'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1KCSPY1glIKqW2TotWuXOR'},
         'href': 'https://api.spotify.com/v1/artists/1KCSPY1glIKqW2TotWuXOR',
         'id': '1KCSPY1glIKqW2TotWuXOR',
         'name': 'P!nk',
         'type': 'artist',
         'uri': 'spotify:artist:1KCSPY1glIKqW2TotWuXOR'}],
       'disc_number': 1,
       'duration_ms': 208493,
       'explicit': False,
       'external_ids': {'isrc': 'USLF20600021'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/7uYl7xgDeAOHP98obvrJvB'},
       'href': 'https://api.spotify.com/v1/tracks/7uYl7xgDeAOHP98obvrJvB',
       'id': '7uYl7xgDeAOHP98obvrJvB',
       'is_local': False,
       'is_playable': True,
       'name': 'Who Knew',
       'popularity': 69,
       'preview_url': 'https://p.scdn.co/mp3-preview/e1d31c14939bd998e6a95853fe76251169d267e6?cid=f3e46ecaa544412cad663d349be1f137',
       'track_number': 2,
       'type': 'track',
       'uri': 'spotify:track:7uYl7xgDeAOHP98obvrJvB'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1Hsdzj7Dlq2I7tHP7501T4'},
          'href': 'https://api.spotify.com/v1/artists/1Hsdzj7Dlq2I7tHP7501T4',
          'id': '1Hsdzj7Dlq2I7tHP7501T4',
          'name': 'Niall Horan',
          'type': 'artist',
          'uri': 'spotify:artist:1Hsdzj7Dlq2I7tHP7501T4'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/7ahctQBwcSxDdP0fRAPo2p'},
        'href': 'https://api.spotify.com/v1/albums/7ahctQBwcSxDdP0fRAPo2p',
        'id': '7ahctQBwcSxDdP0fRAPo2p',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b2738d61a242f5a4e73709b02931',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e028d61a242f5a4e73709b02931',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d000048518d61a242f5a4e73709b02931',
          'width': 64}],
        'name': 'Flicker (Deluxe)',
        'release_date': '2017-10-20',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:7ahctQBwcSxDdP0fRAPo2p'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1Hsdzj7Dlq2I7tHP7501T4'},
         'href': 'https://api.spotify.com/v1/artists/1Hsdzj7Dlq2I7tHP7501T4',
         'id': '1Hsdzj7Dlq2I7tHP7501T4',
         'name': 'Niall Horan',
         'type': 'artist',
         'uri': 'spotify:artist:1Hsdzj7Dlq2I7tHP7501T4'}],
       'disc_number': 1,
       'duration_ms': 223043,
       'explicit': True,
       'external_ids': {'isrc': 'USUG11701396'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/39jXnbACjiaiTwwhsr5sY5'},
       'href': 'https://api.spotify.com/v1/tracks/39jXnbACjiaiTwwhsr5sY5',
       'id': '39jXnbACjiaiTwwhsr5sY5',
       'is_local': False,
       'is_playable': True,
       'name': 'Too Much To Ask',
       'popularity': 73,
       'preview_url': None,
       'track_number': 5,
       'type': 'track',
       'uri': 'spotify:track:39jXnbACjiaiTwwhsr5sY5'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5Rl15oVamLq7FbSb0NNBNy'},
          'href': 'https://api.spotify.com/v1/artists/5Rl15oVamLq7FbSb0NNBNy',
          'id': '5Rl15oVamLq7FbSb0NNBNy',
          'name': '5 Seconds of Summer',
          'type': 'artist',
          'uri': 'spotify:artist:5Rl15oVamLq7FbSb0NNBNy'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/43v9cUsP5K0hvu9iyuAzmZ'},
        'href': 'https://api.spotify.com/v1/albums/43v9cUsP5K0hvu9iyuAzmZ',
        'id': '43v9cUsP5K0hvu9iyuAzmZ',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273a7cb3e00ac2f3a1bf8679fef',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02a7cb3e00ac2f3a1bf8679fef',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851a7cb3e00ac2f3a1bf8679fef',
          'width': 64}],
        'name': 'Sounds Good Feels Good (Deluxe)',
        'release_date': '2015-10-23',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:43v9cUsP5K0hvu9iyuAzmZ'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5Rl15oVamLq7FbSb0NNBNy'},
         'href': 'https://api.spotify.com/v1/artists/5Rl15oVamLq7FbSb0NNBNy',
         'id': '5Rl15oVamLq7FbSb0NNBNy',
         'name': '5 Seconds of Summer',
         'type': 'artist',
         'uri': 'spotify:artist:5Rl15oVamLq7FbSb0NNBNy'}],
       'disc_number': 1,
       'duration_ms': 220708,
       'explicit': False,
       'external_ids': {'isrc': 'GBUM71505161'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/5TMjhlh25Oitlh3LBKdfMi'},
       'href': 'https://api.spotify.com/v1/tracks/5TMjhlh25Oitlh3LBKdfMi',
       'id': '5TMjhlh25Oitlh3LBKdfMi',
       'is_local': False,
       'is_playable': True,
       'name': 'Broken Home',
       'popularity': 56,
       'preview_url': None,
       'track_number': 12,
       'type': 'track',
       'uri': 'spotify:track:5TMjhlh25Oitlh3LBKdfMi'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY'},
          'href': 'https://api.spotify.com/v1/artists/4dpARuHxo51G3z768sgnrY',
          'id': '4dpARuHxo51G3z768sgnrY',
          'name': 'Adele',
          'type': 'artist',
          'uri': 'spotify:artist:4dpARuHxo51G3z768sgnrY'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/1ydnyXPdmHrWXqXDgtQCPf'},
        'href': 'https://api.spotify.com/v1/albums/1ydnyXPdmHrWXqXDgtQCPf',
        'id': '1ydnyXPdmHrWXqXDgtQCPf',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273f407037aabc6dffe5abb3bf8',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02f407037aabc6dffe5abb3bf8',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851f407037aabc6dffe5abb3bf8',
          'width': 64}],
        'name': '19',
        'release_date': '2008-01-28',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:1ydnyXPdmHrWXqXDgtQCPf'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY'},
         'href': 'https://api.spotify.com/v1/artists/4dpARuHxo51G3z768sgnrY',
         'id': '4dpARuHxo51G3z768sgnrY',
         'name': 'Adele',
         'type': 'artist',
         'uri': 'spotify:artist:4dpARuHxo51G3z768sgnrY'}],
       'disc_number': 1,
       'duration_ms': 203906,
       'explicit': False,
       'external_ids': {'isrc': 'GBBKS0700584'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/0WPXlTF9IADmeaX86DoUr8'},
       'href': 'https://api.spotify.com/v1/tracks/0WPXlTF9IADmeaX86DoUr8',
       'id': '0WPXlTF9IADmeaX86DoUr8',
       'is_local': False,
       'is_playable': True,
       'name': 'Melt My Heart To Stone',
       'popularity': 57,
       'preview_url': 'https://p.scdn.co/mp3-preview/6f28651c953f711c0df454acc97d3436cf4abf70?cid=f3e46ecaa544412cad663d349be1f137',
       'track_number': 6,
       'type': 'track',
       'uri': 'spotify:track:0WPXlTF9IADmeaX86DoUr8'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1Xylc3o4UrD53lo9CvFvVg'},
          'href': 'https://api.spotify.com/v1/artists/1Xylc3o4UrD53lo9CvFvVg',
          'id': '1Xylc3o4UrD53lo9CvFvVg',
          'name': 'Zara Larsson',
          'type': 'artist',
          'uri': 'spotify:artist:1Xylc3o4UrD53lo9CvFvVg'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/0vXJ3rh6Sy7KWjp2P5d7ll'},
        'href': 'https://api.spotify.com/v1/albums/0vXJ3rh6Sy7KWjp2P5d7ll',
        'id': '0vXJ3rh6Sy7KWjp2P5d7ll',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273a9eccb7ff0ef93cba9e4da5d',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02a9eccb7ff0ef93cba9e4da5d',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851a9eccb7ff0ef93cba9e4da5d',
          'width': 64}],
        'name': 'Uncover',
        'release_date': '2012',
        'release_date_precision': 'year',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:0vXJ3rh6Sy7KWjp2P5d7ll'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1Xylc3o4UrD53lo9CvFvVg'},
         'href': 'https://api.spotify.com/v1/artists/1Xylc3o4UrD53lo9CvFvVg',
         'id': '1Xylc3o4UrD53lo9CvFvVg',
         'name': 'Zara Larsson',
         'type': 'artist',
         'uri': 'spotify:artist:1Xylc3o4UrD53lo9CvFvVg'}],
       'disc_number': 1,
       'duration_ms': 213543,
       'explicit': False,
       'external_ids': {'isrc': 'SEWEE1201112'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/3DQisSEr1TLp9H0BEeKiQS'},
       'href': 'https://api.spotify.com/v1/tracks/3DQisSEr1TLp9H0BEeKiQS',
       'id': '3DQisSEr1TLp9H0BEeKiQS',
       'is_local': False,
       'is_playable': True,
       'linked_from': {'external_urls': {'spotify': 'https://open.spotify.com/track/5rkok5WSDPoQb9xKx5R61n'},
        'href': 'https://api.spotify.com/v1/tracks/5rkok5WSDPoQb9xKx5R61n',
        'id': '5rkok5WSDPoQb9xKx5R61n',
        'type': 'track',
        'uri': 'spotify:track:5rkok5WSDPoQb9xKx5R61n'},
       'name': 'Uncover',
       'popularity': 66,
       'preview_url': 'https://p.scdn.co/mp3-preview/1ee901eae93c71f55bcdcd7ebdac8c203239d305?cid=f3e46ecaa544412cad663d349be1f137',
       'track_number': 3,
       'type': 'track',
       'uri': 'spotify:track:3DQisSEr1TLp9H0BEeKiQS'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4EzkuveR9pLvDVFNx6foYD'},
          'href': 'https://api.spotify.com/v1/artists/4EzkuveR9pLvDVFNx6foYD',
          'id': '4EzkuveR9pLvDVFNx6foYD',
          'name': 'James Bay',
          'type': 'artist',
          'uri': 'spotify:artist:4EzkuveR9pLvDVFNx6foYD'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/2aIsEIVLrAP75xdEhdVm1d'},
        'href': 'https://api.spotify.com/v1/albums/2aIsEIVLrAP75xdEhdVm1d',
        'id': '2aIsEIVLrAP75xdEhdVm1d',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b2734b32688c63234ca628de1cc9',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e024b32688c63234ca628de1cc9',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d000048514b32688c63234ca628de1cc9',
          'width': 64}],
        'name': 'Oh My Messy Mind',
        'release_date': '2019-05-10',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:2aIsEIVLrAP75xdEhdVm1d'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4EzkuveR9pLvDVFNx6foYD'},
         'href': 'https://api.spotify.com/v1/artists/4EzkuveR9pLvDVFNx6foYD',
         'id': '4EzkuveR9pLvDVFNx6foYD',
         'name': 'James Bay',
         'type': 'artist',
         'uri': 'spotify:artist:4EzkuveR9pLvDVFNx6foYD'},
        {'external_urls': {'spotify': 'https://open.spotify.com/artist/0ZED1XzwlLHW4ZaG4lOT6m'},
         'href': 'https://api.spotify.com/v1/artists/0ZED1XzwlLHW4ZaG4lOT6m',
         'id': '0ZED1XzwlLHW4ZaG4lOT6m',
         'name': 'Julia Michaels',
         'type': 'artist',
         'uri': 'spotify:artist:0ZED1XzwlLHW4ZaG4lOT6m'}],
       'disc_number': 1,
       'duration_ms': 176826,
       'explicit': False,
       'external_ids': {'isrc': 'USUM71901255'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/4RE3vueod5PL48rvHtuu9C'},
       'href': 'https://api.spotify.com/v1/tracks/4RE3vueod5PL48rvHtuu9C',
       'id': '4RE3vueod5PL48rvHtuu9C',
       'is_local': False,
       'is_playable': True,
       'name': 'Peer Pressure',
       'popularity': 74,
       'preview_url': None,
       'track_number': 1,
       'type': 'track',
       'uri': 'spotify:track:4RE3vueod5PL48rvHtuu9C'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/2Kx7MNY7cI1ENniW7vT30N'},
          'href': 'https://api.spotify.com/v1/artists/2Kx7MNY7cI1ENniW7vT30N',
          'id': '2Kx7MNY7cI1ENniW7vT30N',
          'name': 'Norah Jones',
          'type': 'artist',
          'uri': 'spotify:artist:2Kx7MNY7cI1ENniW7vT30N'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/6PguISnE2nz7CuhnIAWhQF'},
        'href': 'https://api.spotify.com/v1/albums/6PguISnE2nz7CuhnIAWhQF',
        'id': '6PguISnE2nz7CuhnIAWhQF',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273d2d5321f75c99ddd16324ffe',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02d2d5321f75c99ddd16324ffe',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851d2d5321f75c99ddd16324ffe',
          'width': 64}],
        'name': 'Come Away With Me (Deluxe Edition)',
        'release_date': '2002-02-22',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:6PguISnE2nz7CuhnIAWhQF'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/2Kx7MNY7cI1ENniW7vT30N'},
         'href': 'https://api.spotify.com/v1/artists/2Kx7MNY7cI1ENniW7vT30N',
         'id': '2Kx7MNY7cI1ENniW7vT30N',
         'name': 'Norah Jones',
         'type': 'artist',
         'uri': 'spotify:artist:2Kx7MNY7cI1ENniW7vT30N'}],
       'disc_number': 1,
       'duration_ms': 198226,
       'explicit': False,
       'external_ids': {'isrc': 'USBN20100889'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/52FKX00U3PnzrBQmbMTB8b'},
       'href': 'https://api.spotify.com/v1/tracks/52FKX00U3PnzrBQmbMTB8b',
       'id': '52FKX00U3PnzrBQmbMTB8b',
       'is_local': False,
       'is_playable': True,
       'name': 'Come Away With Me',
       'popularity': 57,
       'preview_url': None,
       'track_number': 5,
       'type': 'track',
       'uri': 'spotify:track:52FKX00U3PnzrBQmbMTB8b'},
      {'album': {'album_type': 'ALBUM',
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6KImCVD70vtIoJWnq6nGn3'},
          'href': 'https://api.spotify.com/v1/artists/6KImCVD70vtIoJWnq6nGn3',
          'id': '6KImCVD70vtIoJWnq6nGn3',
          'name': 'Harry Styles',
          'type': 'artist',
          'uri': 'spotify:artist:6KImCVD70vtIoJWnq6nGn3'}],
        'external_urls': {'spotify': 'https://open.spotify.com/album/1FZKIm3JVDCxTchXDo5jOV'},
        'href': 'https://api.spotify.com/v1/albums/1FZKIm3JVDCxTchXDo5jOV',
        'id': '1FZKIm3JVDCxTchXDo5jOV',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b2736c619c39c853f8b1d67b7859',
          'width': 640},
         {'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e026c619c39c853f8b1d67b7859',
          'width': 300},
         {'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d000048516c619c39c853f8b1d67b7859',
          'width': 64}],
        'name': 'Harry Styles',
        'release_date': '2017-05-12',
        'release_date_precision': 'day',
        'total_tracks': 0,
        'type': 'album',
        'uri': 'spotify:album:1FZKIm3JVDCxTchXDo5jOV'},
       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6KImCVD70vtIoJWnq6nGn3'},
         'href': 'https://api.spotify.com/v1/artists/6KImCVD70vtIoJWnq6nGn3',
         'id': '6KImCVD70vtIoJWnq6nGn3',
         'name': 'Harry Styles',
         'type': 'artist',
         'uri': 'spotify:artist:6KImCVD70vtIoJWnq6nGn3'}],
       'disc_number': 1,
       'duration_ms': 340706,
       'explicit': False,
       'external_ids': {'isrc': 'USSM11703595'},
       'external_urls': {'spotify': 'https://open.spotify.com/track/5Ohxk2dO5COHF1krpoPigN'},
       'href': 'https://api.spotify.com/v1/tracks/5Ohxk2dO5COHF1krpoPigN',
       'id': '5Ohxk2dO5COHF1krpoPigN',
       'is_local': False,
       'is_playable': True,
       'name': 'Sign of the Times',
       'popularity': 81,
       'preview_url': 'https://p.scdn.co/mp3-preview/af237206f611b722f48620ece049aff3b8650e77?cid=f3e46ecaa544412cad663d349be1f137',
       'track_number': 2,
       'type': 'track',
       'uri': 'spotify:track:5Ohxk2dO5COHF1krpoPigN'}],
     'seeds': [{'initialPoolSize': 250,
       'afterFilteringSize': 235,
       'afterRelinkingSize': 234,
       'id': '4dpARuHxo51G3z768sgnrY',
       'type': 'ARTIST',
       'href': 'https://api.spotify.com/v1/artists/4dpARuHxo51G3z768sgnrY'},
      {'initialPoolSize': 249,
       'afterFilteringSize': 234,
       'afterRelinkingSize': 233,
       'id': '7IWkJwX9C0J7tHurTD7ViL',
       'type': 'TRACK',
       'href': 'https://api.spotify.com/v1/tracks/7IWkJwX9C0J7tHurTD7ViL'}]}




```python
recomm_df = pd.DataFrame([[i['id'] for i in recomm['tracks']],
                          [i['name'] for i in recomm['tracks']],
                          [i['popularity'] for i in recomm['tracks']]]).T
```


```python
recomm_df.columns = ['id', 'name', 'popularity']
```


```python
recomm_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>popularity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1wVcLKdJ4AFKPhKucNvEpy</td>
      <td>Beneath Your Beautiful</td>
      <td>56</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24cKN8P2uGWypxTw5WaNlq</td>
      <td>Don't You Remember</td>
      <td>64</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6yLX8QnxlnEqZfs3YKCfjF</td>
      <td>Tears Dry On Their Own</td>
      <td>66</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2YlZnw2ikdb837oKMKjBkW</td>
      <td>Like I'm Gonna Lose You (feat. John Legend)</td>
      <td>78</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7nXq1vaZiz7PdbfojpPjW5</td>
      <td>Fighter</td>
      <td>68</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1V6gIisPpYqgFeWbMLI0bA</td>
      <td>Heart Attack</td>
      <td>74</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0KAiuUOrLTIkzkpfpn9jb9</td>
      <td>Drive By</td>
      <td>74</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2VxeLyX666F8uXCJ0dZF8B</td>
      <td>Shallow</td>
      <td>86</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2IF2XQ095Qqf6tBL9Y4vZn</td>
      <td>Right As Rain</td>
      <td>51</td>
    </tr>
    <tr>
      <th>9</th>
      <td>6F5c58TMEs1byxUstkzVeM</td>
      <td>Roar</td>
      <td>75</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3xrn9i8zhNZsTtcoWgQEAd</td>
      <td>Since U Been Gone</td>
      <td>73</td>
    </tr>
    <tr>
      <th>11</th>
      <td>083Qf6hn6sFL6xiOHlZUyn</td>
      <td>I'll Be There</td>
      <td>71</td>
    </tr>
    <tr>
      <th>12</th>
      <td>7uYl7xgDeAOHP98obvrJvB</td>
      <td>Who Knew</td>
      <td>69</td>
    </tr>
    <tr>
      <th>13</th>
      <td>39jXnbACjiaiTwwhsr5sY5</td>
      <td>Too Much To Ask</td>
      <td>73</td>
    </tr>
    <tr>
      <th>14</th>
      <td>5TMjhlh25Oitlh3LBKdfMi</td>
      <td>Broken Home</td>
      <td>56</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0WPXlTF9IADmeaX86DoUr8</td>
      <td>Melt My Heart To Stone</td>
      <td>57</td>
    </tr>
    <tr>
      <th>16</th>
      <td>3DQisSEr1TLp9H0BEeKiQS</td>
      <td>Uncover</td>
      <td>66</td>
    </tr>
    <tr>
      <th>17</th>
      <td>4RE3vueod5PL48rvHtuu9C</td>
      <td>Peer Pressure</td>
      <td>74</td>
    </tr>
    <tr>
      <th>18</th>
      <td>52FKX00U3PnzrBQmbMTB8b</td>
      <td>Come Away With Me</td>
      <td>57</td>
    </tr>
    <tr>
      <th>19</th>
      <td>5Ohxk2dO5COHF1krpoPigN</td>
      <td>Sign of the Times</td>
      <td>81</td>
    </tr>
  </tbody>
</table>
</div>



### Check track features and compare them to 'When We Were Young' to see how recommendations match


```python
def get_features(row):
    data = requests.get('https://api.spotify.com/v1/audio-features/' + row, headers=headers).json()
    return data
```


```python
recomm_df['features'] = recomm_df['id'].apply(get_features)
```


```python
stepper = 0
for i in recomm_df['features']:
    for n in i:
        recomm_df.at[stepper, n] = i[n]
    stepper += 1
```


```python
# drop extra cols
recomm_df.drop(labels=['features', 'type', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'], axis=1, inplace=True)
```


```python
recomm_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>popularity</th>
      <th>danceability</th>
      <th>energy</th>
      <th>key</th>
      <th>loudness</th>
      <th>mode</th>
      <th>speechiness</th>
      <th>acousticness</th>
      <th>instrumentalness</th>
      <th>liveness</th>
      <th>valence</th>
      <th>tempo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1wVcLKdJ4AFKPhKucNvEpy</td>
      <td>Beneath Your Beautiful</td>
      <td>56</td>
      <td>0.558</td>
      <td>0.522</td>
      <td>2.0</td>
      <td>-5.857</td>
      <td>1.0</td>
      <td>0.0360</td>
      <td>0.22800</td>
      <td>0.000000</td>
      <td>0.1040</td>
      <td>0.228</td>
      <td>83.977</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24cKN8P2uGWypxTw5WaNlq</td>
      <td>Don't You Remember</td>
      <td>64</td>
      <td>0.640</td>
      <td>0.395</td>
      <td>3.0</td>
      <td>-5.689</td>
      <td>1.0</td>
      <td>0.0307</td>
      <td>0.20600</td>
      <td>0.000000</td>
      <td>0.0935</td>
      <td>0.235</td>
      <td>115.082</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6yLX8QnxlnEqZfs3YKCfjF</td>
      <td>Tears Dry On Their Own</td>
      <td>66</td>
      <td>0.643</td>
      <td>0.871</td>
      <td>1.0</td>
      <td>-2.734</td>
      <td>0.0</td>
      <td>0.1180</td>
      <td>0.49100</td>
      <td>0.000000</td>
      <td>0.2900</td>
      <td>0.452</td>
      <td>121.569</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2YlZnw2ikdb837oKMKjBkW</td>
      <td>Like I'm Gonna Lose You (feat. John Legend)</td>
      <td>78</td>
      <td>0.630</td>
      <td>0.530</td>
      <td>0.0</td>
      <td>-7.259</td>
      <td>1.0</td>
      <td>0.0434</td>
      <td>0.40000</td>
      <td>0.000000</td>
      <td>0.1770</td>
      <td>0.417</td>
      <td>108.038</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7nXq1vaZiz7PdbfojpPjW5</td>
      <td>Fighter</td>
      <td>68</td>
      <td>0.435</td>
      <td>0.920</td>
      <td>4.0</td>
      <td>-1.357</td>
      <td>0.0</td>
      <td>0.2010</td>
      <td>0.23500</td>
      <td>0.000353</td>
      <td>0.5520</td>
      <td>0.450</td>
      <td>188.899</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1V6gIisPpYqgFeWbMLI0bA</td>
      <td>Heart Attack</td>
      <td>74</td>
      <td>0.504</td>
      <td>0.785</td>
      <td>8.0</td>
      <td>-4.802</td>
      <td>1.0</td>
      <td>0.1040</td>
      <td>0.07380</td>
      <td>0.000000</td>
      <td>0.2390</td>
      <td>0.502</td>
      <td>173.968</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0KAiuUOrLTIkzkpfpn9jb9</td>
      <td>Drive By</td>
      <td>74</td>
      <td>0.765</td>
      <td>0.837</td>
      <td>1.0</td>
      <td>-3.113</td>
      <td>0.0</td>
      <td>0.0320</td>
      <td>0.00107</td>
      <td>0.000011</td>
      <td>0.0801</td>
      <td>0.721</td>
      <td>122.028</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2VxeLyX666F8uXCJ0dZF8B</td>
      <td>Shallow</td>
      <td>86</td>
      <td>0.572</td>
      <td>0.385</td>
      <td>7.0</td>
      <td>-6.362</td>
      <td>1.0</td>
      <td>0.0308</td>
      <td>0.37100</td>
      <td>0.000000</td>
      <td>0.2310</td>
      <td>0.323</td>
      <td>95.799</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2IF2XQ095Qqf6tBL9Y4vZn</td>
      <td>Right As Rain</td>
      <td>51</td>
      <td>0.842</td>
      <td>0.678</td>
      <td>1.0</td>
      <td>-5.878</td>
      <td>1.0</td>
      <td>0.0849</td>
      <td>0.77500</td>
      <td>0.000000</td>
      <td>0.0891</td>
      <td>0.920</td>
      <td>137.194</td>
    </tr>
    <tr>
      <th>9</th>
      <td>6F5c58TMEs1byxUstkzVeM</td>
      <td>Roar</td>
      <td>75</td>
      <td>0.554</td>
      <td>0.772</td>
      <td>7.0</td>
      <td>-4.821</td>
      <td>0.0</td>
      <td>0.0418</td>
      <td>0.00487</td>
      <td>0.000007</td>
      <td>0.3540</td>
      <td>0.455</td>
      <td>179.984</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3xrn9i8zhNZsTtcoWgQEAd</td>
      <td>Since U Been Gone</td>
      <td>73</td>
      <td>0.662</td>
      <td>0.741</td>
      <td>0.0</td>
      <td>-5.406</td>
      <td>1.0</td>
      <td>0.0334</td>
      <td>0.00165</td>
      <td>0.030300</td>
      <td>0.1140</td>
      <td>0.404</td>
      <td>131.000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>083Qf6hn6sFL6xiOHlZUyn</td>
      <td>I'll Be There</td>
      <td>71</td>
      <td>0.623</td>
      <td>0.851</td>
      <td>7.0</td>
      <td>-3.111</td>
      <td>1.0</td>
      <td>0.0409</td>
      <td>0.02280</td>
      <td>0.000000</td>
      <td>0.1200</td>
      <td>0.400</td>
      <td>100.063</td>
    </tr>
    <tr>
      <th>12</th>
      <td>7uYl7xgDeAOHP98obvrJvB</td>
      <td>Who Knew</td>
      <td>69</td>
      <td>0.688</td>
      <td>0.733</td>
      <td>9.0</td>
      <td>-4.569</td>
      <td>1.0</td>
      <td>0.0274</td>
      <td>0.00462</td>
      <td>0.000000</td>
      <td>0.0756</td>
      <td>0.459</td>
      <td>140.004</td>
    </tr>
    <tr>
      <th>13</th>
      <td>39jXnbACjiaiTwwhsr5sY5</td>
      <td>Too Much To Ask</td>
      <td>73</td>
      <td>0.443</td>
      <td>0.533</td>
      <td>0.0</td>
      <td>-6.549</td>
      <td>1.0</td>
      <td>0.0396</td>
      <td>0.37100</td>
      <td>0.000000</td>
      <td>0.1280</td>
      <td>0.201</td>
      <td>77.342</td>
    </tr>
    <tr>
      <th>14</th>
      <td>5TMjhlh25Oitlh3LBKdfMi</td>
      <td>Broken Home</td>
      <td>56</td>
      <td>0.585</td>
      <td>0.631</td>
      <td>10.0</td>
      <td>-5.522</td>
      <td>0.0</td>
      <td>0.0264</td>
      <td>0.12800</td>
      <td>0.000000</td>
      <td>0.1050</td>
      <td>0.500</td>
      <td>128.001</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0WPXlTF9IADmeaX86DoUr8</td>
      <td>Melt My Heart To Stone</td>
      <td>57</td>
      <td>0.354</td>
      <td>0.387</td>
      <td>11.0</td>
      <td>-7.066</td>
      <td>0.0</td>
      <td>0.0373</td>
      <td>0.35900</td>
      <td>0.000000</td>
      <td>0.2480</td>
      <td>0.208</td>
      <td>80.915</td>
    </tr>
    <tr>
      <th>16</th>
      <td>3DQisSEr1TLp9H0BEeKiQS</td>
      <td>Uncover</td>
      <td>66</td>
      <td>0.556</td>
      <td>0.529</td>
      <td>2.0</td>
      <td>-4.464</td>
      <td>1.0</td>
      <td>0.0250</td>
      <td>0.40000</td>
      <td>0.000000</td>
      <td>0.2680</td>
      <td>0.308</td>
      <td>89.887</td>
    </tr>
    <tr>
      <th>17</th>
      <td>4RE3vueod5PL48rvHtuu9C</td>
      <td>Peer Pressure</td>
      <td>74</td>
      <td>0.631</td>
      <td>0.715</td>
      <td>1.0</td>
      <td>-6.083</td>
      <td>0.0</td>
      <td>0.0277</td>
      <td>0.02990</td>
      <td>0.000000</td>
      <td>0.1220</td>
      <td>0.420</td>
      <td>135.826</td>
    </tr>
    <tr>
      <th>18</th>
      <td>52FKX00U3PnzrBQmbMTB8b</td>
      <td>Come Away With Me</td>
      <td>57</td>
      <td>0.380</td>
      <td>0.119</td>
      <td>0.0</td>
      <td>-14.246</td>
      <td>1.0</td>
      <td>0.0332</td>
      <td>0.91100</td>
      <td>0.000002</td>
      <td>0.1490</td>
      <td>0.156</td>
      <td>163.139</td>
    </tr>
    <tr>
      <th>19</th>
      <td>5Ohxk2dO5COHF1krpoPigN</td>
      <td>Sign of the Times</td>
      <td>81</td>
      <td>0.516</td>
      <td>0.595</td>
      <td>5.0</td>
      <td>-4.630</td>
      <td>1.0</td>
      <td>0.0313</td>
      <td>0.02750</td>
      <td>0.000000</td>
      <td>0.1090</td>
      <td>0.222</td>
      <td>119.972</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ref song 'When We Were Young' track features
ref = pd.Series(requests.get('https://api.spotify.com/v1/audio-features/7IWkJwX9C0J7tHurTD7ViL', headers=headers).json())[:-7]
```


```python
ref
```




    danceability         0.381
    energy               0.594
    key                      3
    loudness             -5.97
    mode                     1
    speechiness         0.0486
    acousticness         0.348
    instrumentalness         0
    liveness            0.0925
    valence              0.273
    tempo               143.86
    dtype: object



### Calculate the distances of audio features between the list of recommendation and the reference song, by making a vector of audio feature difference and get its norm, for each song


```python
holder = []
stepper = 0

while stepper != len(recomm_df):
    v = (recomm_df.iloc[stepper, 3:] - ref)
    holder.append(np.linalg.norm(v.astype('float').values))
    stepper += 1
    
recomm_df['distance'] = holder
```


```python
recomm_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>popularity</th>
      <th>danceability</th>
      <th>energy</th>
      <th>key</th>
      <th>loudness</th>
      <th>mode</th>
      <th>speechiness</th>
      <th>acousticness</th>
      <th>instrumentalness</th>
      <th>liveness</th>
      <th>valence</th>
      <th>tempo</th>
      <th>distance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1wVcLKdJ4AFKPhKucNvEpy</td>
      <td>Beneath Your Beautiful</td>
      <td>56</td>
      <td>0.558</td>
      <td>0.522</td>
      <td>2.0</td>
      <td>-5.857</td>
      <td>1.0</td>
      <td>0.0360</td>
      <td>0.22800</td>
      <td>0.000000</td>
      <td>0.1040</td>
      <td>0.228</td>
      <td>83.977</td>
      <td>59.891900</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24cKN8P2uGWypxTw5WaNlq</td>
      <td>Don't You Remember</td>
      <td>64</td>
      <td>0.640</td>
      <td>0.395</td>
      <td>3.0</td>
      <td>-5.689</td>
      <td>1.0</td>
      <td>0.0307</td>
      <td>0.20600</td>
      <td>0.000000</td>
      <td>0.0935</td>
      <td>0.235</td>
      <td>115.082</td>
      <td>28.781606</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6yLX8QnxlnEqZfs3YKCfjF</td>
      <td>Tears Dry On Their Own</td>
      <td>66</td>
      <td>0.643</td>
      <td>0.871</td>
      <td>1.0</td>
      <td>-2.734</td>
      <td>0.0</td>
      <td>0.1180</td>
      <td>0.49100</td>
      <td>0.000000</td>
      <td>0.2900</td>
      <td>0.452</td>
      <td>121.569</td>
      <td>22.640717</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2YlZnw2ikdb837oKMKjBkW</td>
      <td>Like I'm Gonna Lose You (feat. John Legend)</td>
      <td>78</td>
      <td>0.630</td>
      <td>0.530</td>
      <td>0.0</td>
      <td>-7.259</td>
      <td>1.0</td>
      <td>0.0434</td>
      <td>0.40000</td>
      <td>0.000000</td>
      <td>0.1770</td>
      <td>0.417</td>
      <td>108.038</td>
      <td>35.971849</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7nXq1vaZiz7PdbfojpPjW5</td>
      <td>Fighter</td>
      <td>68</td>
      <td>0.435</td>
      <td>0.920</td>
      <td>4.0</td>
      <td>-1.357</td>
      <td>0.0</td>
      <td>0.2010</td>
      <td>0.23500</td>
      <td>0.000353</td>
      <td>0.5520</td>
      <td>0.450</td>
      <td>188.899</td>
      <td>45.300982</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1V6gIisPpYqgFeWbMLI0bA</td>
      <td>Heart Attack</td>
      <td>74</td>
      <td>0.504</td>
      <td>0.785</td>
      <td>8.0</td>
      <td>-4.802</td>
      <td>1.0</td>
      <td>0.1040</td>
      <td>0.07380</td>
      <td>0.000000</td>
      <td>0.2390</td>
      <td>0.502</td>
      <td>173.968</td>
      <td>30.546025</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0KAiuUOrLTIkzkpfpn9jb9</td>
      <td>Drive By</td>
      <td>74</td>
      <td>0.765</td>
      <td>0.837</td>
      <td>1.0</td>
      <td>-3.113</td>
      <td>0.0</td>
      <td>0.0320</td>
      <td>0.00107</td>
      <td>0.000011</td>
      <td>0.0801</td>
      <td>0.721</td>
      <td>122.028</td>
      <td>22.143321</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2VxeLyX666F8uXCJ0dZF8B</td>
      <td>Shallow</td>
      <td>86</td>
      <td>0.572</td>
      <td>0.385</td>
      <td>7.0</td>
      <td>-6.362</td>
      <td>1.0</td>
      <td>0.0308</td>
      <td>0.37100</td>
      <td>0.000000</td>
      <td>0.2310</td>
      <td>0.323</td>
      <td>95.799</td>
      <td>48.229826</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2IF2XQ095Qqf6tBL9Y4vZn</td>
      <td>Right As Rain</td>
      <td>51</td>
      <td>0.842</td>
      <td>0.678</td>
      <td>1.0</td>
      <td>-5.878</td>
      <td>1.0</td>
      <td>0.0849</td>
      <td>0.77500</td>
      <td>0.000000</td>
      <td>0.0891</td>
      <td>0.920</td>
      <td>137.194</td>
      <td>7.018965</td>
    </tr>
    <tr>
      <th>9</th>
      <td>6F5c58TMEs1byxUstkzVeM</td>
      <td>Roar</td>
      <td>75</td>
      <td>0.554</td>
      <td>0.772</td>
      <td>7.0</td>
      <td>-4.821</td>
      <td>0.0</td>
      <td>0.0418</td>
      <td>0.00487</td>
      <td>0.000007</td>
      <td>0.3540</td>
      <td>0.455</td>
      <td>179.984</td>
      <td>36.380551</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3xrn9i8zhNZsTtcoWgQEAd</td>
      <td>Since U Been Gone</td>
      <td>73</td>
      <td>0.662</td>
      <td>0.741</td>
      <td>0.0</td>
      <td>-5.406</td>
      <td>1.0</td>
      <td>0.0334</td>
      <td>0.00165</td>
      <td>0.030300</td>
      <td>0.1140</td>
      <td>0.404</td>
      <td>131.000</td>
      <td>13.226375</td>
    </tr>
    <tr>
      <th>11</th>
      <td>083Qf6hn6sFL6xiOHlZUyn</td>
      <td>I'll Be There</td>
      <td>71</td>
      <td>0.623</td>
      <td>0.851</td>
      <td>7.0</td>
      <td>-3.111</td>
      <td>1.0</td>
      <td>0.0409</td>
      <td>0.02280</td>
      <td>0.000000</td>
      <td>0.1200</td>
      <td>0.400</td>
      <td>100.063</td>
      <td>44.074918</td>
    </tr>
    <tr>
      <th>12</th>
      <td>7uYl7xgDeAOHP98obvrJvB</td>
      <td>Who Knew</td>
      <td>69</td>
      <td>0.688</td>
      <td>0.733</td>
      <td>9.0</td>
      <td>-4.569</td>
      <td>1.0</td>
      <td>0.0274</td>
      <td>0.00462</td>
      <td>0.000000</td>
      <td>0.0756</td>
      <td>0.459</td>
      <td>140.004</td>
      <td>7.286861</td>
    </tr>
    <tr>
      <th>13</th>
      <td>39jXnbACjiaiTwwhsr5sY5</td>
      <td>Too Much To Ask</td>
      <td>73</td>
      <td>0.443</td>
      <td>0.533</td>
      <td>0.0</td>
      <td>-6.549</td>
      <td>1.0</td>
      <td>0.0396</td>
      <td>0.37100</td>
      <td>0.000000</td>
      <td>0.1280</td>
      <td>0.201</td>
      <td>77.342</td>
      <td>66.588244</td>
    </tr>
    <tr>
      <th>14</th>
      <td>5TMjhlh25Oitlh3LBKdfMi</td>
      <td>Broken Home</td>
      <td>56</td>
      <td>0.585</td>
      <td>0.631</td>
      <td>10.0</td>
      <td>-5.522</td>
      <td>0.0</td>
      <td>0.0264</td>
      <td>0.12800</td>
      <td>0.000000</td>
      <td>0.1050</td>
      <td>0.500</td>
      <td>128.001</td>
      <td>17.373893</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0WPXlTF9IADmeaX86DoUr8</td>
      <td>Melt My Heart To Stone</td>
      <td>57</td>
      <td>0.354</td>
      <td>0.387</td>
      <td>11.0</td>
      <td>-7.066</td>
      <td>0.0</td>
      <td>0.0373</td>
      <td>0.35900</td>
      <td>0.000000</td>
      <td>0.2480</td>
      <td>0.208</td>
      <td>80.915</td>
      <td>63.469256</td>
    </tr>
    <tr>
      <th>16</th>
      <td>3DQisSEr1TLp9H0BEeKiQS</td>
      <td>Uncover</td>
      <td>66</td>
      <td>0.556</td>
      <td>0.529</td>
      <td>2.0</td>
      <td>-4.464</td>
      <td>1.0</td>
      <td>0.0250</td>
      <td>0.40000</td>
      <td>0.000000</td>
      <td>0.2680</td>
      <td>0.308</td>
      <td>89.887</td>
      <td>54.003916</td>
    </tr>
    <tr>
      <th>17</th>
      <td>4RE3vueod5PL48rvHtuu9C</td>
      <td>Peer Pressure</td>
      <td>74</td>
      <td>0.631</td>
      <td>0.715</td>
      <td>1.0</td>
      <td>-6.083</td>
      <td>0.0</td>
      <td>0.0277</td>
      <td>0.02990</td>
      <td>0.000000</td>
      <td>0.1220</td>
      <td>0.420</td>
      <td>135.826</td>
      <td>8.352195</td>
    </tr>
    <tr>
      <th>18</th>
      <td>52FKX00U3PnzrBQmbMTB8b</td>
      <td>Come Away With Me</td>
      <td>57</td>
      <td>0.380</td>
      <td>0.119</td>
      <td>0.0</td>
      <td>-14.246</td>
      <td>1.0</td>
      <td>0.0332</td>
      <td>0.91100</td>
      <td>0.000002</td>
      <td>0.1490</td>
      <td>0.156</td>
      <td>163.139</td>
      <td>21.206879</td>
    </tr>
    <tr>
      <th>19</th>
      <td>5Ohxk2dO5COHF1krpoPigN</td>
      <td>Sign of the Times</td>
      <td>81</td>
      <td>0.516</td>
      <td>0.595</td>
      <td>5.0</td>
      <td>-4.630</td>
      <td>1.0</td>
      <td>0.0313</td>
      <td>0.02750</td>
      <td>0.000000</td>
      <td>0.1090</td>
      <td>0.222</td>
      <td>119.972</td>
      <td>24.011586</td>
    </tr>
  </tbody>
</table>
</div>



### Sort songs by distance to see the closest and furthest songs


```python
recomm_df_sort = recomm_df.sort_values(by='distance')
recomm_df_sort.reset_index(inplace=True)
recomm_df_sort
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>id</th>
      <th>name</th>
      <th>popularity</th>
      <th>danceability</th>
      <th>energy</th>
      <th>key</th>
      <th>loudness</th>
      <th>mode</th>
      <th>speechiness</th>
      <th>acousticness</th>
      <th>instrumentalness</th>
      <th>liveness</th>
      <th>valence</th>
      <th>tempo</th>
      <th>distance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>2IF2XQ095Qqf6tBL9Y4vZn</td>
      <td>Right As Rain</td>
      <td>51</td>
      <td>0.842</td>
      <td>0.678</td>
      <td>1.0</td>
      <td>-5.878</td>
      <td>1.0</td>
      <td>0.0849</td>
      <td>0.77500</td>
      <td>0.000000</td>
      <td>0.0891</td>
      <td>0.920</td>
      <td>137.194</td>
      <td>7.018965</td>
    </tr>
    <tr>
      <th>1</th>
      <td>12</td>
      <td>7uYl7xgDeAOHP98obvrJvB</td>
      <td>Who Knew</td>
      <td>69</td>
      <td>0.688</td>
      <td>0.733</td>
      <td>9.0</td>
      <td>-4.569</td>
      <td>1.0</td>
      <td>0.0274</td>
      <td>0.00462</td>
      <td>0.000000</td>
      <td>0.0756</td>
      <td>0.459</td>
      <td>140.004</td>
      <td>7.286861</td>
    </tr>
    <tr>
      <th>2</th>
      <td>17</td>
      <td>4RE3vueod5PL48rvHtuu9C</td>
      <td>Peer Pressure</td>
      <td>74</td>
      <td>0.631</td>
      <td>0.715</td>
      <td>1.0</td>
      <td>-6.083</td>
      <td>0.0</td>
      <td>0.0277</td>
      <td>0.02990</td>
      <td>0.000000</td>
      <td>0.1220</td>
      <td>0.420</td>
      <td>135.826</td>
      <td>8.352195</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10</td>
      <td>3xrn9i8zhNZsTtcoWgQEAd</td>
      <td>Since U Been Gone</td>
      <td>73</td>
      <td>0.662</td>
      <td>0.741</td>
      <td>0.0</td>
      <td>-5.406</td>
      <td>1.0</td>
      <td>0.0334</td>
      <td>0.00165</td>
      <td>0.030300</td>
      <td>0.1140</td>
      <td>0.404</td>
      <td>131.000</td>
      <td>13.226375</td>
    </tr>
    <tr>
      <th>4</th>
      <td>14</td>
      <td>5TMjhlh25Oitlh3LBKdfMi</td>
      <td>Broken Home</td>
      <td>56</td>
      <td>0.585</td>
      <td>0.631</td>
      <td>10.0</td>
      <td>-5.522</td>
      <td>0.0</td>
      <td>0.0264</td>
      <td>0.12800</td>
      <td>0.000000</td>
      <td>0.1050</td>
      <td>0.500</td>
      <td>128.001</td>
      <td>17.373893</td>
    </tr>
    <tr>
      <th>5</th>
      <td>18</td>
      <td>52FKX00U3PnzrBQmbMTB8b</td>
      <td>Come Away With Me</td>
      <td>57</td>
      <td>0.380</td>
      <td>0.119</td>
      <td>0.0</td>
      <td>-14.246</td>
      <td>1.0</td>
      <td>0.0332</td>
      <td>0.91100</td>
      <td>0.000002</td>
      <td>0.1490</td>
      <td>0.156</td>
      <td>163.139</td>
      <td>21.206879</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>0KAiuUOrLTIkzkpfpn9jb9</td>
      <td>Drive By</td>
      <td>74</td>
      <td>0.765</td>
      <td>0.837</td>
      <td>1.0</td>
      <td>-3.113</td>
      <td>0.0</td>
      <td>0.0320</td>
      <td>0.00107</td>
      <td>0.000011</td>
      <td>0.0801</td>
      <td>0.721</td>
      <td>122.028</td>
      <td>22.143321</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2</td>
      <td>6yLX8QnxlnEqZfs3YKCfjF</td>
      <td>Tears Dry On Their Own</td>
      <td>66</td>
      <td>0.643</td>
      <td>0.871</td>
      <td>1.0</td>
      <td>-2.734</td>
      <td>0.0</td>
      <td>0.1180</td>
      <td>0.49100</td>
      <td>0.000000</td>
      <td>0.2900</td>
      <td>0.452</td>
      <td>121.569</td>
      <td>22.640717</td>
    </tr>
    <tr>
      <th>8</th>
      <td>19</td>
      <td>5Ohxk2dO5COHF1krpoPigN</td>
      <td>Sign of the Times</td>
      <td>81</td>
      <td>0.516</td>
      <td>0.595</td>
      <td>5.0</td>
      <td>-4.630</td>
      <td>1.0</td>
      <td>0.0313</td>
      <td>0.02750</td>
      <td>0.000000</td>
      <td>0.1090</td>
      <td>0.222</td>
      <td>119.972</td>
      <td>24.011586</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1</td>
      <td>24cKN8P2uGWypxTw5WaNlq</td>
      <td>Don't You Remember</td>
      <td>64</td>
      <td>0.640</td>
      <td>0.395</td>
      <td>3.0</td>
      <td>-5.689</td>
      <td>1.0</td>
      <td>0.0307</td>
      <td>0.20600</td>
      <td>0.000000</td>
      <td>0.0935</td>
      <td>0.235</td>
      <td>115.082</td>
      <td>28.781606</td>
    </tr>
    <tr>
      <th>10</th>
      <td>5</td>
      <td>1V6gIisPpYqgFeWbMLI0bA</td>
      <td>Heart Attack</td>
      <td>74</td>
      <td>0.504</td>
      <td>0.785</td>
      <td>8.0</td>
      <td>-4.802</td>
      <td>1.0</td>
      <td>0.1040</td>
      <td>0.07380</td>
      <td>0.000000</td>
      <td>0.2390</td>
      <td>0.502</td>
      <td>173.968</td>
      <td>30.546025</td>
    </tr>
    <tr>
      <th>11</th>
      <td>3</td>
      <td>2YlZnw2ikdb837oKMKjBkW</td>
      <td>Like I'm Gonna Lose You (feat. John Legend)</td>
      <td>78</td>
      <td>0.630</td>
      <td>0.530</td>
      <td>0.0</td>
      <td>-7.259</td>
      <td>1.0</td>
      <td>0.0434</td>
      <td>0.40000</td>
      <td>0.000000</td>
      <td>0.1770</td>
      <td>0.417</td>
      <td>108.038</td>
      <td>35.971849</td>
    </tr>
    <tr>
      <th>12</th>
      <td>9</td>
      <td>6F5c58TMEs1byxUstkzVeM</td>
      <td>Roar</td>
      <td>75</td>
      <td>0.554</td>
      <td>0.772</td>
      <td>7.0</td>
      <td>-4.821</td>
      <td>0.0</td>
      <td>0.0418</td>
      <td>0.00487</td>
      <td>0.000007</td>
      <td>0.3540</td>
      <td>0.455</td>
      <td>179.984</td>
      <td>36.380551</td>
    </tr>
    <tr>
      <th>13</th>
      <td>11</td>
      <td>083Qf6hn6sFL6xiOHlZUyn</td>
      <td>I'll Be There</td>
      <td>71</td>
      <td>0.623</td>
      <td>0.851</td>
      <td>7.0</td>
      <td>-3.111</td>
      <td>1.0</td>
      <td>0.0409</td>
      <td>0.02280</td>
      <td>0.000000</td>
      <td>0.1200</td>
      <td>0.400</td>
      <td>100.063</td>
      <td>44.074918</td>
    </tr>
    <tr>
      <th>14</th>
      <td>4</td>
      <td>7nXq1vaZiz7PdbfojpPjW5</td>
      <td>Fighter</td>
      <td>68</td>
      <td>0.435</td>
      <td>0.920</td>
      <td>4.0</td>
      <td>-1.357</td>
      <td>0.0</td>
      <td>0.2010</td>
      <td>0.23500</td>
      <td>0.000353</td>
      <td>0.5520</td>
      <td>0.450</td>
      <td>188.899</td>
      <td>45.300982</td>
    </tr>
    <tr>
      <th>15</th>
      <td>7</td>
      <td>2VxeLyX666F8uXCJ0dZF8B</td>
      <td>Shallow</td>
      <td>86</td>
      <td>0.572</td>
      <td>0.385</td>
      <td>7.0</td>
      <td>-6.362</td>
      <td>1.0</td>
      <td>0.0308</td>
      <td>0.37100</td>
      <td>0.000000</td>
      <td>0.2310</td>
      <td>0.323</td>
      <td>95.799</td>
      <td>48.229826</td>
    </tr>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>3DQisSEr1TLp9H0BEeKiQS</td>
      <td>Uncover</td>
      <td>66</td>
      <td>0.556</td>
      <td>0.529</td>
      <td>2.0</td>
      <td>-4.464</td>
      <td>1.0</td>
      <td>0.0250</td>
      <td>0.40000</td>
      <td>0.000000</td>
      <td>0.2680</td>
      <td>0.308</td>
      <td>89.887</td>
      <td>54.003916</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0</td>
      <td>1wVcLKdJ4AFKPhKucNvEpy</td>
      <td>Beneath Your Beautiful</td>
      <td>56</td>
      <td>0.558</td>
      <td>0.522</td>
      <td>2.0</td>
      <td>-5.857</td>
      <td>1.0</td>
      <td>0.0360</td>
      <td>0.22800</td>
      <td>0.000000</td>
      <td>0.1040</td>
      <td>0.228</td>
      <td>83.977</td>
      <td>59.891900</td>
    </tr>
    <tr>
      <th>18</th>
      <td>15</td>
      <td>0WPXlTF9IADmeaX86DoUr8</td>
      <td>Melt My Heart To Stone</td>
      <td>57</td>
      <td>0.354</td>
      <td>0.387</td>
      <td>11.0</td>
      <td>-7.066</td>
      <td>0.0</td>
      <td>0.0373</td>
      <td>0.35900</td>
      <td>0.000000</td>
      <td>0.2480</td>
      <td>0.208</td>
      <td>80.915</td>
      <td>63.469256</td>
    </tr>
    <tr>
      <th>19</th>
      <td>13</td>
      <td>39jXnbACjiaiTwwhsr5sY5</td>
      <td>Too Much To Ask</td>
      <td>73</td>
      <td>0.443</td>
      <td>0.533</td>
      <td>0.0</td>
      <td>-6.549</td>
      <td>1.0</td>
      <td>0.0396</td>
      <td>0.37100</td>
      <td>0.000000</td>
      <td>0.1280</td>
      <td>0.201</td>
      <td>77.342</td>
      <td>66.588244</td>
    </tr>
  </tbody>
</table>
</div>



### Visualize the song closest to the audio features of 'When We Were Young'


```python
import plotly.graph_objects as go

categories = ['danceability', 'energy', 'key', 
              'loudness', 'mode', 'speechiness', 
              'acousticness', 'instrumentalness',
              'liveness', 'valence', 'tempo']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=recomm_df_sort.iloc[0, :-1],
      theta=categories,
      fill='toself',
      name='The closest song'
))

fig.add_trace(go.Scatterpolar(
      r=ref.values,
      theta=categories,
      fill='toself',
      name='When We Were Young'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 0.5]
    )),
  showlegend=True
)

fig.show()
```

### Visualize the song furthest to the audio features of 'When We Were Young'


```python
categories = ['danceability', 'energy', 'key', 
              'loudness', 'mode', 'speechiness', 
              'acousticness', 'instrumentalness',
              'liveness', 'valence', 'tempo']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=recomm_df_sort.iloc[len(recomm_df_sort)-1, :-1],
      theta=categories,
      fill='toself',
      name='The furthest song'
))

fig.add_trace(go.Scatterpolar(
      r=ref.values,
      theta=categories,
      fill='toself',
      name='When We Were Young'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 0.5]
    )),
  showlegend=True
)

fig.show()
```
