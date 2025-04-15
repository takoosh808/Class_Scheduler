import React, {useState, useEffect} from 'react'
import './ClassSearch.css'
import axios from 'axios';

const ClassSearch = () => {

  const [searchInput, setSearchInput] = useState("");
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/courses/")
      .then((response) => {
        setCourses(response.data);
      })
      .catch((error) => {
        console.error("Error fetching courses:", error);
      });
  }, []);


  const handleChange = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value);
  };

  const filteredCourses = searchInput.length > 0
    ? courses.filter(course =>
        course.class_name.toLowerCase().includes(searchInput.toLowerCase())
      )
    : courses;

  return (<div>

    <input
      type="search"
      placeholder="Search here"
      className="input"
      onChange={handleChange}
      value={searchInput} 
      />
    <table className="searchWrapper">
        <tr className = "title">
            <th>Course Name</th>
            <th>SLN</th>
            <th>Time</th>
            <th>Date</th>
        </tr>
        {filteredCourses.map((course, index) => (
        <tr key={index} className="result">
          <td>{course.class_name}</td>
          <td>{course.id_number}</td>
          <td>{course.time}</td>
          <td>{course.date}</td>
        </tr>
        ))}
    </table>
    </div>)


}

export default ClassSearch