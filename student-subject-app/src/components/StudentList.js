import React, { useState, useEffect } from 'react';
import { NavLink } from 'react-router-dom';
import { getStudents, deleteStudent } from '../api/studentAPI';

const StudentList = () => {
  const [students, setStudents] = useState([]);
  const [skip, setSkip] = useState(0);
  const [limit] = useState(10);

  useEffect(() => {
    fetchStudents();
  }, [skip]);

  const fetchStudents = async () => {
    try {
      const response = await getStudents(skip, limit);
      setStudents(response.data);
    } catch (error) {
      console.error('Error fetching students:', error);
    }
  };

  const handleDelete = async (studentId) => {
    try {
      await deleteStudent(studentId);
      fetchStudents();
    } catch (error) {
      console.error('Error deleting student:', error);
    }
  };

  return (
    <div>
      <h1>Student List</h1>
      <ul>
        {students.map(student => (
          <li key={student.id}>
            <NavLink to={`/students/${student.id}`}>{student.name}</NavLink>
            <button onClick={() => handleDelete(student.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <button onClick={() => setSkip(skip - limit)} disabled={skip === 0}>Previous</button>
      <button onClick={() => setSkip(skip + limit)}>Next</button>
    </div>
  );
};

export default StudentList;
