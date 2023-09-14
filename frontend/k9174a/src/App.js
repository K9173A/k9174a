import React from 'react';
import {BrowserRouter} from 'react-router-dom';
import './App.css';
import Header from './components/UI/Header/Header';
import AppRouter from './components/AppRouter';

const App = () => {
    return (
        <div className="App">
            <BrowserRouter>
                <Header/>
                <AppRouter/>
            </BrowserRouter>
        </div>
    );
}

export default App;