import React from 'react';
import { Navigate } from 'react-router-dom';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import FormControl from '@mui/material/FormControl';
import IconButton from '@mui/material/IconButton';
import InputAdornment from '@mui/material/InputAdornment';
import InputLabel from '@mui/material/InputLabel';
import OutlinedInput from '@mui/material/OutlinedInput';
import Typography from '@mui/material/Typography';
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';
import classes from './Login.module.css';
import { login } from '../../api/service';

const Login = () => {
    const [username, setUsername] = React.useState('');
    const [password, setPassword] = React.useState('');
    const [showPassword, setShowPassword] = React.useState(false);

    const handleClickShowPassword = () => setShowPassword((show) => !show);
    const handleMouseDownPassword = (event) => event.preventDefault();
    const handleLoginButtonClick = (event) => {
        event.preventDefault();
        login({username, password})
            .then((success) => {
                if (success) {
                    return <Navigate to='/storage' />;
                } else {
                    alert('Login error!');
                }
            })
    }

    return (
        <Box
            sx={{
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'center',
                alignItems: 'center'
            }}
        >
            <Typography variant='h4' sx={{ my: 1 }}>
                Login
            </Typography>
            <form
                className={classes.form}
                onSubmit={handleLoginButtonClick}
            >
                <FormControl
                    variant='outlined'
                    sx={{
                        my: 1,
                        width: '100%'
                    }}
                    required
                >
                    <InputLabel htmlFor='email'>
                        Username
                    </InputLabel>
                    <OutlinedInput
                        id='username'
                        label='Username'
                        onChange={event => setUsername(event.target.value)}
                    />
                </FormControl>
                <FormControl
                    variant='outlined'
                    sx={{
                        my: 1
                    }}
                    required
                >
                    <InputLabel htmlFor='password'>
                        Password
                    </InputLabel>
                    <OutlinedInput
                        id='password'
                        label='Password'
                        type={showPassword ? 'text' : 'password'}
                        endAdornment={
                            <InputAdornment>
                                <IconButton
                                    aria-label='password-visibility-toggle'
                                    onClick={handleClickShowPassword}
                                    onMouseDown={handleMouseDownPassword}
                                    edge='end'
                                >
                                    {showPassword ? <VisibilityOff /> : <Visibility />}
                                </IconButton>
                            </InputAdornment>
                        }
                        onChange={event => setPassword(event.target.value)}
                    />
                </FormControl>
                {/* todo: remember me */}
                <Button
                    type='submit'
                    variant='contained'
                    size='large'
                    sx={{
                        width: '100%',
                        my: 1
                    }}
                >
                    Log In
                </Button>
            </form>
        </Box>
    );
};

export default Login;