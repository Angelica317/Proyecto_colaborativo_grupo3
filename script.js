async function loadCourses() {
  try {
    const response = await fetch("http://127.0.0.1:5000/courses");
    const data = await response.json();
    const list = document.getElementById("courses-list");
    list.innerHTML = "";
    data.forEach(course => {
      const item = document.createElement("li");
      item.textContent = `${course.name} - Duración: ${course.duration}`;
      list.appendChild(item);
    });
  } catch (error) {
    console.error("Error cargando cursos:", error);
  }
}

loadCourses();
