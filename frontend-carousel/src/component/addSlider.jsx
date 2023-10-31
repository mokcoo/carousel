import React, { useState } from 'react';
import { addNewSlider } from '../utils/addNewSlider';

export default function AddSlider() {
  const [data, setData] = useState([
    { title: '', description: '', buttonText: '', component: '', link: '' }
  ]);

  const handleChange = (index, event) => {
    const values = [...data];
    values[index][event.target.name] = event.target.value;
    setData(values);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const payload = { data };
    addNewSlider(JSON.stringify(payload))
    //console.log('JSON Data:', JSON.stringify(payload));
    // Send payload to backend or other logic here...
  };

  const handleAddFields = () => {
    const values = [...data];
    values.push({ title: '', description: '', buttonText: '', component: '', link: '' });
    setData(values);
  };

  return (
    <form onSubmit={handleSubmit}>
      {data.map((item, index) => (
        <div key={index}>
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
        Add More
      </button>
      <button type="submit">Submit</button>
    </form>
  );
}


