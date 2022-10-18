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
    const [username, setUserName] = useState('');
    const [first_name, setFirstName] = useState('');
    const [last_name, setLastName] = useState('');
    const [phone_number, setPhoneNumber] = useState('');
    const [password, setPassword] = useState('');
    const [profile_picture_href, setProfilePic] = useState('')
    const [error, setError] = useState(null);
    const [createUser, result] = useCreateUsersMutation();
    console.log(process.env.REACT_APP_MONO_API)
    async function handleSubmit(e) {
        e.preventDefault();
        createUser({email, username, first_name, last_name, phone_number, password, profile_picture_href});
    }

    if (result.isSuccess) {
        navigate('/dashboard');
    } else if (result.isError) {
        setError(result.error);
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
            value={username} 
            onChange={e=> setUserName(e.target.value)}
            type="text" />
        <CreateInput 
            id="first_name" 
            placeholder="First Name" 
            labelText="First Name" 
            value={first_name} 
            onChange={e=> setFirstName(e.target.value)}
            type="text" />
        <CreateInput 
            id="last_name" 
            placeholder="Last Name" 
            labelText="Last Name" 
            value={last_name} 
            onChange={e=> setLastName(e.target.value)}
            type="text" />
        <CreateInput 
            id="phone_number" 
            placeholder="Phone Number" 
            labelText="Phone Number" 
            value={phone_number} 
            onChange={e=> setPhoneNumber(e.target.value)}
            type="text" />
        <CreateInput
            id="password"
            placeholder="Password"
            labelText="Password"
            value={password}
            onChange={e=> setPassword(e.target.value)}
            type="password" />
        <CreateInput 
            id="profile_picture_href" 
            placeholder="Profile Picture" 
            labelText="Profile Picture" 
            value={profile_picture_href} 
            onChange={e=> setProfilePic(e.target.value)}
            type="url" />
         <FormButton type='submit'>Submit</FormButton>
        </Form>
        </FormContent>
        </FormWrap>
    </Container>
    </>
  );
}
export default SignUp;
