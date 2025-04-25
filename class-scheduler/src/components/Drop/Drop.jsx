import React, { useState, useEffect } from 'react';
import axios from 'axios';
import "../../assets/css/variables.css";

const EnrolledCourses = () => {
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  const [selectedCourses, setSelectedCourses] = useState([]);
  const studentId = localStorage.getItem('student_id');  // Assuming you're storing student id

  useEffect(() => {
    if (studentId) {
      axios.get(`http://localhost:8000/api/enrolled/${studentId}/`)
        .then(response => {
          setEnrolledCourses(response.data.enrolled_courses || []);
        })
        .catch(error => {
          console.error('Error loading enrolled courses:', error);
        });
    }
  }, [studentId]);

  const handleCheckboxChange = (courseId) => {
    if (selectedCourses.includes(courseId)) {
      setSelectedCourses(selectedCourses.filter(id => id !== courseId));
    } else {
      setSelectedCourses([...selectedCourses, courseId]);
    }
  };

  const handleDropSelected = () => {
    if (selectedCourses.length === 0) {
      alert('Please select at least one course to drop.');
      return;
    }

    const remainingCourses = enrolledCourses.length - selectedCourses.length;

    if (remainingCourses < 1) {
      alert('You must remain enrolled in at least one course.');
      return;
    }


    axios.post('http://localhost:8000/api/drop/', {
      student_id: studentId,
      course_ids: selectedCourses
    })
    .then(response => {
      console.log(response.data);
      alert(`Dropped: ${response.data.dropped_courses.join(", ")}`);

      // Refresh enrolled courses after dropping
      return axios.get(`http://localhost:8000/api/enrolled/${studentId}/`);
    })
    .then(response => {
      setEnrolledCourses(response.data.enrolled_courses || []);
      setSelectedCourses([]);
    })
    .catch(error => {
      console.error('Error dropping courses:', error);
    });
  };

  return (
    <div style={{ marginLeft: "300px", marginTop: "20px", width: "875px", padding: "20px" }}>
      <h2 style = {{backgroundColor: "var(--button-primary)"}}>Enrolled Courses</h2>
      {enrolledCourses.length === 0 ? (
        <p>You are not enrolled in any courses.</p>
      ) : (
        <form>
          {enrolledCourses.map((course, index) => (
            <div key={index}>
              <label>
                <input
                  type="checkbox"
                  value={course.id_number}
                  onChange={() => handleCheckboxChange(course.id_number)}
                  checked={selectedCourses.includes(course.id_number)}
                />
                {course.class_name} (SLN: {course.id_number})
              </label>
            </div>
          ))}
          <br />
          <button type="button" onClick={handleDropSelected}>
            Drop Selected Courses
          </button>
        </form>
      )}
    </div>
  );
};

export default EnrolledCourses;