// import { useEffect, useState } from 'react';
// import Construct from './Construct.js'
// import ErrorNotification from './ErrorNotification';
// import './App.css';

import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Dashboard from './components/dashboard/Dashboard.js';
import SignIn from './components/users/signin.js';
import SignUp from './components/users/signup.js';
import Home from './pages';



function App() {
  // const [token, login, logout, signup] = useToken();
  // +++++++++++++++++Should remove this?+++++++++++++++++++++++

  // const [launch_info, setLaunchInfo] = useState([]);
  // const [error, setError] = useState(null);

  // useEffect(() => {
  //   async function getData() {
  //     let url = `${process.env.REACT_APP_API_HOST}/api/launch-details`;
  //     console.log('fastapi url: ', url);
  //     let response = await fetch(url);
  //     console.log("------- hello? -------");
  //     let data = await response.json();

  //     if (response.ok) {
  //       console.log("got launch data!");
  //       setLaunchInfo(data.launch_details);
  //     } else {
  //       console.log("drat! something happened");
  //       setError(data.message);
  //     }
  //   }
  //   getData();
  // }, [])

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='dashboard' element={<Dashboard />} />
        <Route path="signup" element={<SignUp />} />
        <Route path='/signin' element={<SignIn />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
