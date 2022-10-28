import React, { useState } from 'react'
import styles from "./Modal.module.css"
import { RiCloseLine } from "react-icons/ri"
import { useUpdateShiftSwapEventMutation } from '../../store/UsersApi';


export default function UpdateShiftFormModal({ handleClose, id }) {
  const [shift_start, setShiftStart] = useState('');
  const [shift_end, setShiftEnd] = useState('');
  const [availability_start, setAvailStart] = useState('');
  const [availability_end, setAvailEnd] = useState('');
  const [updateShift, result] = useUpdateShiftSwapEventMutation();


  async function handleSubmit(e) {
    e.preventDefault();
    updateShift({ id, shift_start, shift_end, availability_start, availability_end });
    handleClose();
  }

  return (
    <>
      <div className={styles.darkBG} onClick={() => handleClose()} />
      <div className={styles.centered}>
        <div className={styles.modal}>
          <div className={styles.modalHeader}>
            <h2 className={styles.heading}>Update your swap event</h2>
          </div>
          <button className={styles.closeBtn} onClick={() => handleClose()}>
            <RiCloseLine style={{ marginBottom: "-3px" }} />
          </button>
          <form className={styles.modalContent} onSubmit={(e) => handleSubmit(e)}>
            <h6>Enter Shift Start</h6>
            <input type="datetime-local" id="shift_start" value={shift_start} onChange={e => setShiftStart(e.target.value)} />
            <h6>Enter Shift End</h6>
            <input type="datetime-local" id="shift_end" value={shift_end} onChange={e => setShiftEnd(e.target.value)} />
            <hr></hr>
            <h6>Enter Start Availability</h6>
            <input type="datetime-local" id="availability_start" value={availability_start} onChange={e => setAvailStart(e.target.value)} />
            <h6>Enter End Availability</h6>
            <input type="datetime-local" id="availability_end" value={availability_end} onChange={e => setAvailEnd(e.target.value)} />
            <hr></hr>
            <div className={styles.modalActions}>
              <div className={styles.actionsContainer}>
                <button type="submit" className={styles.deleteBtn}>
                  Submit
                </button>
                <button type="button"
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
