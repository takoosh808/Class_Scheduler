import React, { useEffect, useState } from "react";
import axios from "axios";
import "./WeeklySchedule.css";

export default function WeeklySchedule() {
  const [schedule, setSchedule] = useState({});
  const studentId = localStorage.getItem("student_id");

  useEffect(() => {
      if (!studentId) return;

      axios.get(`http://localhost:8000/api/schedule/${studentId}/`)
          .then(res => {
              console.log("Schedule response:", res.data);
              setSchedule(res.data.weekly_schedule || {});
          })
          .catch(err => console.log("Unable to fetch schedule.", err));
  }, [studentId]);

  const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];

  // Sort each day's classes by time
  const sortedSchedule = {};
  days.forEach(day => {
      sortedSchedule[day] = (schedule[day] || []).sort((a, b) => a.time - b.time);
  });

  return (
      <div className="schedule-wrapper">
          <h2 className="schedule-title">Weekly Schedule</h2>
          <div className="schedule-grid">
              {days.map(day => (
                  <div key={day} className="schedule-column">
                      <h3>{day}</h3>
                      {sortedSchedule[day] && sortedSchedule[day].length > 0 ? (
                          <ul className="class-list">
                              {sortedSchedule[day].map((cls, index) => (
                                  <li key={index} className="class-card">
                                      <strong>{cls.class_name}</strong><br />
                                      ID: {cls.id_number}<br />
                                      Time: {formatTime(cls.time)}<br />
                                      Location: {cls.location}<br />
                                      Instructor: {cls.instructor}
                                  </li>
                              ))}
                          </ul>
                      ) : (
                          <p className="no-class">No classes</p>
                      )}
                  </div>
              ))}
          </div>
      </div>
  );
}

function formatTime(militaryTime) {
  const hour = Math.floor(militaryTime / 100);
  const minute = militaryTime % 100;
  const ampm = hour >= 12 ? 'PM' : 'AM';
  const hr12 = hour % 12 || 12;
  return `${hr12}:${minute.toString().padStart(2, '0')} ${ampm}`;
}