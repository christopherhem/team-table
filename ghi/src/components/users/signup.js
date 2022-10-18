import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom';
import ErrorNotification from '../../ErrorNotification';
import { useCreateUsersMutation } from '../../store/UsersApi';

import {
    Container,
    FormWrap,
    Icon,
    FormContent,
    Form,
    FormH1,
    FormButton,
    CreateInput
  } from './SignUpElements';

function SignUp() {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [userName, setUserName] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);
    const [createUser, result] = useCreateUsersMutation();
    console.log(process.env.REACT_APP_MONO_API)
    async function handleSubmit(e) {
        e.preventDefault();
        createUser({email, userName, firstName, lastName, phoneNumber,password});
        if (result.isSuccess) {
            navigate("/dashboard");
        } else {
            setError(result.error);
        }
    }

    return (
    <>
    <Container>
        <FormWrap>
        <Icon to='/'>TeamTable</Icon>
        <ErrorNotification error={error}/>
        <FormContent>
        <Form onSubmit={(e) => handleSubmit(e)}>
        <FormH1>Create Account</FormH1>
        <CreateInput
            id="email"
            placeholder="Enter Email"
            labelText="Your email address"
            value={email}
            onChange={e=> setEmail(e.target.value)}
            type="email" />
        <CreateInput
            id="username"
            placeholder="Enter User Name"
            labelText="Create User Name"
            value={userName}
            onChange={e=> setUserName(e.target.value)}
            type="text" />
        <CreateInput
            id="first_name"
            placeholder="First Name"
            labelText="First Name"
            value={firstName}
            onChange={e=> setFirstName(e.target.value)}
            type="text" />
        <CreateInput
            id="last_name"
            placeholder="Last Name"
            labelText="Last Name"
            value={lastName}
            onChange={e=> setLastName(e.target.value)}
            type="text" />
        <CreateInput
            id="phone_number"
            placeholder="Phone Number"
            labelText="Phone Number"
            value={phoneNumber}
            onChange={e=> setPhoneNumber(e.target.value)}
            type="text" />
        <CreateInput
            id="password"
            placeholder="Password"
            labelText="Password"
            value={password}
            onChange={e=> setPassword(e.target.value)}
            type="password" />
         <FormButton type='submit'>Submit</FormButton>
        </Form>
        </FormContent>
        </FormWrap>
    </Container>
    </>
  );
}
export default SignUp;
