import { useState } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import SignIn from './components/users/signin.js';
import SignUp from './components/users/signup.js';
import { TeamDashboard } from './components/teams/team_dash.js';

import Landing from './pages/landing';
import UserHome from './pages/home';

import { FaBars } from 'react-icons/fa';
import HomeSidebar from './components/dashboard/HomeSidebar.js';

import { useGetTokenQuery } from './store/UsersApi.js';

import './styles.scss';

function App() {
  const [collapsed, setCollapsed] = useState(false);
  const [toggled, setToggled] = useState(false);
  const { data, error, isLoading } = useGetTokenQuery();

  if (isLoading) {
    return (
      <progress className="progress is-primary" max="100"></progress>
    );
  }
  const handleCollapsedChange = () => {
    setCollapsed(!collapsed);
  };
  const handleToggleSidebar = (value) => {
    setToggled(value);
  };
  return (
    <BrowserRouter>
      {data != null ?
        <div className={`app ${toggled ? 'toggled' : ''}`}>
          <HomeSidebar
            collapsed={collapsed}
            toggled={toggled}
            handleToggleSidebar={handleToggleSidebar}
            handleCollapsedChange={handleCollapsedChange}
          />
          <main>
            <div className="btn-toggle" onClick={() => handleToggleSidebar(true)}>
              <FaBars />
            </div>
            <Routes>
              <Route forceRefresh={true} path='/' element={<UserHome />} />
              <Route path='/team' element={<TeamDashboard />} />
  
            </Routes>
          </main>
        </div>
        :
        <Routes>
          <Route forceRefresh={true} path='/' element={<Landing />} />
          <Route path='/signin' element={<SignIn />} />
          <Route path="signup" element={<SignUp />} />
        </Routes>
      }
    </BrowserRouter>
  );
}
export default App;
