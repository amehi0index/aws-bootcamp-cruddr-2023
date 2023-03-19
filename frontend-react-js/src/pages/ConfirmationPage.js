import './ConfirmationPage.css';
import React from "react";
import { useLocation } from 'react-router-dom';
import {ReactComponent as Logo} from '../components/svg/logo.svg';

import { Auth } from 'aws-amplify';

export default function ConfirmationPage() {

  const location = useLocation();

  const [email, setEmail] = React.useState('');
  const [code, setCode] = React.useState('');
  const [errors, setErrors] = React.useState('');
  const [codeSent, setCodeSent] = React.useState(false);

  React.useEffect(()=>{
    if (location.state.email) {
      setEmail(location.state.email)
    }
  }, [])

  const code_onchange = (event) => {
    setCode(event.target.value);
  }
  const email_onchange = (event) => {
    setEmail(event.target.value);
  }

  const resend_code = async (event) => {
    setErrors('')
    try {
      await Auth.resendSignUp(email);
      console.log('code resent successfully');
      setCodeSent(true)
    } catch (err) {
      // does not return a code
      // does cognito always return english
      // for this to be an okay match?
      console.log(err)
      if (err.message == 'Username cannot be empty'){
        setErrors("You need to provide an email in order to send Resend Activiation Code")   
      } else if (err.message == "Username/client id combination not found."){
        setErrors("Email is invalid or cannot be found.")   
      }
    }
  }

  const onsubmit = async (event) => {
    event.preventDefault();
    setErrors('')
    try {
      await Auth.confirmSignUp(email, code);
      //Should check user --> sign user in here
      //await Auth.signIn(email, password)
      //checkUser()
      window.location.href = "/"
    } catch (error) {
      setErrors(error.message)
    }
    return false
  }

//   async function checkUser(){
//     try {
//       const user = await Auth.currentAuthenticatedUser()
//       const { email, nickname } = user.attributes
//       setUser(()=> nickname ? nickname : email)
//       await Auth.currentAuthenticatedUser()
      
//       console.log(({ user }))
//     } catch (error) {
//        setUser(null)
//        setUiState('signIn')
//     }
// }


  let el_errors;
  if (errors){
    el_errors = <div className='errors'>{errors}</div>;
  }


  let code_button;
  if (codeSent){
    code_button = <div className="sent-message">A new activation code has been sent to your email</div>
  } else {
    code_button = <button className="resend" onClick={resend_code}>Resend Activation Code</button>;
  }

  return (
    <article className="confirm-article">
      <div className='recover-info'>
        <Logo className='logo' />
      </div>
      <div className='recover-wrapper'>
        <form
          className='confirm_form'
          onSubmit={onsubmit}
        >
          <h2>Confirm your Email</h2>
          <div className='fields'>
            <div className='field text_field email'>
              <label>Email</label>
              <input
                type="text"
                value={email}
                onChange={email_onchange} 
              />
            </div>
            <div className='field text_field code'>
              <label>Confirmation Code</label>
              <input
                type="text"
                value={code}
                onChange={code_onchange} 
              />
            </div>
          </div>
          {el_errors}
          <div className='submit'>
            <button type='submit'>Confirm Email</button>
          </div>
        </form>
      </div>
      {code_button}
    </article>
  );
}