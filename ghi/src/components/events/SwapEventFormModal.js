// Create Event Form Modal 
import React, {useState} from 'react'
import styles from "./Modal.module.css"
import { RiCloseLine } from "react-icons/ri"
import { useCreateShiftSwapEventMutation } from '../../store/UsersApi';

export default function SwapEventFormModal({ setIsOpenSwap }) {
  const [shift_start, setShiftStart] = useState('');
  const [shift_end, setShiftEnd] = useState('');
  const [availability_start, setAvailStart] = useState('');
  const [availability_end, setAvailEnd] = useState('');
  const [team_href, setTeam] = useState('');
  const [createShift, result] = useCreateShiftSwapEventMutation();


  async function handleSubmit(e) {
    e.preventDefault();
    createShift({shift_start, shift_end, availability_start, availability_end, team_href});
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
          <input type="datetime-local" id="shift_start" value={shift_start} onChange={e=> setShiftStart(e.target.value)} />
          <hr></hr>
          <h6>Enter Shift End</h6>
          <input type="datetime-local" id="shift_end" value={shift_end} onChange={e=> setShiftEnd(e.target.value)} />
          <h6>Enter Start Availability</h6>
          <input type="datetime-local" id="availability_start" value={availability_start} onChange={e=> setAvailStart(e.target.value)} />
          <hr></hr>
          <h6>Enter End Availability</h6>
          <input type="datetime-local" id="availability_end" value={availability_end} onChange={e=> setAvailEnd(e.target.value)} />
          <hr></hr>
          <div className="dropdown">
          <button className="btn btn-secondary dropdown-toggle" type="button" id="team_href" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Select Team
          </button>
          {/* Needs to generate team list here */}
          <select onChange={e=> setTeam(e.target.value)} value={team_href} className="dropdown-menu" aria-labelledby="dropdownMenu2">
          <option value="">Select a Team</option>
          {salesPersons.map((employee) => {
          return (
          <option key={employee.employee_number} value={employee.employee_number}>{employee.name}</option>
          );
        })}
          </select>
          </div>
          </form>
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


