import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useSignInMutation } from '../../store/UsersApi';
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

} from './SignInElements';

function SignIn() {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [signIn, result] = useSignInMutation();

  async function handleSubmit(e) {
    e.preventDefault();
    signIn(
      { email, password }
    )
  }
  if (result.isSuccess) {
    console.log("Login Successful")
    navigate("/");
    localStorage.setItem('email', JSON.stringify(email));
    localStorage.setItem('token', JSON.stringify(result.data.access_token));
  } else if (result.isError) {
    console.log("Error Login")

  }

  return (
    <>
      <Container>
        <FormWrap>
          <Icon to='/'>TeamTable</Icon>
          <FormContent>
            <Form onSubmit={(e) => handleSubmit(e)}>
              <FormH1>Sign into your account</FormH1>
              <FormLabel htmlFor='for'>Email</FormLabel>
              <FormInput onChange={(e) => setEmail(e.target.value)} value={email} type='email' required />
              <FormLabel htmlFor='for'>Password</FormLabel>
              <FormInput onChange={(e) => setPassword(e.target.value)} value={password} type='password' required />
              <FormButton type='submit'>Continue</FormButton>
            </Form>
          </FormContent>
        </FormWrap>
      </Container>
    </>
  );
};

export default SignIn;
