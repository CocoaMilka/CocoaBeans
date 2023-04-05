import React, { useState } from 'react';
import styles from '../styles/Home.module.css'
import LoginBox from './loginbox';

const Index = () => {
  const [value, setValue] = useState('');

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return (
    <center>
      <div>
      <h1>CocoaBeans</h1>
      <p>Under Construction...</p>
    </div>
    </center>
  );
};

export default Index;