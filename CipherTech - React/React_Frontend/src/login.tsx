// Recreating the login stuff in Typescript

import { useState } from "react";
import {useAuth} from "./hooks/auth";
import { useLocation, Navigate } from "react-router-dom";


// Future TODO - centralize the API path so all other pages/tools that need it can pull from shared import
// Only login needed the API presently, so the value is loaded in here.
const api_path = "http://localhost:5000"



const Login = () => {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [emailValidity, setEmailValidity] = useState("")
    const [passValidity, setPassValidity] = useState("")

    
    // Basic sanity checks, mainly empty fields
    const frontend_validation = () => {
        // Wipe out previous messages
        setPassValidity("");
        setEmailValidity("");

        // Username validation 
        if (username.length == 0) {
            setEmailValidity("Please enter an username");
            return false
        }

        if (password.length == 0){
            setPassValidity("Please enter a password");
            return false
        }

        return true
    }

    const state = useLocation();
    const { signin } = useAuth();

    const login_process = async() => {
        if (frontend_validation()) {
            // Trigger POST request, then update auth.signin() with our credentials obtained
            // Tried to figure out https, but Flask wasn't cooperating with that for whatever reason

            
            const response =  await fetch(api_path + "/api_login",{
                headers:{
                    'content-type': 'application/json',
                },
                method: 'POST',
                body: JSON.stringify({'username': username, 'password': password}),
            }) ;  
            // signin();
            
            if (response.status == 200) {
                // Login successful - set the returned token and redirect to where we were going
                console.log(state)
                console.log(response)
                if (!state.state){
                    // No state attribute, default redirect
                }
                else if (state.state.from.pathname){
                    // Path has been found - trigger redirect back (Or just go to landing screen)
                    // State info is available in useLocation() if we want to implement that
                }
                // Future TODO - Use token returned by API rather than a temp value here
                await signin('token', ()=>{});

            }
            else if (response.status == 400) {
                setEmailValidity("Error in request to backend")
            }
            else if (response.status == 401) {
                setEmailValidity("Error: Invalid username or password")
            }
            else {
                setEmailValidity("Unknown error encountered")
            }
            // console.log(await response.json())
            
        }
    }

    // Login is handled as a chunk, so this can be inserted into multiple pages and still behave as expected
    return (
        <div>
            {/* Login Chunk */}
            <br/>

            <div className={"inputContainer"}>
                <input
                    value={username}
                    placeholder="Username"
                    onChange={ev => setUsername(ev.target.value)}
                    className={"textInputBox"}
                />
            </div>
            <div className={"inputContainer"}>
                <input
                    type="password"
                    value={password}
                    placeholder="Password"
                    onChange={ev => setPassword(ev.target.value)}
                    className={"textInputBox"}
                />
            </div>

            <div className={"inputContainer"}>
                <input
                    type="button"
                    className = {"inputButton"}
                    value = {"Log In"}
                    onClick={login_process}
                />
            </div>

            <div>
                <label className="validationError">{emailValidity}</label>
                <label className="validationError">{passValidity}</label>
            </div>
        </div>
    )
}
export default Login;