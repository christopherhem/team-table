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
import { useGetTokenQuery, useGetUserCoverEventsQuery, useGetUserShiftSwapEventsQuery, useDeleteCoverEventMutation, useDeleteShiftSwapEventMutation } from '../store/UsersApi';
import UpdateShiftFormModal from '../components/events/updateSwapModal';
import { FaBars, FaTrash } from 'react-icons/fa';
import Swap from '../components/swaps/ShiftSwapModal';
import { useGetValidSwapsQuery } from '../store/TeamsApi';
import { usePerformSwapMutation } from '../store/UsersApi';

import './styles.scss';

function UserHome() {
    const [isOpenSwap, setIsOpenSwap] = useState(false);
    const [isOpenUpdateShift, setIsOpenUpdateShift] = useState(false);
    const [isOpenUpdateCover, setIsOpenUpdateCover] = useState(false);
    const [isOpenCover, setIsOpenCover] = useState(false);
    const [isOpenShift, setIsOpenShift] = useState(false);
    const [isOpen, setIsOpen] = useState(false);
    const [collapsed, setCollapsed] = useState(false);
    const [image, setImage] = useState(false);
    const [toggled, setToggled] = useState(false);
    const [deleteCover, coverResult] = useDeleteCoverEventMutation();
    const [deleteShift, shiftResult] = useDeleteShiftSwapEventMutation();
    const { data: userData, isLoading: isLoadingUser } = useGetTokenQuery();
    const { data: eventData, isLoading: isLoadingEvent } = useGetUserCoverEventsQuery();
    console.log("Event:", eventData)
    const { data: shiftData, isLoading: isLoadingShift } = useGetUserShiftSwapEventsQuery();
    const {data: swapData, isLoading: isLoadingSwaps} = useGetValidSwapsQuery();


    if (isLoadingEvent || isLoadingShift || isLoadingUser || isLoadingSwaps) {
        return (
            <progress className="progress is-primary" max="100"></progress>
        );
    }
    console.log(swapData)
    const user = userData.user.first_name
    const toggle = () => {
        setIsOpen(!isOpen)
    }
    return (
        <>
            <h1 className="">
                Hello, {user}!
            </h1>
            <div>
                <Card>
                {/* <button className={styles.primaryBtn} onClick={() => setIsOpenSwap(true)}>Swap Shifts</button>{isOpenSwap && <Swap setIsOpenSwap={setIsOpenSwap} />} */}
                    <CardBody>
                        <Table className="border table-striped no-wrap mt-3 align-middle" response border>
                            <thead>
                                <tr>
                                {
                                    swapData.swaps.map((shift) =>{
                                        return (
                                                <th key={shift.user_event.mono_id}>
                                                    {new DateObject(shift.user_event.shift_start).format("ddd DD MMM YYYY")}
                                                </th>
                                        )
                                    })
                                }
                                </tr>
                            </thead>
                            <tbody>
                                {
                                    swapData.swaps.map((shift) => {
                                        return (
                                            shift.valid_swaps.map((swap) =>{
                                                console.log("ID", swap)
                                                return (
                                                    <tr key={swap.mono_id}>
                                                        <td>{swap.owner}</td>
                                                        <td>{swap.owner}</td>
                                                    </tr>
                                            )
                                                }
                                            )
                                        )})
                                }
                            </tbody>
                        </Table>
                        <NavLogo tag="h5" color="#6C63FF">Your Cover Events</NavLogo>
                        <Table className="border table-striped no-wrap mt-3 align-middle" response border>
                            <thead>
                                <tr>
                                    <th>Edit</th>
                                    <th>Delete</th>
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
                                                <td><button className={styles.deleteBtn} onClick={() => deleteCover(id)}><FaTrash /></button></td>
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
                                    <th>Delete</th>
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
                                            <td><button className={styles.deleteBtn} onClick={() => deleteShift(id)}><FaTrash /></button></td>
                                            <td>{shift_start}</td>
                                            <td>{shift_end}</td>
                                            <td>{start_date}</td>
                                            <td>{end_date}</td>
                                            <td><Link to="/team" state={{ id: teamId }}>{shift.team_name}</Link></td>

                                        </tr>
                                    );
                                })}
                            </tbody>
                        </Table>
                        <button className={styles.primaryBtn} onClick={() => setIsOpenShift(true)}>Create Swap Event</button>{isOpenShift && <SwapEventFormModal setIsOpenShift={setIsOpenShift} />}
                    </CardBody>
                </Card>
            </div>

        </>
    );
}

export default UserHome;
