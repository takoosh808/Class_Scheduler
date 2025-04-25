import React, {useState, useEffect} from 'react'
import './ClassSearch.css'
import axios from 'axios';

const ClassSearch = () => {

  const [searchInput, setSearchInput] = useState("");
  const [courses, setCourses] = useState([]);
  const [searchField, setSearchField] = useState('class_name');

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

  const handleAddToCart = (courseId) => {
    const studentId = localStorage.getItem("student_id");
  
    if (!studentId) {
      alert("You must be logged in to add courses.");
      return;
    }
    axios.post("http://127.0.0.1:8000/api/cart/add/", {
      student_id: studentId,
      course_id: courseId,
    })
    .then((response) => {
      alert("Course added to cart!");
    })
    .catch((error) => {
      console.error("Error adding to cart:", error);
      alert("Failed to add course to cart.");
    });
  };

  const handleSearchFieldChange = (e) => {
    setSearchField(e.target.value);
  };

  const filteredCourses = courses.filter(course => {
    if (!searchInput) return true;
    const fieldValue = course[searchField];
    if (fieldValue) {
      return fieldValue.toLowerCase().includes(searchInput.toLowerCase());
    }
    return false;
  });

  return (<div className = "searchBody">

      <div className="searchInputs">
        <select value={searchField} onChange={handleSearchFieldChange} className="input">
          <option value="class_name">Course Name</option>
          <option value="Time">Time</option>
          <option value="Date">Date</option>
          <option value="Instructor">Instructor</option>
          <option value="Location">Location</option>
        </select>

        <input
          type="text"
          placeholder={`Search by ${searchField.replace('_', ' ')}`}
          value={searchInput}
          onChange={handleChange}
          className="input"
        />
      </div>


    <table className="searchWrapper">
        <tr className = "title">
            <th>Course Name</th>
            <th>Section Number</th>
            <th>Instructor</th>
            <th>Location</th>
            <th>SLN</th>
            <th>Time</th>
            <th>Date</th>
        </tr>
        {filteredCourses.map((course, index) => (
        <tr key={index} className="result">
          <td>{course.class_name}</td>
          <td>{course.Section_Number}</td>
          <td>{course.Instructor}</td>
          <td>{course.Location}</td>
          <td>{course.id_number}</td>
          <td>{course.Time}</td>
          <td>{course.Date}</td>
          <td>
          <button onClick={() => handleAddToCart(course.id_number)}>Add to Cart</button>
          </td>
        </tr>
        ))}
    </table>
    </div>)


}

export default ClassSearch