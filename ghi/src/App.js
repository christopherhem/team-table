import {BrowserRouter, Route, Routes} from 'react-router-dom';
import EventFormModal from './components/events/CoverEventFormModal.js';
import SignIn from './components/users/signin.js';
import SignUp from './components/users/signup.js';
import { TeamDashboard } from './components/teams/team_dash.js';

import Landing from './pages/landing';
import UserHome from './pages/home';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path ="events" >
            <Route path="new" element={<EventFormModal/>} />
          </Route>
        <Route path='team' element={<TeamDashboard />} />
        <Route path='/' element={<Landing />} />
        <Route path='home' element={<UserHome />}/>
        <Route path="signup" element={<SignUp />} />
        <Route path='/signin' element={<SignIn />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
