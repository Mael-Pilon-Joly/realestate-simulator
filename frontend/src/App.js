import logo from './logo.svg';
import './App.css';
import { getHabitants } from "./server";
import React, { useState, useEffect } from "react";

function App() {
  const [habitants, setHabitants] = useState([]);
  
  useEffect(() => {
    getHabitants()
      .then(response => {
        setHabitants(response.data);
      })
      .catch(error => console.log(error));
  }, []);

  const listItems = habitants.map(habitant =>
    <li key={habitant.id}>
      {habitant.age}
      {habitant.est_employe}
      {habitant.satisfaction}
    </li>
  );

  return (
    <div>
      <ul>
        {listItems}
      </ul>
    </div>
  );
}

export default App;
