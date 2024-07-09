import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/api/students';

export const getStudents = (skip = 0, limit = 10) => axios.get(`${BASE_URL}?skip=${skip}&limit=${limit}`);
export const getStudentDetails = (studentId) => axios.get(`${BASE_URL}/${studentId}`);
export const addStudent = (studentData) => axios.post(BASE_URL, studentData);
export const updateStudent = (studentId, studentData) => axios.put(`${BASE_URL}/${studentId}`, studentData);
export const deleteStudent = (studentId) => axios.delete(`${BASE_URL}/${studentId}`);
