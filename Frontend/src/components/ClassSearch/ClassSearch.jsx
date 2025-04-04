import React, {useState} from 'react'
import './ClassSearch.css'

const ClassSearch = () => {

 const [searchInput, setSearchInput] = useState("");

 const courses = [
  {name: "Cpts322"},
];

const handleChange = (e) => {
  e.preventDefault();
  setSearchInput(e.target.value);
};

if (searchInput.length > 0) {
    courses.filter((course) => {
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
<input
  type ="submit"
  value = "Submit"
/>
{/* <table>
  <tr>
    <th>Course</th>
  </tr>

{courses.map((course, index) => {

<div>
  <tr>
    <td>{course.name}</td>
  </tr>
</div>

})}
</table> */}

</div>)


}

export default ClassSearch