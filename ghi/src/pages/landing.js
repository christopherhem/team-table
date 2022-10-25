import React, {useState} from 'react'
import InfoSection from '../components/info_section'
import { infoOne, infoThree, infoTwo } from '../components/info_section/Data'
import NavBar from '../components/navbar'
import Sidebar from '../components/sidebar'
import { FlexInfoContainer } from '../components/info_section/InfoElements'

const Landing = () => {
    const [isOpen, setIsOpen] = useState(false)

    const toggle = () => {
        setIsOpen(!isOpen)
    }

  return (
    <>
      <Sidebar isOpen={isOpen} toggle={toggle}/>
      <NavBar toggle={toggle} />
      <FlexInfoContainer>
      <InfoSection {...infoOne} />
      <InfoSection {...infoTwo} />
      <InfoSection {...infoThree} />
      </FlexInfoContainer>
    </>
  )
}

export default Landing