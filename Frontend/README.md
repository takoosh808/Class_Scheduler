# Class Scheduler
### Brian Leung, Ben Metzger, Travis Takushi

## Documentation for Sprint 1 Frontend
- Main layout created
- Basic login authentication implemented
    - Needs to communicate with backend to verify credentials
    - Using *server.js* to send token
- Basic styling

# Testing and Using Sprint 1 Frontend
- Gets token from 
```
server.js
```
and stores in sessionStorage. Any username/password will get the token for the time being.
sessionStorage will clear the token when the window is closed. Alternatively we can use localStorage to save token outside of window (tradoff is security)