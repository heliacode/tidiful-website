# TidiFul Branding & CSS Guide

Complete guide to TidiFul's visual identity, color system, typography, and styling patterns.

---

## 🎨 Color Palette

### Primary Colors (Emerald Green)
The primary brand color represents growth, efficiency, and technology.

| Shade | Hex Code | Tailwind Class | Usage |
|-------|----------|----------------|-------|
| 50 | `#ecfdf5` | `primary-50` | Light backgrounds, subtle highlights |
| 100 | `#d1fae5` | `primary-100` | Very light backgrounds |
| 200 | `#a7f3d0` | `primary-200` | Light accents |
| 300 | `#6ee7b7` | `primary-300` | Soft highlights |
| 400 | `#34d399` | `primary-400` | Hover states, secondary actions |
| **500** | **`#10b981`** | **`primary-500` / `emerald-500`** | **Primary brand color - main CTAs, links, accents** |
| 600 | `#059669` | `primary-600` / `emerald-600` | Buttons, active states |
| 700 | `#047857` | `primary-700` | Darker buttons, emphasis |
| 800 | `#065f46` | `primary-800` | Dark backgrounds, cards |
| 900 | `#064e3b` | `primary-900` | Darkest backgrounds |

**Primary Usage:**
- Main brand color: `#10b981` (emerald-500)
- Buttons: `bg-emerald-600 hover:bg-emerald-500`
- Links: `text-emerald-400 hover:text-emerald-300`
- Accents: `text-emerald-400`, `border-emerald-500`

### Secondary Colors (Cyan Blue)
Used for informational elements, secondary actions, and complementary accents.

| Shade | Hex Code | Tailwind Class | Usage |
|-------|----------|----------------|-------|
| 50 | `#ecfeff` | `secondary-50` | Light backgrounds |
| 100 | `#cffafe` | `secondary-100` | Very light backgrounds |
| 200 | `#a5f3fc` | `secondary-200` | Light accents |
| 300 | `#67e8f9` | `secondary-300` | Soft highlights |
| 400 | `#22d3ee` | `secondary-400` | Hover states |
| **500** | **`#06b6d4`** | **`secondary-500` / `cyan-500`** | **Secondary brand color - info boxes, secondary CTAs** |
| 600 | `#0891b2` | `secondary-600` | Buttons, active states |
| 700 | `#0e7490` | `secondary-700` | Darker buttons |
| 800 | `#155e75` | `secondary-800` | Dark backgrounds |
| 900 | `#164e63` | `secondary-900` | Darkest backgrounds |

**Secondary Usage:**
- Info boxes: `bg-blue-900/20 border border-blue-500/30`
- Internal links in blog posts: `text-blue-400 hover:text-blue-300`

### Neutral Colors (Gray Scale)
Used for backgrounds, text, and UI elements.

| Shade | Hex Code | Tailwind Class | Usage |
|-------|----------|----------------|-------|
| 100 | `#f3f4f6` | `gray-100` | Light backgrounds (email templates) |
| 200 | `#e5e7eb` | `gray-200` | Light borders |
| 300 | `#d1d5db` | `gray-300` | Body text, secondary text |
| 400 | `#9ca3af` | `gray-400` | Muted text, links |
| 500 | `#6b7280` | `gray-500` | Placeholder text |
| 600 | `#4b5563` | `gray-600` | Borders, dividers |
| 700 | `#374151` | `gray-700` | Cards, elevated surfaces |
| 800 | `#1f2937` | `gray-800` | Dark cards, content areas |
| 900 | `#111827` | `gray-900` | Navigation, headers |
| Background | `#161616` | Custom | Main page background |

**Neutral Usage:**
- Page background: `#161616` (custom dark)
- Navigation: `bg-gray-900`
- Cards: `bg-gray-800` or `bg-gray-700`
- Text (headings): `text-gray-100`
- Text (body): `text-gray-300`
- Text (muted): `text-gray-400`
- Borders: `border-gray-700` or `border-gray-600`

