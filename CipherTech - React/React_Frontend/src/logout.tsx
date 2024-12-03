// Reusable logout button/link functionality that can be dropped into any page

import {useAuth} from "./hooks/auth";

const Logout = () => {
    const { signout } = useAuth();
    const logoff_process = async () => {
        // Revoke the user's authentication token - redirects are handled by signout
        await signout(() =>{});
    }

    return (
        <div>
            {/* Logout Chunk <br/> */}
            <div className={"LogoutContainer"}>
                <input
                    type="button"
                    className={"logoutButton"}
                    value="Log Out"
                    onClick={logoff_process}
                />
            </div>
        </div>
    )
}

export default Logout;