import React, { useState } from 'react'
import styles from "../events/Modal.module.css"
import { RiCloseLine } from "react-icons/ri"
import { useGetValidSwapsQuery } from '../../store/TeamsApi'
import { usePerformSwapMutation } from '../../store/UsersApi'
import DateObject from "react-date-object";


export default function Swap({ setIsOpenSwap }) {
    const {data: swapData, isLoading: isLoadingSwaps} = useGetValidSwapsQuery();
    const [swap, setSwap] = useState()

    if (isLoadingSwaps) {
        return (
            <progress className="progress is-primary" max="100"></progress>
        );
    }


    async function handleSubmit(e) {
        e.preventDefault();
        // updateCover({id, availability_start, availability_end })
        setIsOpenSwap(false);
      }

    return (
        <>
      <div className={styles.darkBG} onClick={() => setIsOpenSwap(false)} />
      <div className={styles.centered}>
        <div className={styles.modal}>
          <div className={styles.modalHeader}>
            <h2 className={styles.heading}>Swap Shifts</h2>
          </div>
          <button className={styles.closeBtn} onClick={() => setIsOpenSwap(false)}>
            <RiCloseLine style={{ marginBottom: "-3px" }} />
          </button>
          <h1>HELOOOO</h1>
          <form className={styles.modalContent} onSubmit={(e) => handleSubmit(e)}>
              {
                swapData.swaps.map((shift) => {
                    shift.valid_swaps.map((swap) => {

                        return (
                            <input type="radio" id={swap.mono_id} value={swap}>{swap.owner}</input>
                        );
                    })
                })
              }


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
    )
}