---

## 🎯 Tailwind Configuration

All pages use Tailwind CSS with a custom configuration. Include this in your HTML:

```html
<script src="https://cdn.tailwindcss.com"></script>
<script>
    tailwind.config = {
        darkMode: 'class',
        theme: {
            extend: {
                colors: {
                    primary: {
                        50: '#ecfdf5',
                        100: '#d1fae5',
                        200: '#a7f3d0',
                        300: '#6ee7b7',
                        400: '#34d399',
                        500: '#10b981',
                        600: '#059669',
                        700: '#047857',
                        800: '#065f46',
                        900: '#064e3b',
                    },
                    secondary: {
                        50: '#ecfeff',
                        100: '#cffafe',
                        200: '#a5f3fc',
                        300: '#67e8f9',
                        400: '#22d3ee',
                        500: '#06b6d4',
                        600: '#0891b2',
                        700: '#0e7490',
                        800: '#155e75',
                        900: '#164e63',
                    }
                }
            }
        }
    }
</script>
```

**Important:** Always set `darkMode: 'class'` and add `class="dark"` to the `<html>` tag.

---

## 📝 Typography

### Font System
- **Primary Font**: System fonts (sans-serif stack)
- **Code Font**: `'Monaco', 'Consolas', monospace`

### Typography Scale

#### Headings
```css
/* H1 - Page Titles */
.prose h1 {
    font-size: 2.5rem;        /* 40px */
    margin-bottom: 1rem;
    color: #10b981;           /* emerald-500 */
}

/* H2 - Section Titles */
.prose h2 {
    font-size: 1.8rem;         /* 28.8px */
    margin-top: 2rem;
    margin-bottom: 1rem;
    color: #10b981;           /* emerald-500 */
}

/* H3 - Subsection Titles */
.prose h3 {
    font-size: 1.4rem;         /* 22.4px */
    margin-top: 1.5rem;
    margin-bottom: 0.8rem;
    color: #10b981;           /* emerald-500 */
}
```

#### Body Text
```css
.prose p {
    margin-bottom: 1.2rem;
    font-size: 1.1rem;         /* 17.6px */
    line-height: 1.8;
    color: #e5e7eb;            /* gray-200 */
}
```

#### Lists
```css
.prose ul, .prose ol {
    margin-bottom: 1.2rem;
    padding-left: 2rem;
}

.prose li {
    margin-bottom: 0.5rem;
    line-height: 1.8;
}
```

#### Code
```css
.prose code {
    background: #374151;        /* gray-700 */
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Monaco', 'Consolas', monospace;
}
```

#### Links
```css
.prose a {
    color: #10b981;            /* emerald-500 */
}

/* Hover state */
.prose a:hover {
    color: #34d399;            /* emerald-400 */
}
```

### Prose Class
Use the `prose` class for content areas. It provides consistent typography:

```html
<div class="prose prose-lg max-w-none">
    <!-- Your content here -->
</div>
```

**Prose Colors:**
- Text: `#e5e7eb` (gray-200)
- Headings: `#10b981` (emerald-500)
- Links: `#10b981` (emerald-500)

---

## 🎨 Custom CSS Classes

### Core Styles

#### Body Background
```css
body {
    background: #161616;
}
```

#### Text Gradient
Used for highlighting important text in headings:

```css
.text-gradient {
    background: linear-gradient(135deg, #10b981, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
```

**Usage:**
```html
<h1>About <span class="text-gradient">TidiFul</span></h1>
```

#### Gradient Background
Used for section backgrounds:

```css
.gradient-bg {
    background: linear-gradient(135deg, #10b981, #059669);
}

/* Alternative gradient (for features page) */
.gradient-bg {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
}
```

### Component Classes

#### Card Hover Effect
Adds smooth hover animation to cards:

