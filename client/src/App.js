import React from 'react';
import logo from './Logo_Netflix.png';
import './App.css';
import {Movies} from './films.js'
import superagent from "superagent"
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';

function App() {
  const [user, setUser] = React.useState(null);
  React.useEffect(() => {
    superagent
        .get("http://localhost:5000/application/user/Mbappe/Kylian")
        .then(response => setUser(response.body.user));
  }, []);
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" width="1600 px" height="500 px"/>
        <Router>
          <p>
          </p>
          <div>
             <div id="tab">
                <tr id="tabtr">
                  <td id="tabtd">
                    <Link to="/home">Home</Link>
                  </td>
                   &nbsp;
                  <td id="tabtd">
                    <Link to="movies">Movies</Link>
                  </td>
                   &nbsp;
                  <td id="tabtd">
                    <Link to="search">Search</Link>
                  </td>
                   &nbsp;
                  <td id="tabtd">
                    <Link to="For you">For you</Link>
                  </td>
                </tr>
             </div>
            <Route exact path="/home" component={Home} />
            <Route exact path="/movies" component={Movies} />
            <Route path="/search" component={Search} />
            <Route path="/For you" component={Foryou} />
          </div>
        </Router>
        <p>
          {user ? (
            <div>
                hello {user.age} {user.last_name}

            </div>
          ) : (
            <div>introuvable</div>
          )}
        </p>
      </header>
    </div>
  );
}

function Home() {
  return (
    <div>
      <h2>Home</h2>
    </div>
  );
}


function Search() {
  var p = document.getElementById("search-btn");
  const [tri, setTri] = React.useState(null);
  const [movies, setMovies] = React.useState(null);
  React.useEffect(() => {
    superagent
      .get("http://localhost:5000/application/movie/getall")
      .then(response => setMovies(response.body));
  }, []);
  return (
    <div>
       <p>
       </p>
        <div className = "connexion" >
        <form>
        username:<input type="text" id="search" name="number"/><br/>
        <input type="button" id="search-btn" value="se connecter" onClick={() => (connecter(movies,setMovies,setTri,tri))}/>
        </form>
            <tr>
                {movies && movies.map(movie => (<td id="tabtd">{movie.name} ({movie.year})</td>))}
            </tr>
            <tr>

                {movies && movies.map(movie => (<td><img src={movie.affiche}/></td>))}
            </tr>
            <tr>
                {movies && movies.map(movie => (<td id="tabtd"><div>{movie.notes}</div></td>))}
            </tr>
        </div>
        <h2> </h2>
    </div>
  );
}

function Hello()
{
var username=document.getElementById("search").value
return(username)
}
function connecter(movies,setMovies,setTri,tri)
{
var username=document.getElementById("search").value
    superagent
     .get("http://localhost:5000/application/user/"+username)
     .then(response => response.status==200?
    setMovies(FiltrerUser(movies,response.body.films)): null);
  setTri(tri + 1)
return (<div> Bonjour {username} </div>);
}

function FiltrerUser(movies,films)
{var tmp = movies
 if (movies)
  tmp = movies.filter(x => !(films.includes(x.name)))
return(tmp)
}

function Foryou() {
  return (
    <div>
        <h2>
          Best Movies
        </h2>
        <tr class="ligne1">
            <td class="poster du film">
                <a href="./film_1">
                    <img src="https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY67_CR0,0,45,67_AL_.jpg" width="45" height="67" alt="Les évadés"/>
                </a>
            </td>
            <td class="titleColumn">
                1.
                <a href="./film_1" title="Frank Darabont (dir.), Tim Robbins, Morgan Freeman">Les évadés</a>
                <span class="secondaryInfo">(1994)</span>
            </td>
            <td class="ratingColumn">
                9,2
            </td>
        </tr>
        <tr class="ligne2">
            <td class="poster du film">
                <a href="./film_2">
                    <img src="https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY67_CR1,0,45,67_AL_.jpg" width="45" height="67" alt="Le parrain"/>
                </a>
            </td>
            <td class="titleColumn">
                2.
                <a href="./film2" title="Francis Ford Coppola (dir.), Marlon Brando, Al Pacino">Le parrain</a>
                <span class="secondaryInfo">(1972)</span>
            </td>
            <td class="ratingColumn">
                9,2
            </td>
        </tr>
    </div>

  );
}

export default App;



function myFunction() {
  document.getElementsByTagName("BODY")[0].style.backgroundColor = "yellow";
}
