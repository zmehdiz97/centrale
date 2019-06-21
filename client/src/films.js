import React from 'react';
import superagent from "superagent"
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';

export function Movies() {
  const [tri, setTri] = React.useState(null);
  const [movies, setMovies] = React.useState(null);
  React.useEffect(() => {
    superagent
      .get("http://localhost:5000/application/movie/getall")
      .then(response => setMovies(response.body));
  }, []);
  return (
    <div>
      <h2>Movies</h2>
        <form>
            <input type="button" id="search-btn" value="drame" onClick= {() => setMovies(Filtre(movies,"drame",setTri,tri))}/>&nbsp;
            <input type="button" id="search-btn" value="crime" onClick= {() => setMovies(Filtre(movies,"crime",setTri,tri))}/>&nbsp;
            <input type="button" id="search-btn" value="aventure" onClick= {() => setMovies(Filtre(movies,"aventure",setTri,tri))}/>&nbsp;
            <input type="button" id="search-btn" value="romance" onClick= {() => setMovies(Filtre(movies,"romance",setTri,tri))}/>&nbsp;

        </form>
        <form>
            <button onclick= "javascript:location.reload();" href="#bas_de_page">All Movies</button>
        </form>
        <div>
            <div className = "classer_note">
            Recommondons pour vous :
            <button onClick= {() => setMovies(Trier3(movies,setTri,tri))}>
            Cliquez ici!
            </button>
            <p>
            </p>
            </div>
        </div>
        <form>
        search:<input type="text" id="search" name="number"/><br/>
        <input type="button" id="search-btn" value="search" onClick={() => setMovies(chercher(movies,setTri,tri))}/>
        </form>
        <div>
            <tr>
                {movies && movies.map(movie => (<td id="tabtd"> {movie.name} ({movie.year})</td>))}
            </tr>
            <tr>
                {movies && movies.map(movie => (<td><img src={movie.affiche}/></td>))}
            </tr>
            <tr>
                {movies && movies.map(movie => (<td id="tabtd"><div>{movie.notes}</div></td>))}
            </tr>

        </div>
    </div>
  );
}
function chercher(movies,setTri,tri){
var film_name=document.getElementById("search").value
var   tmp=movies
 setTri(tri + 1)
 if (movies)
  tmp = movies.filter(x => x.name == film_name)
return (tmp)
}
function Trier3(movies,setTri,tri){
    var tmp = movies
    setTri(tri + 1)
    { movies && tmp.sort(function(a,b){ return b.notes - a.notes})}
    return(tmp)
}

function Filtre(movies,a,setTri,tri)
{ var tmp = movies
  setTri(tri + 1)
 if (movies)
  tmp = movies.filter(x => x.genre.includes(a))
return(tmp)
}

function all(movies,setTri,tri)
{ var tmp = movies
  setTri(tri + 1)
  if (movies)
  tmp = movies.filter(x => x.genre.contains("drame romance action aventure crime scincefiction") )
return(tmp)
}

