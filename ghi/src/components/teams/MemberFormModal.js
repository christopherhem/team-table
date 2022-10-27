// Create Event Form Modal 
import React, { useState } from 'react'
import styles from "../events/Modal.module.css"
import { RiCloseLine } from "react-icons/ri"
import { useCreateMemberMutation } from '../../store/TeamsApi';
import { useGetRolesQuery } from '../../store/TeamsApi';



export default function MemberFormModal({ setIsOpenMember }) {
  const [member_username, setMember] = useState('');
  const [role, setRole] = useState('');
  const [createMember, result] = useCreateMemberMutation();
  const { data, error, isLoading } = useGetRolesQuery([]);


  if (isLoading) {
    return (
      <progress className="progress is-primary" max="100"></progress>
    );
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setIsOpenMember(false);
    createMember({ member_username, role });
    console.log(result)
  }

  return (
    <>
      <div className={styles.darkBG} onClick={() => setIsOpenMember(false)} />
      <div className={styles.centered}>
        <div className={styles.modal}>
          <div className={styles.modalHeader}>
            <h2 className={styles.heading}>Add Member</h2>
          </div>
          <button className={styles.closeBtn} onClick={() => setIsOpenMember(false)}>
            <RiCloseLine style={{ marginBottom: "-3px" }} />
          </button>
          <form className={styles.modalContent} onSubmit={(e) => handleSubmit(e)}>
            <h6>Select a member</h6>
            <div className="mb-3">
              {/* <select onChange={e => setMember(e.target.value)} value={team_href} className="form-select" name="member_username" id="member_username">
                <option value="">Select a member</option>
                {data.map((member) => {
                  return (
                    <option key={member.member_username} value={member.member_username}>{member.member_username}</option>
                  );
                })}
              </select> */}
              {/* <select onChange={e => setRole(e.target.value)} value={team_href} className="form-select" name="role" id="role">
                <option value="">Select a role</option>
                {data.map((role) => {
                  return (
                    <option key={role.name} value={role.name}>{role.name}</option>
                  );
                })}
              </select> */}
            </div>

            <div className={styles.modalActions}>
              <div className={styles.actionsContainer}>
                <button className={styles.deleteBtn}>
                  Submit
                </button>
                <button
                  className={styles.cancelBtn}
                  onClick={() => setIsOpenMember(false)}
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


