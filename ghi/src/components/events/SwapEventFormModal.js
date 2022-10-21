// Create Event Form Modal 
import React, { useState } from 'react'
import styles from "./Modal.module.css"
import { RiCloseLine } from "react-icons/ri"
import { useCreateShiftSwapEventMutation, useGetUsersTeamsQuery } from '../../store/UsersApi';


export default function SwapEventFormModal({ setIsOpenSwap }) {
  const [shift_start, setShiftStart] = useState('');
  const [shift_end, setShiftEnd] = useState('');
  const [availability_start, setAvailStart] = useState('');
  const [availability_end, setAvailEnd] = useState('');
  const [team_href, setTeam] = useState('');
  const [createShift, result] = useCreateShiftSwapEventMutation();
  const { data, error, isLoading } = useGetUsersTeamsQuery([]);


  if (isLoading) {
    return (
      <progress className="progress is-primary" max="100"></progress>
    );
  }


  console.log("Data:", data)

  async function handleSubmit(e) {
    e.preventDefault();
    setIsOpenSwap(false)
    createShift({ shift_start, shift_end, availability_start, availability_end, team_href });
    console.log(result)
  }

  return (
    <>
      <div className={styles.darkBG} onClick={() => setIsOpenSwap(false)} />
      <div className={styles.centered}>
        <div className={styles.modal}>
          <div className={styles.modalHeader}>
            <h2 className={styles.heading}>Create a swap event</h2>
          </div>
          <button className={styles.closeBtn} onClick={() => setIsOpenSwap(false)}>
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
                    onClick={() => setIsOpenSwap(false)}
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


