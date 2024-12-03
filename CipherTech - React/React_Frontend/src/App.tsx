
import { Routes, Route } from 'react-router-dom'
import './App.css'

import Login from './login'
import Logout from './logout'
import {RequireAuth, useAuth, AuthProvider} from "./hooks/auth";

function App() {
  useAuth();

  return (
    <>
      <div>
        {/* Redesigned using Vite and Typescript instead */}
        <br/>
      </div>
      <AuthProvider>
        <Routes>
          <Route path="/" element={<Login/>} />
          <Route path="/login" element={<>You must be logged in to access that page. <br/><Login/></>} />
          <Route 
            path="/secure" 
            element={
            <RequireAuth>
              <div>
                <Logout/>
                <p>Secure Page</p>
              </div>
            </RequireAuth>
            } 
          />

        </Routes>
      </AuthProvider>
    </>
    
  )
}





export default App
