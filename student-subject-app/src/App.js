import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import StudentList from './components/StudentList';
import StudentForm from './components/StudentForm';
import SubjectForm from './components/SubjectForm';
import AssignSubjects from './components/AssignSubjects';
import StudentDetails from './components/StudentDetails';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/students/:id" element={<StudentDetails />} />
        <Route path="/students" element={<StudentList />} />
        <Route path="/add-student" element={<StudentForm />} />
        <Route path="/add-subject" element={<SubjectForm />} />
        <Route path="/assign-subjects" element={<AssignSubjects />} />
      </Routes>
    </Router>
  );
};

export default App;
