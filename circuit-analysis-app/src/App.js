import React, { useState } from 'react';
import './App.css';
import { Drawer, List, ListItem, ListItemText, ThemeProvider, CssBaseline, createTheme } from '@mui/material';

function App() {
  // State for which component is currently selected
  const [selectedComponent, setSelectedComponent] = useState(null);

  // State to track components placed on the canvas
  const [componentsOnCanvas, setComponentsOnCanvas] = useState([]);

  return (
    <ThemeProvider theme={createTheme()}>
      <CssBaseline />

      <Drawer
        variant="permanent"
        open={true}
      >
        <List>
          {['Resistor', 'Voltage Source', 'Current Source', 'Wires'].map((text) => (
            <ListItem 
              button 
              key={text} 
              onClick={() => setSelectedComponent(text)}
            >
              <ListItemText primary={text} />
            </ListItem>
          ))}
        </List>
      </Drawer>

      <div 
        style={{ marginLeft: '240px', height: '100vh', border: '1px solid gray' }}
        onClick={(e) => {
          if (selectedComponent) {
            // For now, just store the component and its position
            setComponentsOnCanvas([
              ...componentsOnCanvas,
              {
                component: selectedComponent,
                x: e.clientX,
                y: e.clientY
              }
            ]);

            // Deselect the component after placing it
            setSelectedComponent(null);
          }
        }}
      >
        {componentsOnCanvas.map((comp, index) => (
          <div 
            key={index} 
            style={{ position: 'absolute', top: comp.y, left: comp.x }}
          >
            {comp.component}
          </div>
        ))}
      </div>
      
    </ThemeProvider>
  );
}

export default App;
