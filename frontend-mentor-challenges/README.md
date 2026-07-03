# 🎓 Frontend Mentor

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Frontend Mentor](https://img.shields.io/badge/Frontend_Mentor-Practice-blueviolet?style=for-the-badge&logo=frontendmentor&logoColor=white)

## 🏫 Academic Context
**Student Status:** Computer Science (L2 Student)  
**Subject:** UI/UX Implementation & Visual Fidelity  
**Objective:** I build the logic from scratch, these challenges train my eye to read professional Figma designs and translate visual spacing, typography, and layouts into exact CSS properties.

---

## 📖 Project Overview
A collection of solutions for Frontend Mentor challenges. This repository focuses strictly on **Visual Accuracy** and **Responsive Behavior**, serving as a practical lab to test if my CSS skills can match professional design standards.

---

## 🧠 Key Concepts Learned

### 1. The "Pixel-Perfect" Logic
*   **Visual Deconstruction:** Learning to look at a design and automatically break it down into Flexbox containers or Grid areas, rather than guessing.
*   **The Box Model in Practice:** Realizing that in professional designs, `padding` is often used inside the component itself, while `margin` (specifically `gap` in Grid/Flex) is used to separate components from each other.

### 2. Responsive Breakpoints Strategy
*   **Mobile-First Reality:** Writing the mobile layout as the default CSS, then using `@media (min-width: 768px)` strictly to *add* or *rearrange* elements for desktop, rather than rewriting the CSS.
*   **Fluid Images:** Discovering that `max-width: 100%; height: auto;` is the magic spell to prevent images from breaking out of their containers on smaller screens.

### 3. Handling Design Assets
*   **Asset Optimization:** Learning to use the exact image dimensions provided (e.g., `image-mobile.jpg` vs `image-desktop.jpg`) and toggling their visibility using CSS media queries instead of letting the browser resize one huge image.

---

## 🛠️ Problem-Solving Log
*(Instead of a generic syntax table, I use this space to document specific visual bugs I faced and how I fixed them)*

| The Visual Bug | The Root Cause | The CSS Fix Applied |
| :--- | :--- | :--- |
| **Card extending beyond screen on mobile** | Used fixed `width: 400px` instead of relative sizing. | Changed to `width: 90%; max-width: 400px;` to make it fluid. |
| **Images looking stretched/squished** | Forced height without maintaining aspect ratio. | Removed fixed height and used `object-fit: cover;`. |
| **Flex items not centering vertically** | Forgot to set height on the parent container. | Added `min-height: 100vh` to the parent flex container. |
| **Desktop layout breaking on medium tablets** | Only wrote CSS for mobile and large desktop. | Added an intermediate `@media (min-width: 768px)` query. |

---