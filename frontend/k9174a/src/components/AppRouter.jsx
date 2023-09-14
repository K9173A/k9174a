import React from 'react';
import {Route, Routes} from 'react-router-dom';
import About from '../pages/About';
import Storage from '../pages/Storage';
import Profile from '../pages/Profile';

const AppRouter = () => {
    const publicRoutes = [
        {path: '/storage', element: <Storage />, exact: true},
        {path: '/about', element: <About />, exact: true},
        {path: '/profile', element: <Profile />, exact: true}
    ];

    return (
        <Routes>
            {publicRoutes.map(route =>
                <Route
                    element={route.element}
                    path={route.path}
                    exact={route.exact}
                />
            )}
        </Routes>
    )
};

export default AppRouter;