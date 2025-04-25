import React, {useState} from 'react'
import PropTypes from 'prop-types';
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
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
        <DialogTitle>User Settings</DialogTitle>
        <List sx={{pt:0}}>
            {settings.map((setting)=>(
                <ListItem disablePadding key={setting}>
                    <ListItemButton onClick={()=>handleListItemClick(setting)}>
                        <ListItemText primary={setting}/>
                    </ListItemButton>
                </ListItem>
            ))}
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