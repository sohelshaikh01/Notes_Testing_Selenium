# Selenium – Automate Testing - 27-07-2026

> Started from PPT Page 33

**Selenium** is an interface that interacts with a browser to execute Selenium commands.

- Can be used with multiple programming languages.
- Commands are called **Selenese**.

## How it Works ? ( All Below are Components)

It automates manual testing by running the same tests again and again.

---

# Selenium IDE

- Creates scripts based on your browser actions.
- Example: Records actions while creating or using web applications.
- **Not commonly used at present.**

---

# Selenium RC (Remote Control)

- **Deprecated from Selenium 4 onwards.**
- Earlier acted as a mediator between Selenium and the browser.
- Allowed communication despite browser limitations.
- Selenium WebDriver components replaced Selenium RC.

---

# Selenium Grid

- Helps in achieving **parallel execution** of test cases.

---

# Selenium WebDriver (Most Important Component)

Selenium communicates with all browsers using the **W3C WebDriver Protocol**.

### Flow

```
Selenium Script (Client)
        ↓
W3C WebDriver Protocol
        ↓
Browser Driver (Server)
        ↓
HTTP Communication
        ↓
Real Browser
```

Example:
- **GeckoDriver** (Firefox Driver)

---

    `SearchContext` is the parent interface of **WebDriver**.

    WEBDRIVER ARCHITECTURE (Diagram at PPT Page 44) 


## Selenium vs Playwright

- Selenium
- Playwright (Modern Framework by Microsoft)

---

# Finding Locators

## Locator Types

### ID Locator
- Fastest locator to find an element.
- Uses a unique **id** attribute.

### Other Locators

- Name
- ClassName
- Tag Name
- Link Text
- Partial Link Text

---

### Print all links present on a page

Possible approaches:
- CSS Locator
- XPath Locator

---

# XPath

## Relative XPath

Example:  
    
    `xpath //h1`

- Starts searching from anywhere in the DOM.
- Begins with `//`.


## Absolute XPath

Example path:

    html
    └── body
        └── h1

Example:

    /html/body/h1


- Starts from the root element.
- Begins with `/`.
- Complete path from the root.

---

## Why Relative XPath is Used Most of the Time

- Real-world applications have deep nesting.
- HTML structure changes frequently.
- Relative XPath adapts better to code changes.

---

# Relative vs Absolute Path

    Relative Path => //

    Absolute Path => /

---

## Relative XPath is Better

Instead of using an absolute path, use attributes.

Example:

    //textarea[@name='q']


Where:

- `textarea` → Tag
- `name` → Attribute
- `q` → Attribute Value

---