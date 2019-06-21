import requests
r=requests.get("http://localhost:5000/application/movie/getall")
print(r.text)


            <tr>
                {movies && movies.map(movie => (<td id="tabtd"> {movie.name} ({movie.year})</td>))}
            </tr>
            <tr>
                {movies && movies.map(movie => (<td><img src={movie.affiche}/></td>))}
            </tr>
            <tr>
                {movies && movies.map(movie => (<td id="tabtd"><div>{movie.notes}</div></td>))}
            </tr>
