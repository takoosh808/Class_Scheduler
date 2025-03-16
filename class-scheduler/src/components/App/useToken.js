import { useState } from "react";

export default function useToken() {

    function getToken(){
        const tokStr = sessionStorage.getItem('token');
        const userTok = JSON.parse(tokStr);
        return userTok?.token;
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
