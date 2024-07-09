import React, { useState, useEffect } from 'react';
import { getStudents, updateStudent } from '../api/studentAPI';
import { getSubjects } from '../api/subjectAPI';

const AssignSubjects = () => {
  const [students, setStudents] = useState([]);
  const [subjects, setSubjects] = useState([]);
  const [selectedStudent, setSelectedStudent] = useState('');
  const [selectedSubjects, setSelectedSubjects] = useState([]);

  useEffect(() => {
    fetchStudents();
    fetchSubjects();
  }, []);

  const fetchStudents = async () => {
    try {
      const response = await getStudents();
      setStudents(response.data);
    } catch (error) {
      console.error('Error fetching students:', error);
    }
  };

  const fetchSubjects = async () => {
    try {
      const response = await getSubjects();
      setSubjects(response.data);
    } catch (error) {
      console.error('Error fetching subjects:', error);
    }
  };

  const handleAssign = async () => {
    try {
      await updateStudent(selectedStudent, { subjects: selectedSubjects });
      setSelectedStudent('');
      setSelectedSubjects([]);
    } catch (error) {
      console.error('Error assigning subjects:', error);
    }
  };

  return (
    <div>
      <h1>Assign Subjects</h1>
      <select onChange={(e) => setSelectedStudent(e.target.value)} value={selectedStudent}>
        <option value="">Select Student</option>
        {students.map(student => (
          <option key={student.id} value={student.id}>{student.name}</option>
        ))}
      </select>
      <div>
        {subjects.map(subject => (
          <label key={subject.id}>
            <input
              type="checkbox"
              value={subject.id}
              checked={selectedSubjects.includes(subject.id)}
              onChange={(e) => {
                const subjectId = e.target.value;
                setSelectedSubjects(prev => 
                  prev.includes(subjectId)
                    ? prev.filter(id => id !== subjectId)
                    : [...prev, subjectId]
                );
              }}
            />
            {subject.name}
          </label>
        ))}
      </div>
      <button onClick={handleAssign}>Assign Subjects</button>
    </div>
  );
};

export default AssignSubjects;
