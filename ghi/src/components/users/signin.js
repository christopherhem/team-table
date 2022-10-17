import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useCreateTokenMutation } from '../../store/UsersApi';
import ErrorNotification from '../../ErrorNotification';
import React from 'react';
import {
  Container,
  FormWrap,
  Icon,
  FormContent,
  Form,
  FormH1,
  FormLabel,
  FormInput,
  FormButton,
  Text
} from './SignInElements';

function SignIn() {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [createToken, result] = useCreateTokenMutation();

    async function handleSubmit(e) {
      e.preventDefault();
      createToken(new FormData(e.target));
    }

    if (result.isSuccess) {
      navigate('/dashboard');
    } else {
      setError(result.error);
    }

  return (
    <>
      <Container>
        <FormWrap>
          <Icon to='/'>TeamTable</Icon>
          <FormContent>
            <Form onSubmit={handleSubmit}>
              <FormH1>Sign into your account</FormH1>
              <FormLabel htmlFor='for'>Email</FormLabel>
              <FormInput onChange={setEmail} value={email.email}type='email' required />
              <FormLabel htmlFor='for'>Password</FormLabel>
              <FormInput onChange={setPassword} value={password.password} type='password' required />
              <FormButton type='submit'>Continue</FormButton>
              {/* <Text>Forgot password?</Text> */}
            </Form>
          </FormContent>
        </FormWrap>
      </Container>
    </>
  );
};

export default SignIn;

