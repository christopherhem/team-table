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
import { useGetTokenQuery,
    useGetUserCoverEventsQuery,
    useGetUserShiftSwapEventsQuery,
    useDeleteCoverEventMutation,
    useDeleteShiftSwapEventMutation,
    useGetUserNotificationsQuery,
    useUpdateNotificationMutation,
} from '../store/UsersApi';
import UpdateShiftFormModal from '../components/events/updateSwapModal';
import { FaBars, FaTrash, FaCheck } from 'react-icons/fa';
import Swap from '../components/swaps/ShiftSwapModal';


import './styles.scss';

function UserHome() {
    const [shiftId, setShiftId] = useState(null);
    const [isOpenSwap, setIsOpenSwap] = useState(false);
    const [isOpenUpdateShift, setIsOpenUpdateShift] = useState(false);
    const [isOpenUpdateCover, setIsOpenUpdateCover] = useState(false);
    const [isOpenCover, setIsOpenCover] = useState(false);
    const [isOpenShift, setIsOpenShift] = useState(false);
    const [seenNote, setSeenNote] = useState(false)
    const [updateNotification, setupdateNotification] = useUpdateNotificationMutation();
    const [isOpen, setIsOpen] = useState(false);
    const [deleteCover, coverResult] = useDeleteCoverEventMutation();
    const [deleteShift, shiftResult] = useDeleteShiftSwapEventMutation();
    const { data: userData, isLoading: isLoadingUser } = useGetTokenQuery();
    const { data: eventData, isLoading: isLoadingEvent } = useGetUserCoverEventsQuery();
    const { data: shiftData, isLoading: isLoadingShift } = useGetUserShiftSwapEventsQuery();
    const { data: notificationData, isLoading: isLoadingNotifications} = useGetUserNotificationsQuery();


    if (isLoadingEvent || isLoadingShift || isLoadingUser || isLoadingNotifications) {
        return (
            <progress className="progress is-primary" max="100"></progress>
        );
    }

    const unseenNotifications = notificationData.filter((notification) => notification.seen === false)
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

                    <CardBody>
                        <NavLogo tag="h5" color="#6C63FF">Notifications</NavLogo>
                        <Table className="border table-striped no-wrap mt-3 align-middle col-6" response border>
                        <thead>
                            <tr>
                            <th>Your Notifications</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                                unseenNotifications.map((item) => {
                                    if (item.seen === false) {
                                    return (
                                    <tr key={item.id}>
                                        <td>{item.message}</td>
                                        <td><button className={styles.seenBtn} onClick={() => setSeenNote(true)}><FaCheck /></button></td>
                                    </tr>
                                )}})
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
                                    <th>Swap</th>
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

                                    return (
                                        <tr key={shift.id}>
                                            <td>
                                                <button className={styles.primaryBtn} onClick={() => {
                                                    setShiftId(shift.id)
                                                    setIsOpenSwap(true)
                                                } }>Swap Shifts</button>{isOpenSwap && shiftId ? <Swap i={shiftId} handleClose={() => {
                                                    setIsOpenSwap(false)
                                                    setShiftId(null)
                                                   }} />: null}
                                            </td>
                                            <td>
                                                <button className={styles.editBtn} onClick={() => {
                                                    setShiftId(shift.id)
                                                    setIsOpenUpdateShift(true)
                                                    }}>Edit</button>{isOpenUpdateShift && shiftId ? <UpdateShiftFormModal setIsOpenUpdateShift={setIsOpenUpdateShift} i={shiftId} />: null}
                                            </td>
                                            <td><button className={styles.deleteBtn} onClick={() => deleteShift(shift.id)}><FaTrash /></button></td>
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
