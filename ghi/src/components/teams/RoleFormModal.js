// Create Role Form Modal 
import React, { useState } from 'react'
import { useLocation } from 'react-router-dom';
import styles from "../events/Modal.module.css"
import { RiCloseLine } from "react-icons/ri"
import { useCreateRoleMutation } from '../../store/TeamsApi';

export default function RoleFormModal({ setIsOpenRole }) {
  const [name, setName] = useState('');
  const location = useLocation()
  const { id } = location.state
  const [invite, setInvite] = useState(false);
  const [approve, setApprove] = useState(false);
  const [createRole, result] = useCreateRoleMutation();

  async function handleSubmit(e) {
    e.preventDefault();
    setIsOpenRole(false)
    const team = parseInt(id)
    const can_invite = Boolean(invite)
    const can_approve = Boolean(approve)

    // let data = {}
    // data['"name"'] = name
    // data['"team"'] = team
    // data['"can_invite"'] = Boolean(can_invite)
    // data['"can_approve"'] = Boolean(can_approve) 
    // console.log(data)
    // console.log(team)
    createRole({name, team, can_invite, can_approve});
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
            <input type="text" id="name" value={name} onChange={e => setName(e.target.value)} />
            <hr></hr>
            <div className="checkbox-wrapper">
            <h6>Privileges</h6>
              <label> Can Invite</label>
                <input onChange={e => setInvite(e.target.value)} value={true} type="checkbox" checked={invite} />
              <br></br>
              <label> Can Approve</label>
                <input onChange={e => setApprove(e.target.value)} value={true} type="checkbox" checked={approve} />
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