// Creates a simple hook to handle authenticated user states and some logic.


import { createContext, useContext, useState } from "react";
import { Navigate, useLocation, useNavigate } from "react-router-dom";


interface AuthCountextType {
    user: any,
    signin: (userToken: string, callback:VoidFunction) => void;
    signout: (callback:VoidFunction) => void;
}

let AuthContext = createContext<AuthCountextType>(null!);

// Wraps the children elements of AuthProvider between the necessary functions
export const AuthProvider = ({children}: {children: React.ReactNode}) => {
    const navigate = useNavigate();
    let [user, setUser] = useState<any>(null);

    // Signin function
    // Future TODO - expand to accept 2 args - the token, and redirect path
    let signin = async (data:string) => {
        setUser(data);
        navigate("/secure");
    }

    // Signout function    
    // Future TODO - expand to handle redirects if needed (Or just let the Auth wrapper handle it)
    let signout = () => {
        setUser(null);
        navigate("/", {replace: true});
    }

    let value = {user, signin, signout};
    return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

// Method for locking authenticated pages 
export const RequireAuth = ({children}: {children: JSX.Element}): JSX.Element => {
    let auth = useAuth();
    let location = useLocation();

    // Future TODO - instead of having the password be kept in current session memory where it instantly expires on manual redirects
    // Move it to longer-term memory with a proper expiry token
    if (!auth.user) {
        // Redirect to login page, retain the page they were trying to access
        return <Navigate to="/login" state={{from: location}} replace />;
    }

    return children;
}


export const useAuth = () => {
    return useContext(AuthContext);
};