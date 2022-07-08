import React, {useState, useRef, useEffect} from 'react'
import Entries from './Entries.js'
import axios from 'axios'


function App() {
  const [entries , setEntries] = useState([
  ]);
  useEffect(()=>{
    fetch("/Entries/obtain").then(
      res => res.json()
    ).then(
       entries =>{
        setEntries(entries)
        console.log(entries)
       }
    )
  }, [])


  const userInputQuestion = useRef();
  const uuid = require('uuid');
  function create_question(e){
    const questionBody = userInputQuestion.current.value;
    if(questionBody === '') return;
    const new_id = Math.floor(Math.random() * 10000) + 1
    fetch('/Entries/create' , {
      method: 'POST',
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        "id": new_id,
        "question": questionBody
      })
    }).then(()=>{
      console.log('new entry created')
    }

    )
    console.log(new_id)
    setEntries(prevEntries =>{
      return [...prevEntries , {id: new_id, question: questionBody , answer: null}]
    })

    userInputQuestion.current.value = null;
  }
  
  
  
  return (
   <>
    <h1>Q&A</h1>
    <input ref={userInputQuestion} type="text"></input>
    <button onClick={create_question}> Ask me</button>
    <Entries entries = {entries}> </Entries>
   </>
  );
}

export default App;
