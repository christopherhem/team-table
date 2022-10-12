import React, { useState } from 'react'

function BootstrapInput(props) {
    const { id, placeholder, labelText, value, onChange, type } = props;

    return (
        <div className="mb-4">
            <label htmlFor={id} className="form-label">{labelText}</label>
            <input value={value} onChange={onChange} required type={type} className="form-control" id={id} placeholder={placeholder} />
        </div>
    )
}

function SignUp(props) {
    // const {token, signup} = props; ?? 
    const [email, setEmail] = useState('');
    const [userName, setUserName] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const [password, setPassword] = useState('');

    // if (token) {
    //     return <Navigate to="/" />;
    // }
    
    return (
    <form>
        <BootstrapInput 
            id="email" 
            placeholder="you@example.com" 
            labelText="Your email address" 
            value={email} 
            onChange={e=> setEmail(e.target.value)}
            type="email" />
        <BootstrapInput 
            id="username" 
            placeholder="Enter User Name" 
            labelText="Create User Name" 
            value={userName} 
            onChange={e=> setUserName(e.target.value)}
            type="text" />
        <BootstrapInput 
            id="first_name" 
            placeholder="Enter First Name" 
            labelText="First Name" 
            value={firstName} 
            onChange={e=> setFirstName(e.target.value)}
            type="text" />
        <BootstrapInput 
            id="last_name" 
            placeholder="Enter Last Name" 
            labelText="Last Name" 
            value={lastName} 
            onChange={e=> setLastName(e.target.value)}
            type="text" />
        <BootstrapInput 
            id="phone_number" 
            placeholder="you@example.com" 
            labelText="Phone Number" 
            value={phoneNumber} 
            onChange={e=> setPhoneNumber(e.target.value)}
            type="text" />
        <BootstrapInput 
            id="password" 
            placeholder="Enter password" 
            labelText="Password" 
            value={password} 
            onChange={e=> setPassword(e.target.value)}
            type="password" />
        <button type="submit" className="btn btn-primary">Submit</button>
    </form>
    
  );
}

export default SignUp;