```css
.card-hover {
    transition: all 0.3s ease;
}

.card-hover:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}
```

**Usage:**
```html
<div class="bg-gray-800 rounded-2xl p-8 card-hover">
    <!-- Card content -->
</div>
```

#### Feature Card
Special styling for feature cards:

```css
.feature-card {
    transition: all 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 25px -5px rgba(16, 185, 129, 0.1), 
                0 10px 10px -5px rgba(16, 185, 129, 0.04);
}
```

#### Highlight Box
Used for important callouts and CTAs in blog posts:

```css
.highlight-box {
    background: linear-gradient(135deg, #065f46 0%, #047857 100%);
    padding: 30px;
    border-radius: 12px;
    margin: 30px 0;
}
```

**Usage:**
```html
<div class="highlight-box text-white">
    <h3 class="text-emerald-400 font-semibold mb-3">🚀 Try TidiFul Today</h3>
    <p class="text-gray-300 mb-4">Save hours of manual work...</p>
    <a href="https://app.tidiful.com" class="inline-block px-6 py-3 bg-emerald-600 hover:bg-emerald-500 text-white font-medium rounded-lg transition-colors">
        Start Free Trial
    </a>
</div>
```

#### Info Box (Blog Posts)
For informational callouts:

```css
/* Info boxes use Tailwind classes */
.bg-blue-900\/20 {
    background-color: rgba(30, 58, 138, 0.2);
}

.border-blue-500\/30 {
    border-color: rgba(59, 130, 246, 0.3);
}
```

**Usage:**
```html
<div class="bg-blue-900/20 border border-blue-500/30 rounded-lg p-6 my-8">
    <h3 class="text-blue-400 font-semibold mb-3">💡 Pro Tip</h3>
    <p class="text-gray-300">...</p>
</div>
```

#### Step Box
For step-by-step instructions:

```css
.step-box {
    background: #1f2937;        /* gray-800 */
    padding: 20px;
    border-radius: 8px;
    border: 1px solid #374151;  /* gray-700 */
    margin: 20px 0;
}
```

#### Upload Area
For drag-and-drop file uploads:

```css
.upload-area {
    transition: all 0.3s ease;
}

.upload-area.dragover {
    border-color: #34d399;     /* emerald-400 */
    box-shadow: 0 0 20px rgba(52, 211, 153, 0.5);
    transform: scale(1.02);
}
```

#### Result Card Animation
For animated result displays:

```css
.result-card {
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.5s ease;
}

.result-card.show {
    opacity: 1;
    transform: translateY(0);
}
```

#### Icon Gradient
For icon backgrounds:

```css
.icon-gradient {
    background: linear-gradient(135deg, #10b981, #059669);
}
```

---

## 🖼️ Logo & Assets

### Logo Files
- **Main Logo**: `assets/images/tidiful_logo.png`
- **Cropped Logo**: `assets/images/tidiful_logo_cropped.png`
- **Leaf Icon (128x128)**: `assets/images/leaf_png_128x128.png`
- **Leaf Icon (256x256)**: `assets/images/leaf_png_256x256.png`
- **Leaf Icon (512x512)**: `assets/images/leaf_png_512x512.png`

### Logo Usage

#### Navigation Logo
```html
<a href="index.html" class="flex items-center space-x-2 hover:opacity-80 transition-opacity">
    <img src="assets/images/leaf_png_128x128.png" 
         alt="TidiFul leaf logo - AI document processing brand" 
         class="h-8 w-auto">
    <span class="text-xl font-bold text-gray-100">TidiFul</span>
</a>
```

#### Favicon
```html
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="assets/images/leaf_png_128x128.png">
<link rel="icon" type="image/png" sizes="128x128" href="assets/images/leaf_png_128x128.png">
<link rel="icon" type="image/png" sizes="256x256" href="assets/images/leaf_png_256x256.png">
<link rel="apple-touch-icon" sizes="180x180" href="assets/images/leaf_png_256x256.png">
```

