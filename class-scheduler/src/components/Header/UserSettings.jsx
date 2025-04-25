import React, {useState} from 'react'
import PropTypes from 'prop-types';
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar  from '@mui/material/ListItemAvatar';
import './UserSettings.css'

const settings = ['Update name', 'Update password', 'Change Login Preference']

function MyDialog(props){
    const {onClose,selectedValue,open} = props;
    const handleClose = () =>{
        onClose(selectedValue);
    };
    const handleListItemClick = (value)=>{
        onClose(value);
    };
    
  return (
    <Dialog onClose={handleClose} open={open}>
        <DialogTitle sx={{backgroundColor:'#84A98C'}}>User Settings</DialogTitle>
        <List sx={{pt:0}}>
            {/* {settings.map((setting)=>(
                <ListItem disablePadding key={setting}>
                    <ListItemButton onClick={()=>handleListItemClick(setting)}>
                        <ListItemText primary={setting}/>
                    </ListItemButton>
                </ListItem>
            ))} */}
            
            <ListItem disablePadding key="update-name">
                <ListItemButton onClick={e=>{
                    e.preventDefault();
                    onClose("Update name");
                }}>
                    <ListItemAvatar>
                        <span className="icon-pencil"></span>
                    </ListItemAvatar>
                    <ListItemText primary={"Update name"}/>
                </ListItemButton>
            </ListItem>

            <ListItem disablePadding key="change-password">
                <ListItemButton onClick={e=>{
                    e.preventDefault();
                    onClose("Change Password");
                }}>
                    <ListItemAvatar>
                        <span className="icon-lock"></span>
                    </ListItemAvatar>
                    <ListItemText primary={"Change password"}/>
                </ListItemButton>
            </ListItem>

            <ListItem disablePadding key="change-login-preference">
                <ListItemButton onClick={e=>{
                    e.preventDefault();
                    onClose("Change login preference");
                }}>
                    <ListItemAvatar>
                        <span className="icon-mustache"></span>
                    </ListItemAvatar>
                    <ListItemText primary={"Change login preference"}/>
                </ListItemButton>
            </ListItem>

            <ListItem disablePadding key="logout">
                <ListItemButton type='submit' onClick={e=>{
                    sessionStorage.clear();
                    window.location.reload();
                }}>
                    <ListItemAvatar>
                        <span className="icon-logout"></span>
                    </ListItemAvatar>
                    <ListItemText primary={"Logout User"}/>
                </ListItemButton>
            </ListItem>
        </List>
    </Dialog>
  )
}


export default function UserSettings() {
    const [open,setOpen] = useState(false);

    const handleClickOpen = () =>{
        setOpen(true);
    }
    const handleClickClose = () =>{
        setOpen(false);
    }
    return(
    <>
        <span className="int-icon icon-user" onClick={handleClickOpen}>
        </span>
        <MyDialog 
        open={open}
        onClose={handleClickClose}
        />
    </>
);
}
MyDialog.propTypes = {
    onClose: PropTypes.func.isRequired,
    open:PropTypes.bool.isRequired,
    selectedValue: PropTypes.string.isRequired,
};