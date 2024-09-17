### React Flow Node-based Pipeline UI with FastAPI Backend

React Flow Node-based Pipeline UI with FastAPI Backend
=============================================

This project is a drag-and-drop pipeline UI built using React, ReactFlow, and Zustand for state management on the frontend, integrated with a FastAPI backend. The UI allows users to create customizable pipeline flows by using node-based interfaces such as inputs, LLM nodes, and outputs.

Table of Contents
-----------------

- [React Flow Node-based UI with FastAPI Backend](#react-flow-node-based-ui-with-fastapi-backend)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Features](#features)
  - [Technologies](#technologies)
    - [Frontend:](#frontend)
    - [Backend:](#backend)
  - [How to Run](#how-to-run)
    - [Frontend:](#frontend-1)
    - [Backend:](#backend-1)
  - [Node Abstraction](#node-abstraction)
  - [Text Node Logic](#text-node-logic)
  - [Styling](#styling)
  - [Backend Integration](#backend-integration)
  - [Concurrently Usage](#concurrently-usage)
  - [Contributing](#contributing)
  - [Developer Info](#developer-info)
  - [License](#license)

Installation
------------

Clone the repository:

    git clone https://github.com/aditya2131/ReactFlow_Node-based-Pipeline-UI.git

Navigate to the project directory:

    cd your-repo-name

Install dependencies for both frontend and backend:

    
    npm install
    cd backend
    pip install uvicorn fastapi pydantic
    

Start the development servers:

    npm run dev

This command will run both the frontend React app and the FastAPI backend concurrently.

Features
--------

*   Custom Nodes: Includes five different types of nodes—Input, LLM, Output, Text, and more recently added CustomNode, CalculationNode, FilterNode, MergeNode, and TransformNode.
*   Backend Integration: Powered by FastAPI, the backend handles the API logic, including handling pipeline data from the React UI.
*   Dynamic Text Node Logic: Supports dynamic text input with JavaScript variable interpolation (e.g., {{ input }}).
*   Styled Components: All components are styled using styled-components for modular and flexible design.
*   Zustand State Management: Manages the application's state, including the nodes, edges, and connections between them.

Technologies
------------

### Frontend:

*   React
*   ReactFlow
*   Zustand
*   Styled-components
*   Poppins Font

### Backend:

*   FastAPI
*   Uvicorn

How to Run
----------

### Frontend:

The frontend is built using React and ReactFlow for the drag-and-drop interface.  
To run the frontend, simply execute:

    npm start

### Backend:

The FastAPI server runs the backend logic, listening for requests from the frontend.  
To run the backend:

    
    cd backend
    uvicorn main:app --reload
    

The frontend communicates with the backend using API calls.

Node Abstraction
----------------

This project includes various types of nodes such as InputNode, OutputNode, LLMNode, and more:

*   *InputNode:* Defines the type and name of input fields.
*   *OutputNode:* Allows you to select different output formats (text or file).
*   *LLMNode:* Represents large language model components.
*   *TextNode:* Dynamically changes based on user input and supports variables like {{ input }}.
*   *CustomNode:* Enables creating user-defined nodes for custom logic.
*   *CalculationNode, FilterNode, MergeNode, TransformNode:* These nodes add additional functionality like performing calculations, filtering data, merging nodes, and transforming content.

Text Node Logic
---------------

The Text Node component allows dynamic input with JavaScript-like variable usage ({{ input }}).  
It adjusts its size automatically based on the input provided by the user.  
Handle elements are dynamically generated to connect to other nodes based on the input.

Styling
-------

The UI is styled using styled-components for modularity and reusability.  
The font used throughout the app is Poppins to ensure a modern, clean look.  
Custom styling is applied for each node to maintain consistency.

Backend Integration
-------------------

The FastAPI backend handles all API requests, processing the pipeline data and returning results to the frontend. It manages the logic for parsing the input from various node types and executing the tasks (e.g., calculations, data transformations).

Concurrently Usage
------------------

Concurrently is used to run both the frontend and backend servers simultaneously using a single command:

    npm run dev

This script starts the React development server and the FastAPI backend together, streamlining the development process.

Contributing
------------

If you'd like to contribute to this project:

*   Fork the repository.
*   Create a new branch for your feature or bugfix.
*   Commit your changes.
*   Push to your branch.
*   Open a Pull Request.

Feel free to reach out for discussions or suggestions.

Developer Info
--------------

# Aditya Mishra

*   GitHub: [github.com/adityamishra2131](https://github.com/aditya2131)
*   LinkedIn: [linkedin.com/in/aditya-mishra-6k](https://linkedin.com/in/aditya-mishra-6k)
  # Akshay Srivastava

*   GitHub: [github.com/aksh10207](https://github.com/aksh10207)
*   LinkedIn: [linkedin.com/in/akshay-07ak](https://linkedin.com/in/akshay-07ak)

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.
