import React, {useState} from 'react'
import NavBar from '../components/navbar'
import Sidebar from '../components/sidebar'

const Home = () => {
    const [isOpen, setIsOpen] = useState(false)

    const toggle = () => {
        setIsOpen(!isOpen)
    }

  return (
    <>
        <Sidebar isOpen={isOpen} toggle={toggle}/>
        <NavBar toggle={toggle} />
    </>
  )
}

export default Home