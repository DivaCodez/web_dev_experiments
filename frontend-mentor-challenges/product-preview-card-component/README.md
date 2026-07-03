Here is a professional `README.md` file tailored for your GitHub repository, based on the challenge provided and your work.

***

# 📦 Frontend Mentor - Product Preview Card Component

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

## 🏫 Academic Context
**Student:** Computer Science (L2 Student)  
**Project:** Frontend Mentor Challenge  
**Goal:** Practice structuring a responsive card component using HTML5 and CSS3 Flexbox.

---

## 📖 Overview
This is a solution to the [Product Preview Card Component challenge on Frontend Mentor](https://www.frontendmentor.io/challenges/product-preview-card-component-GO7UmttRfa). The challenge focuses on building a responsive product card that looks great on both mobile and desktop devices.

### The Challenge
Users should be able to:
- View the optimal layout for the interface depending on their device's screen size.
- See hover and focus states for all interactive elements on the page.

### Screenshot

[ScreenShot](./ScreenShot.png)

---

## 🚀 My Process

### Built With
- **Semantic HTML5 Markup:** Structuring the content logically.
- **CSS Custom Properties:** Using variables for colors.
- **CSS Flexbox:** Used to align the card in the center of the screen and to position image/text side-by-side.
- **Responsive Design:** Using media queries to switch between desktop and mobile layouts.

### What I Learned
This project was a great opportunity to apply the CSS fundamentals I learned recently sush is dealing with multipe device margins.

**1. Centering with Flexbox:**
I learned how to properly center a container in the middle of the page using Flexbox on the `body` element, instead of using fixed margins.
```css
body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
```

**2. Responsive Layout Strategy:**
I used `flex-direction: row` for desktop to place the image and text side-by-side. For mobile screens, I used a media query to change it to `column`, stacking the image above the text.

```css
/* Mobile Responsive */

```

**3. Box Sizing:**
I learned the importance of `box-sizing: border-box` to handle padding and borders without breaking the layout width.

### Continued Development
In future projects, I want to focus on:
- Using the HTML `<picture>` element to swap images dynamically between desktop and mobile versions instead of just resizing one image.
- Improving accessibility features.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/product-preview-card.git
   ```
2. Open the `index.html` file in your browser.

---

## 🙏 Acknowledgments
- Challenge by [Frontend Mentor](https://www.frontendmentor.io).
- Coded by **DivaCodez** (CS L2 Student).

---

*Built with dedication during my L2 Computer Science curriculum.*