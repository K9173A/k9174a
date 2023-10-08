import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import { validate } from '../../api/service';

const UnauthorizedLayout = () => {
    return validate()
        .then((success) => {
            if (success) {
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
        });
};

export default UnauthorizedLayout;