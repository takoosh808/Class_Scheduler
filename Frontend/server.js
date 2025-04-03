import express from 'express';
import cors from 'cors';

const app = express();

app.use(cors());

app.use('/login',(req,res)=>{
    res.send({
        token:'abc123'
    });
});

app.get('/login',(req,res)=>{
    return res.send('Recieved a GET HTTP method');
});
app.post('/login',(req,res)=>{
    return res.send('Recieved a POST HTTP method');
})

app.listen(8080,()=>console.log("API is running on http://localhost:8080/login"));