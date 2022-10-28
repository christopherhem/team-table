// Create Event Form Modal
import React, { useState, useEffect } from 'react'
import styles from '../events/Modal.module.css'
import { RiCloseLine } from "react-icons/ri"
import { usePerformSwapMutation } from '../../store/UsersApi';
import { useGetValidSwapsQuery } from '../../store/TeamsApi';
import DateObject from "react-date-object";


export default function Swap({ handleClose, i }) {
  const [valid_swap, setValidSwap] = useState(null);
  const [events, setEvents] = useState([])
  const { data: validData, isLoading: isLoadingSwaps } = useGetValidSwapsQuery(i);
  const [performSwap, result] = usePerformSwapMutation();

  const fetchEvents = async () => {
    const url = "http://localhost:8080/api/table/shift_swap_events/"
    const response = await fetch(url)
    if (response.ok) {
      const theJson = await response.json()
      setEvents(theJson)
    }
  }

  async function handleSubmit(e) {
    e.preventDefault();
    let u_event = events.filter((event) => event.id === i)
    let s_event = events.filter((event) => event.id === parseInt(valid_swap))
    let swap = []
    swap.push(u_event[0])
    swap.push(s_event[0])
    performSwap(swap);
    handleClose();
  }
  useEffect(() => {
    fetchEvents();
  }, [])

  if (isLoadingSwaps) {
    return (
      <progress className="progress is-primary" max="100"></progress>
    );
  }

  return (
    <>
      <div className={styles.darkBG} onClick={() => handleClose()} />
      <div className={styles.centered}>
        <div className={styles.modal}>
          <div className={styles.modalHeader}>
            <h2 className={styles.heading}>Swap Shifts</h2>
          </div>
          <button className={styles.closeBtn} onClick={() => handleClose()}>
            <RiCloseLine style={{ marginBottom: "-3px" }} />
          </button>
          <form className={styles.modalContent} onSubmit={(e) => handleSubmit(e)}>
            <div className="mb-3">
              <select onChange={e => setValidSwap(e.target.value)} value={valid_swap} className="form-select" name="valid_swap" id="valid_swap">
                <option value="">Select a Swap Event</option>
                {validData.map((obj) => {
                  const date1 = new Date(obj.shift_start)
                  const date2 = new Date(obj.shift_end)

                  return (
                    <option key={obj.mono_id} value={obj.mono_id}>{new DateObject(date1).format("ddd DD MMM YYYY hh:mm a")} - {new DateObject(date2).format("ddd DD MMM YYYY hh:mm a")}</option>
                  );
                })}
              </select>
            </div>
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
