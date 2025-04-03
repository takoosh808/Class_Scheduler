import React, {useState} from 'react'
import './ClassSearch.css'

const ClassSearch = () => {

  const [searchInput, setSearchInput] = useState("");

  const Courses = [
    {name: "Cpts322", id_number: "1000", date:"TTH", time:"4:10"},
    {name: "Cpts321", id_number: "1001",date:"MWF", time:"12:10"},
    {name: "Chem101", id_number: "2356",date:"MWF", time:"11:10"},
    {name: "Chem105", id_number: "2045",date:"TTH", time:"12:10"},
    {name: "Bio106", id_number: "3567",date:"MWF", time:"3:10"},
  ];

  var activeItems = [];

  const handleChange = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value);
  };

  if (searchInput.length > 0) {
      activeItems = Courses.filter((course) => {
      return course.name.match(searchInput);
  });
  }

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
        {activeItems.map((course, index) => (
        <tr key={index} className="result">
          <td>{course.name}</td>
          <td>{course.id_number}</td>
          <td>{course.time}</td>
          <td>{course.date}</td>
        </tr>
        ))}
    </table>
    </div>)


}

export default ClassSearch