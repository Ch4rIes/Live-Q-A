import React from 'react'

export default function QnA({entry}) {
  if(entry.answer == null){
    return (
      <div>
        <label>
          <div>
            {entry.question} 
            <br/> Not answered 
          </div>
        </label>
          
      </div>
  
    )
  }else{
    return (
      <div>
        <label>
          <div id='Display'>
            {entry.question}
            {entry.answer}
          </div>
        </label>
          
      </div>
  
    )
  }
}
