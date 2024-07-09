import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/api/subjects';

export const getSubjects = (skip = 0, limit = 10) => axios.get(`${BASE_URL}/?skip=${skip}&limit=${limit}`);
export const addSubject = (name) => axios.post(BASE_URL, { name });
export const deleteSubject = (subjectId) => axios.delete(`${BASE_URL}/${subjectId}`);
