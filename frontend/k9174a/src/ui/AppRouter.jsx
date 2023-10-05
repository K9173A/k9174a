import React from 'react';
import {BrowserRouter, Navigate, Route, Routes} from 'react-router-dom';
import About from './pages/About';
import Login from './pages/Login';
import Register from './pages/Register';
import Storage from './pages/Storage';
import Profile from './pages/Profile';
import AuthorizedLayout from './layouts/AuthorizedLayout';
import UnauthorizedLayout from './layouts/UnauthorizedLayout';

const AppRouter = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path='/' element={<Navigate replace to='/login' />} exact />
                <Route element={<UnauthorizedLayout />}>
                    <Route path='/login' element={<Login />} exact />
                    <Route path='/register' element={<Register />} exact />
                </Route>
                <Route element={<AuthorizedLayout />}>
                    <Route path='/storage' element={<Storage />} exact />
                    <Route path='/about' element={<About />} exact />
                    <Route path='/profile' element={<Profile />} exact />
                </Route>
            </Routes>
        </BrowserRouter>
    );
};

export default AppRouter;