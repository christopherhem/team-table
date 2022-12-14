import React, { useState } from 'react'
import styles from "./Modal.module.css"
import { RiCloseLine } from "react-icons/ri"
import { useUpdateCoverEventMutation } from '../../store/UsersApi';



export default function UpdateCoverFormModal({ handleClose, id }) {
  const [availability_start, setStart] = useState("");
  const [availability_end, setEnd] = useState("");
  const [updateCover, result] = useUpdateCoverEventMutation();

  async function handleSubmit(e) {
    e.preventDefault();
    updateCover({ id, availability_start, availability_end })
    handleClose();
  }

  return (
    <>
      <div className={styles.darkBG} onClick={() => handleClose()} />
      <div className={styles.centered}>
        <div className={styles.modal}>
          <div className={styles.modalHeader}>
            <h2 className={styles.heading}>Update your cover event</h2>
          </div>
          <button className={styles.closeBtn} onClick={() => handleClose()}>
            <RiCloseLine style={{ marginBottom: "-3px" }} />
          </button>
          <form className={styles.modalContent} onSubmit={(e) => handleSubmit(e)}>
            <h6>Enter Start Availability</h6>
            <input type="datetime-local" id="availability_start" value={availability_start} onChange={e => setStart(e.target.value)} />
            <hr></hr>
            <h6>Enter End Availability</h6>
            <input type="datetime-local" id="availability_end" value={availability_end} onChange={e => setEnd(e.target.value)} />
            <hr></hr>
            <div className={styles.modalActions}>
              <div className={styles.actionsContainer}>
                <button className={styles.deleteBtn}>
                  Submit
                </button>
                <button
                  className={styles.cancelBtn}
                  onClick={() => handleClose()}
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
