// Create Event Form Modal 
import React, { useState } from 'react'
import styles from "../events/Modal.module.css"
import { RiCloseLine } from "react-icons/ri"
import { useCreateTeamMutation } from '../../store/TeamsApi';

export default function TeamFormModal({ setIsOpenTeam }) {
  const [name, setTeamName] = useState('');
  const [type, setTeamType] = useState('');
  const [description, setDescription] = useState('');
  const [createTeam, result] = useCreateTeamMutation();

  async function handleSubmit(e) {
    e.preventDefault();
    setIsOpenTeam(false);
    createTeam({ name, type, description });
    console.log("RESULT:", result)
  }

  return (
    <>
      <div className={styles.darkBG} onClick={() => setIsOpenTeam(false)} />
      <div className={styles.centered}>
        <div className={styles.modal}>
          <div className={styles.modalHeader}>
            <h2 className={styles.heading}>Add Team</h2>
          </div>
          <button className={styles.closeBtn} onClick={() => setIsOpenTeam(false)}>
            <RiCloseLine style={{ marginBottom: "-3px" }} />
          </button>
          <form className={styles.modalContent} onSubmit={(e) => handleSubmit(e)}>
            <div className="mb-3">
              <h6>Enter team name</h6>
              <input onChange={e => setTeamName(e.target.value)} value={name} type="text" name="name" id="name">
              </input>
              <h6>Enter description</h6>
              <textarea onChange={e => setDescription(e.target.value)} value={description} type="text" name="description" id="description">
              </textarea>
            </div>
            <div className={styles.modalActions}>
              <div className={styles.actionsContainer}>
                <button className={styles.deleteBtn}>
                  Submit
                </button>
                <button
                  className={styles.cancelBtn}
                  onClick={() => setIsOpenTeam(false)}
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
