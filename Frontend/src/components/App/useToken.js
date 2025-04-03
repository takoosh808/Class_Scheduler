import { useState } from "react";

export default function useToken() {

    function getToken(){
        const tokStr = sessionStorage.getItem('token');
        const userTok = JSON.parse(tokStr);
        return userTok?.token; //Optional chaining (?) is necessary here! Optional chaining will return undefined if the property DNE which will prevent a very common runtime errors
      }

    const [token,setToken] = useState(getToken());

    const saveToken = userTok =>{
        sessionStorage.setItem('token', JSON.stringify(userTok));
        setToken(userTok.token);
    }
    
    return{
        setToken: saveToken,
        token
    }
}
