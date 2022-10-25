import React from 'react'
import { Link } from 'react-router-dom';
import DateObject from "react-date-object";
import { useState } from 'react';
import { Card, CardBody, Table } from "reactstrap";
import { NavLogo } from '../components/navbar/NavbarElements';
import CoverEventFormModal from '../components/events/CoverEventFormModal';
import SwapEventFormModal from '../components/events/SwapEventFormModal';
import UpdateCoverFormModal from '../components/events/updateCoverModal';
import styles from "../components/dashboard/Home.module.css"
import { useGetTokenQuery, useGetUserCoverEventsQuery, useGetUserShiftSwapEventsQuery } from '../store/UsersApi';
import UpdateShiftFormModal from '../components/events/updateSwapModal';
import { FaBars } from 'react-icons/fa';
import Sidebar from '../components/dashboard/HomeSidebar';

import './styles.scss';

function UserHome() {
    const [isOpenUpdateShift, setIsOpenUpdateShift] = useState(false)
    const [isOpenUpdateCover, setIsOpenUpdateCover] = useState(false)
    const [isOpenCover, setIsOpenCover] = useState(false);
    const [isOpenSwap, setIsOpenSwap] = useState(false);
    const [isOpen, setIsOpen] = useState(false)
    const [collapsed, setCollapsed] = useState(false);
    const [image, setImage] = useState(false);
    const [toggled, setToggled] = useState(false);
    const { data: userData, isLoading: isLoadingUser } = useGetTokenQuery();
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

    // const handleCollapsedChange = () => {
    //     setCollapsed(!collapsed);
    // };
    // const handleImageChange = (checked) => {
    //     setImage(checked);
    // };
    // const handleToggleSidebar = (value) => {
    //     setToggled(value);
    // };

    return (
        <>
            {/* <div className={`app ${toggled ? 'toggled' : ''}`}>
                <Sidebar
                    image={image}
                    collapsed={collapsed}
                    toggled={toggled}
                    handleToggleSidebar={handleToggleSidebar}
                    handleCollapsedChange={handleCollapsedChange}
                />
                <main>
                    <div className="btn-toggle" onClick={() => handleToggleSidebar(true)}>
                        <FaBars />
                    </div> */}
                    <h1 className="">
                        Hello, {user}!
                    </h1>
                    <div>
                        <Card>
                            <CardBody>
                                <NavLogo tag="h5" color="#6C63FF">Your Cover Events</NavLogo>
                                <Table className="border table-striped no-wrap mt-3 align-middle" response border>
                                    <thead>
                                        <tr>
                                            <th>Edit</th>
                                            <th>Availability Start</th>
                                            <th>Availability End</th>
                                            <th>Team</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {
                                            eventData.map((cover) => {
                                                const url = new URL(cover.team_href)
                                                const splitPaths = url.pathname.split('/')
                                                const teamId = splitPaths[splitPaths.length - 1]
                                                let start = new DateObject(cover.availability_start)
                                                let end = new DateObject(cover.availability_end)
                                                let start_date = start.format("ddd DD MMM YYYY")
                                                let end_date = end.format("ddd DD MMM YYYY")
                                                const id = cover.id
                                                return (
                                                    <tr key={cover.id}>
                                                        <td>
                                                            <button className={styles.editBtn} onClick={() => setIsOpenUpdateCover(true)}>Edit</button>{isOpenUpdateCover && <UpdateCoverFormModal setIsOpenUpdateCover={setIsOpenUpdateCover} id={id} />}
                                                        </td>
                                                        <td>{start_date}</td>
                                                        <td>{end_date}</td>
                                                        <Link to="/team" state={{ id: teamId }}>{cover.team_name}</Link>
                                                    </tr>
                                                );
                                            })}
                                    </tbody>
                                </Table>
                                <button className={styles.primaryBtn} onClick={() => setIsOpenCover(true)}>Create Cover Event</button>{isOpenCover && <CoverEventFormModal setIsOpenCover={setIsOpenCover} />}
                                <NavLogo tag="h5" color="#6C63FF">Your Shift Swap Events</NavLogo>
                                <Table className="border table-striped no-wrap mt-3 align-middle" response border>
                                    <thead>
                                        <tr>
                                            <th>Edit</th>
                                            <th>Shift Start</th>
                                            <th>Shift End</th>
                                            <th>Availability Start</th>
                                            <th>Availability End</th>
                                            <th>Team</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {shiftData.map((shift) => {
                                            const url = new URL(shift.team_href)
                                            const splitPaths = url.pathname.split('/')
                                            const teamId = splitPaths[splitPaths.length - 1]
                                            let shift_s = new DateObject(shift.shift_start)
                                            let shift_start = shift_s.format("ddd DD MMM YYYY")
                                            let shift_e = new DateObject(shift.shift_end)
                                            let shift_end = shift_e.format("ddd DD MMM YYYY")
                                            let start = new DateObject(shift.availability_start)
                                            let end = new DateObject(shift.availability_end)
                                            let start_date = start.format("ddd DD MMM YYYY")
                                            let end_date = end.format("ddd DD MMM YYYY")
                                            const id = shift.id
                                            return (
                                                <tr key={shift.id}>
                                                    <td>
                                                        <button className={styles.editBtn} onClick={() => setIsOpenUpdateShift(true)}>Edit</button>{isOpenUpdateShift && <UpdateShiftFormModal setIsOpenUpdateShift={setIsOpenUpdateShift} id={id} />}
                                                    </td>
                                                    <td>{shift_start}</td>
                                                    <td>{shift_end}</td>
                                                    <td>{start_date}</td>
                                                    <td>{end_date}</td>
                                                    <Link to="/team" state={{ id: teamId }}>{shift.team_name}</Link>
                                                </tr>
                                            );
                                        })}
                                    </tbody>
                                </Table>
                                <button className={styles.primaryBtn} onClick={() => setIsOpenSwap(true)}>Create Swap Event</button>{isOpenSwap && <SwapEventFormModal setIsOpenSwap={setIsOpenSwap} />}
                            </CardBody>
                        </Card>
                    </div>
                {/* </main>
            </div> */}
        </>
    );
}

export default UserHome;
