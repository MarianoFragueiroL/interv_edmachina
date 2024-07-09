import React, { useState, useEffect } from 'react';
import { getStudentDetails, updateStudent } from '../api/studentAPI';

const StudentDetails = ({ match }) => {
  const [student, setStudent] = useState(null);
  const [editMode, setEditMode] = useState(false);
  const studentId = match.params.id;

  useEffect(() => {
    fetchStudentDetails();
  }, []);

  const fetchStudentDetails = async () => {
    try {
      const response = await getStudentDetails(studentId);
      setStudent(response.data);
    } catch (error) {
      console.error('Error fetching student details:', error);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setStudent({ ...student, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await updateStudent(studentId, student);
      setEditMode(false);
    } catch (error) {
      console.error('Error updating student:', error);
    }
  };

  if (!student) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Student Details</h1>
      {editMode ? (
        <form onSubmit={handleSubmit}>
          <input type="text" name="name" value={student.name} onChange={handleChange} required />
          <input type="email" name="email" value={student.email} onChange={handleChange} required />
          <input type="text" name="address" value={student.address} onChange={handleChange} required />
          <input type="text" name="phone" value={student.phone} onChange={handleChange} required />
          <input type="text" name="career" value={student.career} onChange={handleChange} required />
          <input type="number" name="subject_repeats" value={student.subject_repeats} onChange={handleChange} required />
          <button type="submit">Save</button>
        </form>
      ) : (
        <div>
          <p>Name: {student.name}</p>
          <p>Email: {student.email}</p>
          <p>Address: {student.address}</p>
          <p>Phone: {student.phone}</p>
          <p>Career: {student.career}</p>
          <p>Subject Repeats: {student.subject_repeats}</p>
          <button onClick={() => setEditMode(true)}>Edit</button>
        </div>
      )}
    </div>
  );
};

export default StudentDetails;
