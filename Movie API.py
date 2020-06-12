import requests

#example = https://api.themoviedb.org/3/movie/550?api_key=<<api_key>>

#Connecting to API
api_key = "<<api_key>>"
api_base_url = "https://api.themoviedb.org/3"
movie = "The Matrix"
endpoint_path = f"/search/movie"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={movie}"

#Sending HTTP request
r = requests.get(endpoint)

#Getiing data from API
data = r.json()
results = data['results']

for result in results:
    print("\n")
    info = {'Name':result['original_title'],
            'Release Date' : result['release_date'],
            'Popularity' : result['popularity'],
            'Votes' : result['vote_count'],
            'Overview': result['overview']}
    for i in info.keys():
        print(f"{i} : {info[i]}")