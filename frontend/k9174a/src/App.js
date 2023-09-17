import React from 'react';
import {ThemeProvider} from '@mui/material';
import AppRouter from './ui/AppRouter';
import theme from './theme';
import './App.css';

const App = () => {
    return (
        <ThemeProvider theme={theme}>
            <div className="App">
                <AppRouter />
            </div>
        </ThemeProvider>
    );
}

export default App;