import React, { useState } from 'react';
import { addSubject } from '../api/subjectAPI';

const SubjectForm = () => {
  const [name, setName] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await addSubject(name);
      setName('');
    } catch (error) {
      console.error('Error adding subject:', error);
    }
  };

  return (
    <div>
      <h1>Add Subject</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Subject Name"
          required
        />
        <button type="submit">Add Subject</button>
      </form>
    </div>
  );
};

export default SubjectForm;
