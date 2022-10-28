// Create Event Form Modal
import React, { useState } from 'react'
import { useLocation } from 'react-router-dom';
import styles from "../events/Modal.module.css"
import { RiCloseLine } from "react-icons/ri"
import { useCreateMemberMutation, useGetRolesQuery } from '../../store/TeamsApi';

export default function MemberFormModal({ setIsOpenMember }) {
  const [member_username, setMember] = useState('');
  const [role, setRole] = useState('');
  const location = useLocation()
  const { id } = location.state
  const [createMember, result] = useCreateMemberMutation();
  const { data, error, isLoading } = useGetRolesQuery(id)

  if (isLoading) {
    return (
      <progress className="progress is-primary" max="100"></progress>
    );
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setIsOpenMember(false);
    createMember({ member_username, role })
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
            <div className="mb-3">
              <h6>Enter Member's Username</h6>
              <input onChange={e => setMember(e.target.value)} value={member_username} type="text" name="member_username" id="member_username">
              </input>
              <h6>Enter Role</h6>
              <div className="mb-3">
                <select onChange={e => setRole(e.target.value)} value={role} className="form-select" name="role" id="role">
                  <option value="">Select a Role</option>
                  {data.map((roles) => {
                    return (
                      <option key={roles.id} value={roles.id}>{roles.name}</option>
                    );
                  })}
                </select>
              </div>
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
