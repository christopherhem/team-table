// Create Event Form Modal 
import React from 'react'
import styles from "./Modal.module.css"
import { RiCloseLine } from "react-icons/ri"

export default function SwapEventFormModal({ setIsOpenSwap }) {
  return (
    <>
      <div className={styles.darkBG} onClick={() => setIsOpenSwap(false)} />
      <div className={styles.centered}>
        <div className={styles.modal}>
          <div className={styles.modalHeader}>
            <h5 className={styles.heading}>Create a swap event</h5>
          </div>
          <button className={styles.closeBtn} onClick={() => setIsOpenSwap(false)}>
            <RiCloseLine style={{ marginBottom: "-3px" }} />
          </button>
          <div className={styles.modalContent}>
            Please enter SWAPPPP event information.
          </div>
          <div className={styles.modalActions}>
            <div className={styles.actionsContainer}>
              <button className={styles.deleteBtn} onClick={() => setIsOpenSwap(false)}>
                Submit
              </button>
              <button
                className={styles.cancelBtn}
                onClick={() => setIsOpenSwap(false)}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};


