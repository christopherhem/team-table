import { useState } from "react";
import { useGetMembersQuery, useGetTeamQuery } from "../../store/TeamsApi"
import { Card, CardBody, CardTitle, CardSubtitle, Table } from "reactstrap";
import { NavLogo } from '../navbar/NavbarElements';
import { useLocation } from "react-router-dom";
<<<<<<< HEAD
import { useState } from "react";
=======
import UpdateShiftFormModal from "../events/updateSwapModal";
>>>>>>> main

import TeamFormModal from "./TeamFormModal";

import styles from "../../components/dashboard/Home.module.css"

<<<<<<< HEAD
export function TeamDashboard( setisOpenTeam ) {
=======
export function TeamDashboard() {
>>>>>>> main
    const [isOpenTeam, setIsOpenTeam] = useState(false)
    const location = useLocation()
    const { id } = location.state
    const {data: teamData, isLoading: isLoadingTeam} = useGetTeamQuery(id)
    const {data: membersData, isLoading: isLoadingMembers} = useGetMembersQuery(id)

    if (isLoadingTeam || isLoadingMembers ) {
        return (
            <progress className="progress is-primary" max="100"></progress>
            );
    }
    console.log(membersData)
    return (
        <div className="grid-container">
        <h1 className="">
            {teamData.name}
        </h1>
        <div>
        <button className={styles.primaryBtn} onClick={() => setIsOpenTeam(true)}>Create Team</button>{isOpenTeam && <TeamFormModal setIsOpenTeam={setIsOpenTeam} />}
        </div>
        <div>
          <Card>
            <CardBody className="col-6">
              <NavLogo tag="h5" color="#6C63FF">Members ({membersData.length})</NavLogo>
              <Table className="border table-striped no-wrap mt-3 align-middle " response border>
                <thead>
                  <tr>
                    <th>Name</th>
                  </tr>
                </thead>
                <tbody>
                  {
                  membersData.map((member) => {
                    return (
                    <tr key={member.id}>
                    <td>{member.member_username}</td>
                    </tr>
                  );
                  })}
                </tbody>
               </Table>
            </CardBody>
          </Card>
          <Card>
            <CardBody className="col-6">
            <Table className="border table-striped no-wrap mt-3 align-middle " response border>
                <thead>
                  <tr>
                    <th>Team Notifications</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td> some notification</td>
                  </tr>
                </tbody>
               </Table>
            </CardBody>
          </Card>
        </div>
        </div>
    )
}
