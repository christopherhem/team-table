
import React, { useState, useEffect } from 'react'
import styles from '../events/Modal.module.css'
import { RiCloseLine } from "react-icons/ri"
import { usePerformCoverSwapMutation, useGetAllCoverEventsQuery} from '../../store/UsersApi';
import { useGetValidCoverSwapsQuery} from '../../store/TeamsApi';
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
import DateObject from "react-date-object";


export default function CoverSwap({ handleClose, i }) {
  const [valid_swap, setValidSwap] = useState(null);
  const [shiftSwapEvents, setShiftSwapEvents] = useState(null);
  const [coverEvents, setCoverEvents] = useState([])
  const {data: validData, isLoading: isLoadingCoverSwaps} = useGetValidCoverSwapsQuery(i);
  const [performCoverSwap, result] = usePerformCoverSwapMutation();


  const fetchCoverEvents = async () => {
    const url = "http://localhost:8080/api/table/cover_events/"
    const response = await fetch(url)
    if (response.ok) {
      const theJson = await response.json()
      console.log(theJson)
      setCoverEvents(theJson)
    }
  }

  const fetchShiftSwapEvents = async () => {
    const url = "http://localhost:8080/api/table/shift_swap_events/"
    const response = await fetch(url)
    if (response.ok) {
      const ssData = await response.json()
      console.log(ssData)
      setShiftSwapEvents(ssData)
    }
  }

  async function handleSubmit(e) {
    e.preventDefault();
    let u_event = coverEvents.filter((event) => event.id === i)
    let s_event = shiftSwapEvents.filter((event) => event.id === parseInt(valid_swap))
    let obj = {}
    obj['cover'] = u_event[0]
    obj['swap'] = s_event[0]
    console.log(obj)
    performCoverSwap(obj);


    // handleClose();
  }
  useEffect(() => {
    fetchCoverEvents();
    fetchShiftSwapEvents();
  }, [])

  if (isLoadingCoverSwaps ) {
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
            <h2 className={styles.heading}>Create a cover event</h2>
          </div>
          <button className={styles.closeBtn} onClick={() => handleClose()}>
            <RiCloseLine style={{ marginBottom: "-3px" }} />
          </button>
          <form className={styles.modalContent} onSubmit={(e) => handleSubmit(e)}>
            <div className="mb-3">
              <select onChange={e => setValidSwap(e.target.value)} value={valid_swap} className="form-select" name="valid_swap" id="valid_swap">
                <option value="">Select a Team</option>
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
