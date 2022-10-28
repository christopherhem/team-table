import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom';
import { useUpdateUsersMutation, useGetTokenQuery } from '../../store/UsersApi';

import {
    Form,
    FormH1,
    FormButton,
    CreateInput
} from './SignUpElements';

function Profile() {
    const navigate = useNavigate();
    const [first_name, setFirstName] = useState('');
    const [last_name, setLastName] = useState('');
    const [password, setPassword] = useState('');
    const [phone_number, setPhoneNumber] = useState('')
    const [profile_picture_url, setProfilePic] = useState(');')
    const [updateUser, result] = useUpdateUsersMutation();
    const { data: userData, isLoading: isLoadingUser } = useGetTokenQuery()
    const id = userData.user.id

    if (isLoadingUser) {
        return (
            <progress className="progress is-primary" max="100"></progress>
        );
    }

    function handleSubmit(e) {
        e.preventDefault();
        updateUser({ first_name, last_name, password, phone_number });
    }
    if (result.isSuccess) {
        navigate('/')
    }
    return (
        <>
            <Form onSubmit={(e) => handleSubmit(e)}>
                <FormH1>Edit Account</FormH1>
                <CreateInput
                    id="first_name"
                    placeholder="Enter First Name"
                    value={first_name}
                    onChange={e => setFirstName(e.target.value)}
                    type="text" />
                <CreateInput
                    id="last_name"
                    placeholder="Enter Last Name"
                    value={last_name}
                    onChange={e => setLastName(e.target.value)}
                    type="text" />
                <CreateInput
                    id="password"
                    placeholder="Password"
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                    type="password" />
                <CreateInput
                    id="phone_number"
                    placeholder="Phone Number"
                    value={phone_number}
                    onChange={e => setPhoneNumber(e.target.value)}
                    type="text" />
                <FormButton type='submit'>Submit</FormButton>
            </Form>
        </>
    );
}
export default Profile;