---

## 🎭 Design Patterns

### Navigation
```html
<nav class="border-b border-gray-700 bg-gray-900 backdrop-blur-sm">
    <div class="container mx-auto px-4 py-4">
        <!-- Navigation content -->
    </div>
</nav>
```

**Link Styles:**
- Default: `text-gray-300`
- Hover: `hover:text-emerald-400`
- Active: `text-emerald-400 font-medium`
- Transition: `transition-colors`

### Buttons

#### Primary Button
```html
<a href="#" class="px-8 py-3 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-lg font-medium transition-colors text-white">
    Start Free Trial
</a>
```

#### Secondary Button (Outlined)
```html
<button class="px-6 py-2 border border-emerald-500 text-emerald-400 hover:bg-emerald-900 rounded-lg transition-colors">
    Learn More
</button>
```

#### Ghost Button
```html
<button class="px-4 py-2 text-gray-400 hover:text-gray-300 transition-colors">
    Cancel
</button>
```

### Cards

#### Standard Card
```html
<div class="bg-gray-800 rounded-2xl p-8 card-hover">
    <!-- Card content -->
</div>
```

#### Feature Card
```html
<div class="feature-card bg-gray-800 rounded-2xl p-8">
    <div class="w-12 h-12 rounded-lg bg-emerald-900 flex items-center justify-center mb-4">
        <i data-feather="zap" class="w-6 h-6 text-emerald-400"></i>
    </div>
    <h3 class="text-xl font-bold mb-2 text-gray-100">Feature Title</h3>
    <p class="text-gray-300">Feature description...</p>
</div>
```

### Forms

#### Input Fields
```html
<input type="text" 
       class="w-full px-4 py-2 bg-gray-800 border border-gray-600 rounded-lg text-gray-100 focus:outline-none focus:border-emerald-400">
```

#### Select Dropdowns
```html
<select class="px-4 py-2 bg-gray-800 border border-gray-600 rounded-lg text-gray-100 text-sm focus:outline-none focus:border-emerald-400 hover:bg-gray-700 transition-all duration-200">
    <option>Option 1</option>
</select>
```

### Spacing System
TidiFul uses Tailwind's spacing scale:
- **Container**: `container mx-auto px-4`
- **Section Padding**: `py-16` or `py-24`
- **Card Padding**: `p-8` or `p-6`
- **Gap Between Elements**: `space-x-8`, `space-y-4`, etc.

### Border Radius
- **Small**: `rounded-lg` (8px)
- **Medium**: `rounded-xl` (12px)
- **Large**: `rounded-2xl` (16px)
- **Full**: `rounded-full` (for circles)

---

## 🌐 Email Templates

For email templates, use a lighter color palette:

- **Primary Green**: `#10b981` (emerald-500)
- **Dark Green**: `#059669` (emerald-600)
- **Light Green**: `#ecfdf5` (emerald-50)
- **Text Dark**: `#1f2937` (gray-800)
- **Text Medium**: `#4b5563` (gray-600)
- **Text Light**: `#6b7280` (gray-500)
- **Background**: `#f5f5f5` (gray-100)
- **White**: `#ffffff`

**Important:** All CSS in emails must be inline for maximum compatibility.

---

## 🎯 Usage Guidelines

### Color Usage Rules

1. **Primary Green (`#10b981`)**:
   - Main CTAs and buttons
   - Links and interactive elements
   - Brand accents and highlights
   - Icons and illustrations

2. **Secondary Cyan (`#06b6d4`)**:
   - Informational callouts
   - Secondary actions
   - Complementary accents

3. **Gray Scale**:
   - Backgrounds: Use dark grays (`gray-800`, `gray-900`, `#161616`)
   - Text: Use light grays (`gray-100`, `gray-300`, `gray-400`)
   - Borders: Use medium grays (`gray-600`, `gray-700`)

