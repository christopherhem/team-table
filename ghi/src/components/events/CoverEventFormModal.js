// Create Event Form Modal 
import React, {useState} from 'react'
import styles from "./Modal.module.css"
import { RiCloseLine } from "react-icons/ri"
import { useCreateCoverEventMutation } from '../../store/UsersApi';

import {
  Container,
  FormWrap,
  Icon,
  FormContent,
  Form,
  FormH1,
  FormButton,
  CreateInput
} from '../users/SignUpElements.js';


export default function CoverEventFormModal({ setIsOpen }) {
  const [availability_start, setStart] = useState('');
  const [availability_end, setEnd] = useState('');
  const [createCover, result] = useCreateCoverEventMutation();

  async function handleSubmit(e) {
      e.preventDefault();
      createCover({availability_start, availability_end});
  }

  return (
    <>
      <div className={styles.darkBG} onClick={() => setIsOpen(false)} />
      <div className={styles.centered}>
        <div className={styles.modal}>
          <div className={styles.modalHeader}>
            <h5 className={styles.heading}>Create a cover event</h5>
          </div>
          <button className={styles.closeBtn} onClick={() => setIsOpen(false)}>
            <RiCloseLine style={{ marginBottom: "-3px" }} />
          </button>
          <form className={styles.modalContent} onSubmit={(e) => handleSubmit(e)}>
          <h4>Enter Start Availability</h4>
          <input type="datetime-local" id="availability_start" value={availability_start} onChange={e=> setStart(e.target.value)} />
          <hr></hr>
          <h4>Enter End Availability</h4>
          <input type="datetime-local" id="availability_end" value={availability_end} onChange={e=> setEnd(e.target.value)} />
          </form>
          <div className={styles.modalActions}>
            <div className={styles.actionsContainer}>
              <button className={styles.deleteBtn} onClick={() => setIsOpen(false)}>
                Submit
              </button>
              <button
                className={styles.cancelBtn}
                onClick={() => setIsOpen(false)}
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


