import React from 'react'
import { useEffect, useState } from 'react';
import { Card, CardBody, CardTitle, CardSubtitle, Table } from "reactstrap";
// import ErrorNotification from '../../ErrorNotification'
// import { Link } from 'react-router-dom';
import { useGetTokenQuery, useGetUserCoverEventsQuery } from '../../store/UsersApi';
import CoverEventFormModal from '../events/CoverEventFormModal';
import SwapEventFormModal from '../events/SwapEventFormModal';


import styles from "./Dashboard.module.css"



function Dashboard() {
    const [isOpen, setIsOpen] = useState(false);
    const [isOpenSwap, setIsOpenSwap] = useState(false);
    useGetTokenQuery();
    const { data: eventData } = useGetUserCoverEventsQuery();
    console.log(eventData)
    // if (isLoading) {
    //   return (
    //     <progress className="progress is-primary" max="100"></progress>
    //   );
    // }

  return (
    <>
        <h1>
            Hello, User
        </h1>
        <div>
          <Card>
            <CardBody>
              <CardTitle tag="h5">Your Cover Events</CardTitle>
              <Table clasName="no-wrap mt-3 align-middle" response borderless>
                <thead>
                  <tr>
                    <th>Availability Start</th>
                    <th>Availability End</th>
                    <th>Team</th>
                  </tr>
                </thead>
                <tbody>
                  data.
                </tbody>
              </Table>
              <button className={styles.primaryBtn} onClick={() => setIsOpen(true)}>Create Cover Event</button>{isOpen && <CoverEventFormModal setIsOpen={setIsOpen} />}
              <button className={styles.primaryBtn} onClick={() => setIsOpenSwap(true)}>Create Swap Event</button>{isOpenSwap && <SwapEventFormModal setIsOpenSwap={setIsOpenSwap} />}
            </CardBody>
          </Card>
          
        </div>
    </>
  )
}
export default Dashboard;
