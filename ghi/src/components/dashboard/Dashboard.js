import React from 'react'
import NavBar from '../navbar';
import DateObject from "react-date-object";
import { useEffect, useState } from 'react';
import { Card, CardBody, CardTitle, CardSubtitle, Table } from "reactstrap";
import { NavLogo } from '../navbar/NavbarElements';
// import ErrorNotification from '../../ErrorNotification'
// import { Link } from 'react-router-dom';
import CoverEventFormModal from '../events/CoverEventFormModal';
import SwapEventFormModal from '../events/SwapEventFormModal';

import styles from "./Dashboard.module.css"
import { useGetTokenQuery, useGetUserCoverEventsQuery, useGetUserShiftSwapEventsQuery } from '../../store/UsersApi';
import SideNavbar from './dashboardNav';


function Dashboard() {

    const [isOpenCover, setIsOpenCover] = useState(false);
    const [isOpenSwap, setIsOpenSwap] = useState(false);
    const [isOpen, setIsOpen] = useState(false)
    const {data: userData, isLoading: isLoadingUser} = useGetTokenQuery();
    const { data: eventData, isLoading: isLoadingEvent } = useGetUserCoverEventsQuery();
    const { data: shiftData, isLoading: isLoadingShift } = useGetUserShiftSwapEventsQuery();
    if (isLoadingEvent || isLoadingShift || isLoadingUser) {
      return (
        <progress className="progress is-primary" max="100"></progress>
        );
      }
    const user = userData.user.first_name
    const toggle = () => {
      setIsOpen(!isOpen)
  }


  return (
    <>
        {/* <SideNavbar /> */}
        {/* <NavBar toggle={toggle} /> */}
        <h1 classname="">
            Hello, {user}!
        </h1>
        <div>
          <Card>
            <CardBody>
              <NavLogo tag="h5" color="#6C63FF">Your Cover Events</NavLogo>
              <Table className="border table-striped no-wrap mt-3 align-middle" response border>
                <thead>
                  <tr>
                    <th>Availability Start</th>
                    <th>Availability End</th>
                    <th>Team</th>
                  </tr>
                </thead>
                <tbody>
                  {
                  eventData.map((event) => {
                    let start = new DateObject(event.availability_start)
                    let end = new DateObject(event.availability_end)
                    let start_date = start.format("ddd DD MMM YYYY, hh:mm a")
                    let end_date = end.format("ddd DD MMM YYYY, hh:mm a")
                    return (
                    <tr key={event.id}>
                    <td>{start_date}</td>
                    <td>{end_date}</td>
                    <td>{event.team_name}</td>
                    </tr>
                  );
                  })}
                </tbody>
              </Table>
              <button className={styles.primaryBtn} onClick={() => setIsOpenCover(true)}>Create Cover Event</button>{isOpenCover && <CoverEventFormModal setIsOpenCover={setIsOpenCover} />}
              <button className={styles.primaryBtn} onClick={() => setIsOpenSwap(true)}>Create Swap Event</button>{isOpenSwap && <SwapEventFormModal setIsOpenSwap={setIsOpenSwap} />}
              <NavLogo tag="h5" color="#6C63FF">Your Shift Swap Events</NavLogo>
              <Table className="border table-striped no-wrap mt-3 align-middle" response border>
                <thead>
                    <tr>
                      <th>Shift Start</th>
                      <th>Shift End</th>
                      <th>Availability Start</th>
                      <th>Availability End</th>
                      <th>Team</th>
                    </tr>
                  </thead>
                  <tbody>
                    {shiftData.map((event) => {
                      let shift_s = new DateObject(event.shift_start)
                      let shift_start = shift_s.format("ddd DD MMM YYYY, hh:mm a")
                      let shift_e = new DateObject(event.shift_end)
                      let shift_end = shift_e.format("ddd DD MMM YYYY, hh:mm a")
                      let start = new DateObject(event.availability_start)
                      let end = new DateObject(event.availability_end)
                      let start_date = start.format("ddd DD MMM YYYY, hh:mm a")
                      let end_date = end.format("ddd DD MMM YYYY, hh:mm a")
                      return (
                      <tr key={event.id}>
                        <td>{shift_start}</td>
                        <td>{shift_end}</td>
                        <td>{start_date}</td>
                        <td>{end_date}</td>
                        <td>{event.team_name}</td>
                      </tr>
                    );
                    })}
                  </tbody>
                  </Table>
            </CardBody>
          </Card>
          
        </div>
    </>
  )
}
export default Dashboard;
