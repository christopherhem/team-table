// Create Event Form Modal
import React, { useState, useCallback } from 'react'
import styles from '../events/Modal.module.css'
import { RiCloseLine } from "react-icons/ri"
import { usePerformSwapMutation, useGetUserShiftSwapEventsQuery, useGetTokenQuery} from '../../store/UsersApi';
import { useGetValidSwapsQuery } from '../../store/TeamsApi';
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
import DateObject from 'react-date-object';


export default function Swap({ setIsOpenSwap, id }) {
  console.log(id)
  const [swap, setSwap] = useState([]);
  const [valid_swap, setValidSwap] = useState({});
  const {data: validData, isLoadingSwaps} = useGetValidSwapsQuery(id);
  const [performSwap, result] = usePerformSwapMutation();

  if (isLoadingSwaps ) {
    return (
      <progress className="progress is-primary" max="100"></progress>
    );
  }
console.log(validData)
//  const validSwapsCallBack = useCallback ((e) => {
//     const {data: validData} = useGetValidSwapsQuery(e);
//     console.log(validData)
//   },
//   [user_event],);


  async function handleSubmit(e) {
    e.preventDefault();
    setIsOpenSwap(false);
    // performSwap([{user_event, valid_swap}]);
  }

  return (
    <>
      <div className={styles.darkBG} onClick={() => setIsOpenSwap(false)} />
      <div className={styles.centered}>
        <div className={styles.modal}>
          <div className={styles.modalHeader}>
            <h2 className={styles.heading}>Create a cover event</h2>
          </div>
          <button className={styles.closeBtn} onClick={() => setIsOpenSwap(false)}>
            <RiCloseLine style={{ marginBottom: "-3px" }} />
          </button>
          <form className={styles.modalContent} onSubmit={(e) => handleSubmit(e)}>
            <div className="mb-3">
              {/* <select onChange={e => setValidSwap(e.target.value)} value={valid_swap} className="form-select" name="valid_swap" id="valid_swap">
                <option value="">Select a Team</option>
                {validData.map((obj) => {
                  return (
                    <option key={obj.mono_id} value={obj.mono_id}>{new DateObject(obj.shift_start).format("ddd DD MMM YYYY hh mm")}</option>
                  );
                })}
              </select> */}
            </div>
            <div className="mb-3">
              {/* { user_event ?
              <select onChange={e => setValidSwap(e.target.value)} value={valid_swap} className="form-select" name="valid_swap" id="valid_swap">
                <option value="">Select a Team</option>
                {validData.map((shift) => {
                  console.log("SHIFT", shift.valid_swaps)
                  if (shift.user_event.mono_id === user_event) {
                    shift.valid_swaps.map((vs) => {
                      return (
                        <option key={vs.mono_id} value={vs.mono_id}>{new DateObject(swap.shift_start).format("ddd DD MMM YYYY hh mm")}</option>
                      );
                    })
                  }
                    })
                  }
              </select>: null} */}

            </div>
            <div className={styles.modalActions}>
              <div className={styles.actionsContainer}>
                <button className={styles.deleteBtn}>
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
          </form>
        </div>
      </div>
    </>
  );
};
