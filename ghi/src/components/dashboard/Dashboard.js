import React from 'react'
import ErrorNotification from '../../ErrorNotification'
import { Link } from 'react-router-dom';
import { useGetUsersQuery } from '../../store/UsersApi';


function Dashboard() {
    const { data, error, isLoading } = useGetUsersQuery();
  return (
    <>
        <h1>
            Hello
        </h1>
    </>
  )
}

export default Dashboard;
