import { useGetMembersQuery, useGetTeamQuery } from "../../store/TeamsApi"
import { Card, CardBody, CardTitle, CardSubtitle, Table } from "reactstrap";
import { NavLogo } from '../navbar/NavbarElements';
import { useGetTokenQuery } from "../../store/UsersApi";



export function TeamDashboard(id) {
    const {data: userData, isLoading: isLoadingUser} = useGetTokenQuery();
    const {data: teamData, isLoading: isLoadingTeam} = (id) = useGetTeamQuery()
    // const {data: membersData, isLoading: isLoadingMembers} = useGetMembersQuery()

    if (isLoadingUser ) {
        return (
            <progress className="progress is-primary" max="100"></progress>
            );
    }
    // const team = teamData.name
    console.log(teamData)
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
                    <th>Availability Start</th>
                    <th>Availability End</th>
                    <th>Team</th>
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
