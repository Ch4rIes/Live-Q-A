import React from 'react'
import QnA from './QnA'

export default function Entries({entries}) {
  return (
    // include both the question and the answer
    entries.map(entry => {
        return <QnA entry = {entry} key = {entry.id}/>
    })
  )
}
