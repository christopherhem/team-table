import React from 'react'
import { Link } from 'react-router-dom';
import DateObject from "react-date-object";
import { useState } from 'react';
import { Card, CardBody, Table } from "reactstrap";
import { TableLogo } from '../components/navbar/NavbarElements';
import CoverEventFormModal from '../components/events/CoverEventFormModal';
import SwapEventFormModal from '../components/events/SwapEventFormModal';
import UpdateCoverFormModal from '../components/events/updateCoverModal';
import styles from "../components/dashboard/Home.module.css"
import {
    useGetTokenQuery,
    useGetUserCoverEventsQuery,
    useGetUserShiftSwapEventsQuery,
    useDeleteCoverEventMutation,
    useDeleteShiftSwapEventMutation,
    useGetUserNotificationsQuery,
    useUpdateNotificationMutation,
} from '../store/UsersApi';
import UpdateShiftFormModal from '../components/events/updateSwapModal';
import { FaTrash, FaCheck } from 'react-icons/fa';
import Swap from '../components/swaps/ShiftSwapModal';
import CoverSwap from '../components/swaps/CoverSwapModal';
import './styles.scss';

function UserHome() {
    const [coverId, setCoverId] = useState(null);
    const [shiftId, setShiftId] = useState(null);
    const [isOpenCoverSwap, setIsOpenCoverSwap] = useState(false);
    const [isOpenSwap, setIsOpenSwap] = useState(false);
    const [isOpenUpdateShift, setIsOpenUpdateShift] = useState(false);
    const [isOpenUpdateCover, setIsOpenUpdateCover] = useState(false);
    const [isOpenCover, setIsOpenCover] = useState(false);
    const [isOpenShift, setIsOpenShift] = useState(false);
    const [updateNotification] = useUpdateNotificationMutation();
    const [deleteCover] = useDeleteCoverEventMutation();
    const [deleteShift] = useDeleteShiftSwapEventMutation();
    const { data: userData, isLoading: isLoadingUser } = useGetTokenQuery();
    const { data: eventData, isLoading: isLoadingEvent } = useGetUserCoverEventsQuery();
    const { data: shiftData, isLoading: isLoadingShift } = useGetUserShiftSwapEventsQuery();
    const { data: notificationData, isLoading: isLoadingNotifications } = useGetUserNotificationsQuery();


    if (isLoadingEvent || isLoadingShift || isLoadingUser || isLoadingNotifications) {
        return (
            <progress className="progress is-primary" max="100"></progress>
        );
    }

    const unseenNotifications = notificationData.filter((notification) => notification.seen === false)
    const user = userData.user.first_name

    return (
        <>
            <h1>Hello, {user}!</h1>
            <div>
                <Card>
                    <CardBody>
                        <TableLogo tag="h5" color="#6C63FF">Notifications</TableLogo>
                        <Table className="border table-striped no-wrap mt-3 align-middle col-6" response border>
                            <thead>
                                <tr>
                                    <th>Your Notifications</th>
                                </tr>
                            </thead>
                            <tbody>
                                {
                                    unseenNotifications.map((item) => {
                                        return (
                                            <tr key={item.id}>
                                                <td>{item.message}</td>
                                                <td><button className={styles.seenBtn} onClick={() => updateNotification(item.id)}><FaCheck /></button></td>
                                            </tr>
                                        )})
                                }
                            </tbody>
                        </Table>
                        <TableLogo tag="h5" color="#6C63FF">Your Cover Events</TableLogo>
                        <Table className="border table-striped no-wrap mt-3 align-middle" response border>
                            <thead>
                                <tr>
                                    <th>Swap</th>
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
                                        const teamId = splitPaths[splitPaths.length -1]
                                        let start = new DateObject(cover.availability_start)
                                        let end = new DateObject(cover.availability_end)
                                        let start_date = start.format("ddd DD MMM YYYY")
                                        let end_date = end.format("ddd DD MMM YYYY")

                                        return (
                                            <tr key={cover.id}>
                                                <td>
                                                    <button className={styles.primaryBtn} onClick={() => {
                                                        setCoverId(cover.id)
                                                        setIsOpenCoverSwap(true)
                                                    }}>Cover a Shift</button>{isOpenCoverSwap && coverId ? <CoverSwap i={coverId} handleClose={() => {
                                                        setIsOpenCoverSwap(false)
                                                        setCoverId(null)
                                                    }} /> : null}
                                                </td>
                                                <td>
                                                    <button className={styles.editBtn} onClick={() => {
                                                        setCoverId(cover.id)
                                                        setIsOpenUpdateCover(true)
                                                    }}>Edit</button>{isOpenUpdateCover && coverId ? <UpdateCoverFormModal id={coverId} handleClose={() => {
                                                        setIsOpenUpdateCover(false)
                                                        setCoverId(null)
                                                    }} /> : null}
                                                </td>
                                                <td><button className={styles.deleteBtn} onClick={() => deleteCover(coverId)}><FaTrash /></button></td>
                                                <td>{start_date}</td>
                                                <td>{end_date}</td>
                                                <Link to="/team" state={{ id: teamId }}>{cover.team_name}</Link>
                                            </tr>
                                        );
                                    })}
                            </tbody>
                        </Table>
                        <button className={styles.secPrimaryBtn} onClick={() => setIsOpenCover(true)}>Create Cover Event</button>{isOpenCover && <CoverEventFormModal setIsOpenCover={setIsOpenCover} />}
                        <TableLogo tag="h5" color="#6C63FF">Your Shift Swap Events</TableLogo>
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
                                                }}>Swap Shifts</button>{isOpenSwap && shiftId ? <Swap i={shiftId} handleClose={() => {
                                                    setIsOpenSwap(false)
                                                    setShiftId(null)
                                                }} /> : null}
                                            </td>
                                            <td>
                                                <button className={styles.editBtn} onClick={() => {
                                                    setShiftId(shift.id)
                                                    setIsOpenUpdateShift(true)
                                                }}>Edit</button>{isOpenUpdateShift && shiftId ? <UpdateShiftFormModal id={shiftId} handleClose={() => {
                                                    setIsOpenUpdateShift(false)
                                                    setShiftId(null)
                                                }} /> : null}
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
                        <button className={styles.secPrimaryBtn} onClick={() => setIsOpenShift(true)}>Create Swap Event</button>{isOpenShift && <SwapEventFormModal setIsOpenShift={setIsOpenShift} />}
                    </CardBody>
                </Card>
            </div>
        </>
    );
}

export default UserHome;