### Typography Rules

1. **Headings**: Always use emerald-500 (`#10b981`) for H1, H2, H3
2. **Body Text**: Use gray-200 (`#e5e7eb`) or gray-300 (`#d1d5db`)
3. **Links**: Use emerald-400 (`#34d399`) with emerald-300 hover
4. **Code**: Use gray-700 background with system monospace font

### Component Rules

1. **Cards**: Always use `rounded-2xl` for consistency
2. **Buttons**: Use `transition-colors` for smooth hover effects
3. **Hover States**: Always provide visual feedback (color change, transform)
4. **Spacing**: Use consistent padding (`p-8` for cards, `py-16` for sections)

---

## 📦 Complete CSS Reference

Here's a complete CSS file you can reference:

```css
/* ============================================
   TIDIFUL BRANDING CSS
   ============================================ */

/* Base Styles */
body {
    background: #161616;
}

/* Typography */
.prose {
    color: #e5e7eb;
}

.prose h1, .prose h2, .prose h3 {
    color: #10b981;
}

.prose h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.prose h2 {
    font-size: 1.8rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

.prose h3 {
    font-size: 1.4rem;
    margin-top: 1.5rem;
    margin-bottom: 0.8rem;
}

.prose p {
    margin-bottom: 1.2rem;
    font-size: 1.1rem;
    line-height: 1.8;
}

.prose ul, .prose ol {
    margin-bottom: 1.2rem;
    padding-left: 2rem;
}

.prose li {
    margin-bottom: 0.5rem;
    line-height: 1.8;
}

.prose code {
    background: #374151;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Monaco', 'Consolas', monospace;
}

.prose a {
    color: #10b981;
}

.prose a:hover {
    color: #34d399;
}

/* Text Gradient */
.text-gradient {
    background: linear-gradient(135deg, #10b981, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* Gradient Backgrounds */
.gradient-bg {
    background: linear-gradient(135deg, #10b981, #059669);
}

.icon-gradient {
    background: linear-gradient(135deg, #10b981, #059669);
}

/* Card Hover Effects */
.card-hover {
    transition: all 0.3s ease;
}

.card-hover:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

.feature-card {
    transition: all 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 25px -5px rgba(16, 185, 129, 0.1), 
                0 10px 10px -5px rgba(16, 185, 129, 0.04);
}

/* Content Boxes */
.highlight-box {
    background: linear-gradient(135deg, #065f46 0%, #047857 100%);
    padding: 30px;
    border-radius: 12px;
    margin: 30px 0;
}

.step-box {
    background: #1f2937;
    padding: 20px;
    border-radius: 8px;
    border: 1px solid #374151;
    margin: 20px 0;
}

.highlight {
    background: #065f46;
    padding: 20px;
    border-radius: 8px;
    border-left: 4px solid #10b981;
    margin: 20px 0;
}

/* Upload Area */
.upload-area {
    transition: all 0.3s ease;
}

.upload-area.dragover {
    border-color: #34d399;
    box-shadow: 0 0 20px rgba(52, 211, 153, 0.5);
    transform: scale(1.02);
}

/* Result Card Animation */
.result-card {
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.5s ease;
}

.result-card.show {
    opacity: 1;
    transform: translateY(0);
}
```

---

## 🔗 Related Resources

- **Tailwind CSS**: https://tailwindcss.com
- **Feather Icons**: https://feathericons.com
- **Logo Assets**: `assets/images/`
- **Email Templates**: `templates/`

---

## 📝 Notes

- All pages use **dark mode** by default (`class="dark"` on `<html>`)
- Tailwind is loaded via CDN in all pages
- Custom styles are defined inline in `<style>` tags
- All transitions use `transition-colors` or `transition-all` for smooth animations
- Icons use Feather Icons library (`data-feather` attributes)

---

**Last Updated:** January 2025  
**Maintained by:** TidiFul Team

