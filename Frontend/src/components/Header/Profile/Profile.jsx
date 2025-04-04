import {useState} from "react"
import { Description,Dialog,DialogPanel,DialogTitle } from '@headlessui/react'
import "./Profile.css"


export const Profile = ({name="User"}) => {
    let [isOpen,setIsOpen] = useState(false);

    return (<>
        <span className="int-icon icon-user" onClick={e=>{
                        e.stopPropagation();
                        setIsOpen(true)
                    }}>
        </span>
        <Dialog open={isOpen} onClose={()=>setIsOpen(false)} id="container">
            <div id="contents">
                <DialogPanel className="max w-large space-y-4 border bg-white p-12">
                    <DialogTitle className="font-bold">Profile Settings</DialogTitle>
                    <Description>Welcome, {name}</Description>
                    <p>Setting 1</p>
                    <p>Setting 2</p>
                    <p>Setting 3</p>
                    <button onClick={()=>setIsOpen(false)}>Close</button>
                </DialogPanel>
            </div>
        </Dialog>
    </>)
}

