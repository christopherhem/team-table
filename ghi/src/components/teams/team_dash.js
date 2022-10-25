import { useGetMembersQuery, useGetTeamQuery } from "../../store/TeamsApi"
import { Card, CardBody, CardTitle, CardSubtitle, Table } from "reactstrap";
import { NavLogo } from '../navbar/NavbarElements';
import { useGetTokenQuery } from "../../store/UsersApi";
import { useLocation } from "react-router-dom";

import TeamFormModal from "./TeamFormModal";

import styles from "../../components/dashboard/Home.module.css"

export function TeamDashboard( setisOpenTeam ) {
    // const location = useLocation()
    // const { id } = location.state
    // const {data: teamData, isLoading: isLoadingTeam} = useGetTeamQuery(id)
    // const {data: membersData, isLoading: isLoadingMembers} = useGetMembersQuery(id)

    // if (isLoadingTeam || isLoadingMembers ) {
    //     return (
    //         <progress className="progress is-primary" max="100"></progress>
    //         );
    // }
    // console.log(membersData)
    return (
        <>
        <h1>Team Page...</h1>
        {/* <SideNavbar /> */}
        {/* <NavBar toggle={toggle} /> */}
        {/* <h1 className="">
            {"Team Page"}
        </h1>
        <div>
        <button className={styles.primaryBtn} onClick={() => setIsOpenTeam(true)}>Create Team</button>{isOpenTeam && <TeamFormModal setIsOpenTeam={setIsOpenTeam} />}
        </div>
        <div>
          <Card>
            <CardBody>
              <NavLogo tag="h5" color="#6C63FF">Members</NavLogo>
              <Table className="border table-striped no-wrap mt-3 align-middle" response border>
                <thead>
                  <tr>
                    <th>Name</th>
                  </tr>
                </thead>
                <tbody> */}
                  {/* {
                  membersData.map((event) => {
                    return (
                    <tr key={event.id}>
                    <td>{start_date}</td>
                    <td>{end_date}</td>
                    <td>{event.team_name}</td>
                    </tr>
                  );
                  })} */}
                {/* </tbody>
               </Table>
            </CardBody>
          </Card>
        </div> */}
        </>
    )
}
