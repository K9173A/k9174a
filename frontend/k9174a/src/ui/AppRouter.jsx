import React from 'react';
import { useCookies } from 'react-cookie';
import {BrowserRouter, Redirect, Route, Routes} from 'react-router-dom';
import About from './pages/About';
import Login from './pages/Login';
import Register from './pages/Register';
import Storage from './pages/Storage';
import Profile from './pages/Profile';
import AuthorizedLayout from './layouts/AuthorizedLayout';
import UnauthorizedLayout from './layouts/UnauthorizedLayout';

const AppRouter = () => {
    const [cookies, setCookie] = useCookies(['K9174A_TOKEN']);

    // Последовательность проверок:
    // 1. Проверяется наличие куки - если нет, то редирект на страницу логина, а если есть - на страницу стораджа
    // 2. Проверяется правильность пути - если не правильный, то редирект на страницу логина
    // 3. Проверяется

    React.useEffect(() => {
        if (cookies.K9174A_TOKEN) {
            <Redirect to='/storage' />
        } else {
            <Redirect to='/login' />
        }
    }, [cookies.K9174A_TOKEN]);

    return (
        <BrowserRouter>
            <Routes>
                <Route element={<UnauthorizedLayout />}>
                    <Route path='/login' element={<Login />} exact />
                    <Route path='/register' element={<Register />} exact />
                </Route>
                <Route element={<AuthorizedLayout />}>
                    <Route path='/storage' element={<Storage />} exact />
                    <Route path='/about' element={<About />} exact />
                    <Route path='/profile' element={<Profile />} exact />
                </Route>
                <Redirect to='/login' />
            </Routes>
        </BrowserRouter>
    );
};

export default AppRouter;