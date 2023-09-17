import React from 'react';
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import About from './pages/About';
import Auth from './pages/Auth';
import Storage from './pages/Storage';
import Profile from './pages/Profile';
import AuthorizedLayout from './layouts/AuthorizedLayout';

const AppRouter = () => {
    // todo: check token -> redirect to /login if not present
    // todo: сделать один эндпоинт auth/ с переключением между компонентами по кнопке login/register
    return (
        <BrowserRouter>
            <Routes>
                <Route path='/' element={<Auth />} exact />
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