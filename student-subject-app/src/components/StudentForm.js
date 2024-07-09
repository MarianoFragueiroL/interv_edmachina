import React, { useState } from 'react';
import { addStudent } from '../api/studentAPI';

const StudentForm = () => {
  const [studentData, setStudentData] = useState({
    name: '',
    email: '',
    address: '',
    phone: '',
    career: '',
    subject_repeats: 0,
    subjects: []
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setStudentData({ ...studentData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await addStudent(studentData);
      setStudentData({
        name: '',
        email: '',
        address: '',
        phone: '',
        career: '',
        subject_repeats: 0,
        subjects: []
      });
    } catch (error) {
      console.error('Error adding student:', error);
    }
  };

  return (
    <div>
      <h1>Add Student</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" name="name" value={studentData.name} onChange={handleChange} placeholder="Name" required />
        <input type="email" name="email" value={studentData.email} onChange={handleChange} placeholder="Email" required />
        <input type="text" name="address" value={studentData.address} onChange={handleChange} placeholder="Address" required />
        <input type="text" name="phone" value={studentData.phone} onChange={handleChange} placeholder="Phone" required />
        <input type="text" name="career" value={studentData.career} onChange={handleChange} placeholder="Career" required />
        <input type="number" name="subject_repeats" value={studentData.subject_repeats} onChange={handleChange} placeholder="Subject Repeats" required />
        <button type="submit">Add Student</button>
      </form>
    </div>
  );
};

export default StudentForm;
