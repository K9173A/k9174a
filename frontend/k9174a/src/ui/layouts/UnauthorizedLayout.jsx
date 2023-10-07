import React from 'react';
import { useCookies } from 'react-cookie';
import { Navigate, Outlet } from 'react-router-dom';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

const UnauthorizedLayout = () => {
    const [cookies] = useCookies(['K9174A_TOKEN']);

    const checkAuthTokenValidity = () => {
        // todo: request validate
        return cookies.K9174A_TOKEN;
    };

    if (checkAuthTokenValidity()) {
        return <Navigate to='/storage' />;
    } else {
        return (
            <Box
                sx={{
                    height: '100vh',
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'center',
                    alignItems: 'center',
                }}
            >
                <Typography variant='h3'>
                    K9174A
                </Typography>
                <Box
                    sx={{
                        display: 'flex',
                        flexDirection: 'column',
                        justifyContent: 'center',
                        alignItems: 'center',
                        p: 4,
                        border: '2px solid #6b7785',
                        borderRadius: '5%',
                        backgroundColor: '#8f9ca282'
                    }}
                >
                    <Outlet />
                </Box>
            </Box>
        );
    }
};

export default UnauthorizedLayout;