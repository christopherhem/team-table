// Create Event Form Modal 
import React, { useState } from 'react'
import styles from "../events/Modal.module.css"
import { RiCloseLine } from "react-icons/ri"
import { useCreateRoleMutation } from '../../store/TeamsApi';
import { useGetUsersTeamsQuery } from '../../store/UsersApi';


export default function RoleFormModal({ setIsOpenRole }) {
  const [name, setName] = useState('');
  const [team, setTeam] = useState('');
  const [createRole, result] = useCreateRoleMutation();
  const { data, error, isLoading } = useGetUsersTeamsQuery([]);


  if (isLoading) {
    return (
      <progress className="progress is-primary" max="100"></progress>
    );
  }

  console.log("Data:", data)

  async function handleSubmit(e) {
    e.preventDefault();
    setIsOpenRole(false)
    createRole({ name, team });
    console.log(result)
  }

  return (
    <>
      <div className={styles.darkBG} onClick={() => setIsOpenRole(false)} />
      <div className={styles.centered}>
        <div className={styles.modal}>
          <div className={styles.modalHeader}>
            <h2 className={styles.heading}>Add Role</h2>
          </div>
          <button className={styles.closeBtn} onClick={() => setIsOpenRole(false)}>
            <RiCloseLine style={{ marginBottom: "-3px" }} />
          </button>
          <form className={styles.modalContent} onSubmit={(e) => handleSubmit(e)}>
            <h6>Enter role name</h6>
            <input type="text" id="name" value={shift_start} onChange={e => setName(e.target.value)} />
            <hr></hr>
            <h6>Enter Team</h6>
            <div className="mb-3">
              <select onChange={e => setTeam(e.target.value)} value={team_href} className="form-select" name="team_href" id="team_href">
                <option value="">Select a Team</option>
                {data.map((team) => {
                  return (
                    <option key={team.team_href} value={team.team_href}>{team.name}</option>
                  );
                })}
              </select>
              </div>
              <div className={styles.modalActions}>
                <div className={styles.actionsContainer}>
                  <button type="submit" className={styles.deleteBtn}>
                    Submit
                  </button>
                  <button type="button"
                    className={styles.cancelBtn}
                    onClick={() => setIsOpenRole(false)}
                  >
                    Cancel
                  </button>
                </div>
              </div>
          </form>
        </div>
      </div>
    </>
  );
};