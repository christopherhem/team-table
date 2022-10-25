import { useGetMembersQuery, useGetTeamQuery } from "../../store/TeamsApi"
import { Card, CardBody, CardTitle, CardSubtitle, Table } from "reactstrap";
import { NavLogo } from '../navbar/NavbarElements';
import { useGetTokenQuery } from "../../store/UsersApi";
import { useLocation } from "react-router-dom";



export function TeamDashboard() {
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
        <>

        {/* <SideNavbar /> */}
        {/* <NavBar toggle={toggle} /> */}
        <h1 className="">
            {"hello"}
        </h1>
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
                <tbody>
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
                </tbody>
               </Table>
            </CardBody>
          </Card>
        </div>
        </>
    )
}
