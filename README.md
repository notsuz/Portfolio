# 🌌 quietlyodd | Minimalist Portfolio & Dynamic Social Grid

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Inter&weight=900&size=28&duration=3500&pause=1000&color=FFCC33&center=true&vCenter=true&width=600&height=50&lines=Full-Stack+Django+Portfolio;Dynamic+Instagram-Style+Feed;Responsive+Minimalist+Design" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap" />
  <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
</p>

---

### 📝 Project Overview
A sleek, responsive, single-page portfolio web application tailored for a minimalist, cinematic aesthetic. This project bridges a clean Python/Django backend with a highly customized Bootstrap layout, transitioning away from traditional rigid formats into a fluid, media-centric presentation.

The centerpiece is a dynamic **Instagram-style post grid** driven directly by a streamlined Django database model, allowing real-time content updates via the admin dashboard.

---

### ⚡ Key Features

* **Dynamic Card Matrix:** An optimized content grid that counts and pulls posts directly from the database, enforcing a clean `1:1 aspect-ratio` image square with smart text-truncation (`-webkit-line-clamp`) to keep the interface uniform regardless of data length.
* **Aesthetic UI Architecture:** Built on top of a dark theme environment (`#050505`) featuring glassmorphism elements (`backdrop-filter: blur`), subtle gold accents (`#ffcc33`), and a cinematic hero mask fade-out using non-destructive linear CSS masking.
* **Fluid Responsiveness:** Engineered with custom flexbox wrapping, `clamp()` typography scaling, and mobile-first container logic to guarantee flawless execution from desktop screens down to mobile viewports without design breakdown.
* **Streamlined DB Schema:** Optimized `models.py` structural design that holds only vital nodes (User metadata, binary blobs/image uploads, caption blocks, and relative metrics) for efficient server queries.

---

### 🛠️ Technical Stack

* **Backend:** Python, Django Web Framework
* **Frontend:** HTML5, CSS3 (Custom Grid Repair / Masking), Bootstrap 5, FontAwesome Icons
* **Database:** PostgreSQL / SQLite (Development ready)

---

