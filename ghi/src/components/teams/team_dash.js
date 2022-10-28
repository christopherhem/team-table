import { useGetMembersQuery, useGetTeamQuery, useGetEventsQuery } from "../../store/TeamsApi"
import { Card, CardBody, Table } from "reactstrap";
import { useLocation } from "react-router-dom";
import { useState } from "react";
import DateObject from "react-date-object";
import TeamFormModal from "./TeamFormModal";
import RoleFormModal from "./RoleFormModal";
import MemberFormModal from "./MemberFormModal";
import styles from "../../components/dashboard/Home.module.css"
import { FlexContainer, TableLogo} from "../navbar/NavbarElements";

export function TeamDashboard() {
  const [isOpenTeam, setIsOpenTeam] = useState(false)
  const [isOpenRole, setIsOpenRole] = useState(false)
  const [isOpenMember, setIsOpenMember] = useState(false)
  const location = useLocation()
  const { id } = location.state
  const { data: eventData, isLoading: isLoadingEvents } = useGetEventsQuery(id)
  const { data: teamData, isLoading: isLoadingTeam } = useGetTeamQuery(id)
  const { data: membersData, isLoading: isLoadingMembers } = useGetMembersQuery(id)

  if (isLoadingTeam || isLoadingMembers || isLoadingEvents) {
    return (
      <progress className="progress is-primary" max="100"></progress>
    );
  }
  return (
    <div>
      <h1 className="">
        {teamData.name}
      </h1>
      <div>
        <Card>
          <CardBody className={styles.wrap}>
            <div className={styles.item1}>
              <FlexContainer>
                <button className={styles.primaryBtn} onClick={() => setIsOpenTeam(true)}>Create Team</button>{isOpenTeam && <TeamFormModal setIsOpenTeam={setIsOpenTeam} />}
                <button className={styles.primaryBtn} onClick={() => setIsOpenMember(true)}>Create Member</button>{isOpenMember && <MemberFormModal setIsOpenMember={setIsOpenMember} id={id} />}
                <button className={styles.primaryBtn} onClick={() => setIsOpenRole(true)}>Create Role</button>{isOpenRole && <RoleFormModal setIsOpenRole={setIsOpenRole} />}
              </FlexContainer>

              <div className={styles.item2}>
                <TableLogo tag="h5" color="#6C63FF">Members</TableLogo>
                <Table className="border table-striped no-wrap mt-3 align-middle col-6" response border>
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
              </div>
              <TableLogo tag="h5" color="#6C63FF">Cover Events</TableLogo>
              <Table className="border table-striped no-wrap mt-3 align-middle col-6" response border>
                <thead>
                  <tr>
                    <th>Owner</th>
                    <th>Availability Start</th>
                    <th>Availability End</th>
                  </tr>
                </thead>
                <tbody>
                  {
                    (eventData.cover_events.length >= 1) ?
                      eventData.cover_events.map((cover) => {
                        let start = new DateObject(cover.availability_start)
                        let end = new DateObject(cover.availability_end)
                        let start_date = start.format("ddd DD MMM YYYY")
                        let end_date = end.format("ddd DD MMM YYYY")
                        return (
                          <tr key={cover.id}>
                            <td>{cover.owner}</td>
                            <td>{start_date}</td>
                            <td>{end_date}</td>
                          </tr>
                        )
                      })
                      : null
                  }
                </tbody>
              </Table>
              <TableLogo tag="h5" color="#6C63FF">Shift Swap Events</TableLogo>
              <Table className="border table-striped no-wrap mt-3 align-middle col-6" response border>
                <thead>
                  <tr>
                    <th>Owner</th>
                    <th>Shift Start</th>
                    <th>Shift End</th>
                    <th>Availability Start</th>
                    <th>Availability End</th>
                  </tr>
                </thead>
                <tbody>
                  {(eventData.swap_events.length >= 1) ?
                    eventData.swap_events.map((swap) => {
                      let shift_s = new DateObject(swap.shift_start)
                      let shift_start = shift_s.format("ddd DD MMM YYYY")
                      let shift_e = new DateObject(swap.shift_end)
                      let shift_end = shift_e.format("ddd DD MMM YYYY")
                      let start = new DateObject(swap.availability_start)
                      let end = new DateObject(swap.availability_end)
                      let start_date = start.format("ddd DD MMM YYYY")
                      let end_date = end.format("ddd DD MMM YYYY")
                      return (
                        <tr key={swap.id}>
                          <td>{swap.owner}</td>
                          <td>{shift_start}</td>
                          <td>{shift_end}</td>
                          <td>{start_date}</td>
                          <td>{end_date}</td>
                        </tr>
                      )
                    }) : null

                  }
                </tbody>
              </Table>
            </div>
          </CardBody>
        </Card>
      </div>
    </div>

  )
}
