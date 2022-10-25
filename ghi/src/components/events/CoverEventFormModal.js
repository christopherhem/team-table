// Create Event Form Modal
import React, { useState } from 'react'
import styles from "./Modal.module.css"
import { RiCloseLine } from "react-icons/ri"
import { useCreateCoverEventMutation } from '../../store/UsersApi';
import { useGetUsersTeamsQuery } from '../../store/UsersApi';
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


export default function CoverEventFormModal({ setIsOpenCover }) {
  const [availability_start, setStart] = useState('');
  const [availability_end, setEnd] = useState('');
  const [team_href, setTeam] = useState('');
  const [createCover, result] = useCreateCoverEventMutation();
  const { data, error, isLoading } = useGetUsersTeamsQuery({});

  if (isLoading) {
    return (
      <progress className="progress is-primary" max="100"></progress>
    );
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setIsOpenCover(false);
    createCover({ availability_start, availability_end, team_href });
    console.log(result)
  }

  return (
    <>
      <div className={styles.darkBG} onClick={() => setIsOpenCover(false)} />
      <div className={styles.centered}>
        <div className={styles.modal}>
          <div className={styles.modalHeader}>
            <h2 className={styles.heading}>Create a cover event</h2>
          </div>
          <button className={styles.closeBtn} onClick={() => setIsOpenCover(false)}>
            <RiCloseLine style={{ marginBottom: "-3px" }} />
          </button>
          <form className={styles.modalContent} onSubmit={(e) => handleSubmit(e)}>
            <h6>Enter Start Availability</h6>
            <input type="datetime-local" id="availability_start" value={availability_start} onChange={e => setStart(e.target.value)} />
            <hr></hr>
            <h6>Enter End Availability</h6>
            <input type="datetime-local" id="availability_end" value={availability_end} onChange={e => setEnd(e.target.value)} />
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
                <button className={styles.deleteBtn}>
                  Submit
                </button>
                <button
                  className={styles.cancelBtn}
                  onClick={() => setIsOpenCover(false)}
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
