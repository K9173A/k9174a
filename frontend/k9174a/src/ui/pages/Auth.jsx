import React from 'react';
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import Login from './Login';
import Register from './Register';

const Auth = () => {
    const [mode, setMode] = React.useState('login');
    const onSignUpLinkClick = () => setMode((mode) => mode === 'login' ? 'register' : 'login');

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
                {mode === 'login' ? <Login /> : <Register />}
            </Box>
            <Typography variant='body2' sx={{ my: 1 }}>
                {mode === 'login'
                    ? 'Don\'t have an account?'
                    : 'Already have an account?'
                }
                <Link
                    component='button'
                    variant='body2'
                    onClick={onSignUpLinkClick}
                >
                    {mode === 'login'
                        ? 'Sign up for K9174A'
                        : 'Sign in for K9174A'
                    }
                </Link>
            </Typography>
        </Box>
    );
};

export default Auth;