import React from 'react';
import { useEffect, useState } from 'react';
import { useGetUsersTeamsQuery } from '../../store/UsersApi';


export function TeamsList() {
    const {data: teamsData, isLoading: isLoadingTeams} = useGetUsersTeamsQuery()

    if (isLoadingTeams) {
        return (
            <progress className="progress is-primary" max="100"></progress>
            );
    }
    console.log(teamsData)

    return (
        <div>
            <h5 color="#6C63FF" >Your Teams</h5>
            <table className="smtable">
                <thead>
                    <tr>
                        <th>Team Name</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        teamsData.map((team) => {
                            return (
                            <tr key={team.team_href}>
                                <td>{team.name}</td>
                            </tr>
                            )
                        })}
                </tbody>
            </table>
        </div>
    )
}
