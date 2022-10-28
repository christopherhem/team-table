import React, { useState } from 'react'
import InfoSection from '../components/info_section'
import { infoOne, infoThree, infoTwo } from '../components/info_section/Data'
import NavBar from '../components/navbar'
import Sidebar from '../components/sidebar'
import { FlexInfoContainer } from '../components/info_section/InfoElements'
import "react-responsive-carousel/lib/styles/carousel.min.css";
import { Carousel } from "react-responsive-carousel";


import "./carousel.css";

const imageData = [
  {
    label: "User Page",
    alt: "image1",
    url: "https://i.imgur.com/liZ7s5p.png"
  },
  {
    label: "Team Page",
    alt: "image2",
    url:
      "https://i.imgur.com/hsEJAwF.png"
  },
  {
    label: "Create Swap",
    alt: "image3",
    url: "https://i.imgur.com/m73gSAv.png"
  },
  {
    label: "Create Cover",
    alt: "image4",
    url:
      "https://i.imgur.com/CoEUobA.png"
  },
  {
    label: "Swap Event",
    alt: "image4",
    url:
      "https://i.imgur.com/m73gSAv.png"
  },
  {
    label: "Cover Event",
    alt: "image4",
    url:
      "https://i.imgur.com/m73gSAv.png"
  }
];

const renderSlides = imageData.map((image) => (
  <div key={image.alt}>
    <img src={image.url} alt={image.alt} />
    <p className="legend">{image.label}</p>
  </div>
));

const Landing = () => {
  const [isOpen, setIsOpen] = useState(false)

  const toggle = () => {
    setIsOpen(!isOpen)
  }

  const [currentIndex, setCurrentIndex] = useState();
  function handleChange(index) {
    setCurrentIndex(index);
  }

  return (
    <>
      <Sidebar isOpen={isOpen} toggle={toggle} />
      <NavBar toggle={toggle} />
      <FlexInfoContainer>
        <InfoSection {...infoOne} />
        <InfoSection {...infoTwo} />
        <InfoSection {...infoThree} />
      </FlexInfoContainer>
      <div className="App">
      <Carousel
        showArrows={true}
        autoPlay={true}
        infiniteLoop={true}
        selectedItem={imageData[currentIndex]}
        onChange={handleChange}
        className="carousel-container"
      >
        {renderSlides}
      </Carousel>
    </div>
    </>
  )
}

export default Landing