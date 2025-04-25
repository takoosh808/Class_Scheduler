import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MyCourses = () => {
  const [courses, setCourses] = useState([]);
  const studentId = localStorage.getItem("student_id");

  useEffect(() => {
    if (!studentId) return;

    axios.get(`http://localhost:8000/api/enrolled/${studentId}/`)
      .then(res => setCourses(res.data.enrolled_courses || []))
      .catch(err => console.error("Error loading enrolled courses", err));
  }, [studentId]);

  return (
    <div style={{ marginLeft: '300px', marginTop: '20px' }}>
      <h2>My Courses</h2>
      {courses.length === 0 ? (
        <p>You have not enrolled in any courses yet.</p>
      ) : (
        <table className="cartWrapper">
          <thead>
            <tr className="title">
              <th>Course</th>
              <th>SLN</th>
              <th>Instructor</th>
              <th>Time</th>
              <th>Date</th>
              <th>Location</th>
            </tr>
          </thead>
          <tbody>
            {courses.map((course, index) => (
              <tr key={index} className="result">
                <td>{course.class_name}</td>
                <td>{course.id_number}</td>
                <td>{course.instructor}</td>
                <td>{course.time}</td>
                <td>{course.date}</td>
                <td>{course.location}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default MyCourses;
