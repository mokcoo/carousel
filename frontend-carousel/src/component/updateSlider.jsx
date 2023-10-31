import React, { useState } from 'react';
import { updateSliderById } from '../utils/updateSliderById';

export default function UpdateSlider() {
  const [data, setData] = useState([
    { id:'',title: '', description: '', buttonText: '', component: '', link: '' }
  ]);
  const [sliderId,setSliderId] = useState(-1)

  const handleChange = (index, event) => {
    const values = [...data];
    values[index][event.target.name] = event.target.value;
    setData(values);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const payload = { data };
    const jsonData = JSON.stringify(payload)
    updateSliderById(sliderId,jsonData)
    //console.log('JSON Data:', JSON.stringify(payload));
    
  };

  const handleAddFields = () => {
    const values = [...data];
    values.push({ id:'',title: '', description: '', buttonText: '', component: '', link: '' });
    setData(values);
  };

  return (
    <form onSubmit={handleSubmit}>
        <input
        type='text'
        name='sliderid'
        placeholder='slider id'
        onChange={(e)=> setSliderId(e.target.value)}
        />
      {data.map((item, index) => (
        <div key={index}>
            <input
            type="text"
            name="id"
            placeholder="id"
            value={item.id}
            onChange={(event) => handleChange(index, event)}
          />
          <input
            type="text"
            name="title"
            placeholder="Title"
            value={item.title}
            onChange={(event) => handleChange(index, event)}
          />
          <input
            type="text"
            name="description"
            placeholder="Description"
            value={item.description}
            onChange={(event) => handleChange(index, event)}
          />
          <input
            type="text"
            name="buttonText"
            placeholder="Button Text"
            value={item.buttonText}
            onChange={(event) => handleChange(index, event)}
          />
          <input
            type="text"
            name="component"
            placeholder="Component"
            value={item.component}
            onChange={(event) => handleChange(index, event)}
          />
          <input
            type="text"
            name="link"
            placeholder="Link"
            value={item.link}
            onChange={(event) => handleChange(index, event)}
          />
        </div>
      ))}
      <button type="button" onClick={handleAddFields}>
        Update More
      </button>
      <button type="submit">Submit</button>
    </form>
  );
}


