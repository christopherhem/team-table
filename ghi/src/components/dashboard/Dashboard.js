import React from 'react'
import DateObject from "react-date-object";
import { useEffect, useState } from 'react';
import { Card, CardBody, CardTitle, CardSubtitle, Table } from "reactstrap";
// import ErrorNotification from '../../ErrorNotification'
// import { Link } from 'react-router-dom';
import { useGetUserCoverEventsQuery, useGetUserShiftSwapEventsQuery } from '../../store/UsersApi';



function Dashboard() {
    const { data: eventData } = useGetUserCoverEventsQuery();
    const { data: shiftData } = useGetUserShiftSwapEventsQuery();
    console.log(shiftData)
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
              <Table className="table-sm no-wrap mt-3 align-middle" response borderless>
                <thead>
                  <tr>
                    <th>Availability Start</th>
                    <th>Availability End</th>
                    <th>Team</th>
                  </tr>
                </thead>
                <tbody>
                  {eventData.map((event) => {
                    let start = new DateObject(event.availability_start)
                    let end = new DateObject(event.availability_end)
                    let start_date = start.format("ddd DD MMM YYYY, hh:mm a")
                    let end_date = end.format("ddd DD MMM YYYY, hh:mm a")
                    return (
                    <tr key={event.id}>
                    <td>{start_date}</td>
                    <td>{end_date}</td>
                    </tr>
                  );
                  })}
                </tbody>
              </Table>
              <Table className=" table-sm no-wrap mt-3 align-middle" response borderless>
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
                    {/* {shiftData.map((event) => {
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
                      </tr>
                    );
                    })} */}
                  </tbody>
                  </Table>
            </CardBody>
          </Card>
        </div>
    </>
  )
}

export default Dashboard;
