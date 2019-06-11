import React, { useEffect } from "react";
import superagent from "superagent";

import logo from "./logo.svg";
import "./App.css";

const App = () => {
  useEffect(() => {
    async function fetchData() {
      try {
        const res = await superagent.get(
          "http://localhost:8000/application/user/last/first"
        );
        console.log(res);
      } catch (err) {
        console.error(err);
      }
    }
    fetchData();
  }, []);

  return (
    <div className='App'>
      <header className='App-header'>
        <img src={logo} className='App-logo' alt='logo' />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className='App-link'
          href='https://reactjs.org'
          target='_blank'
          rel='noopener noreferrer'
        >
          Learn React
        </a>
      </header>
    </div>
  );
};

export default App;
