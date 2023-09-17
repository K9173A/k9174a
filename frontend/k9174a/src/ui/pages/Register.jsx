import React from 'react';
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
import classes from './Register.module.css';
import {register} from '../../api/service';

const Register = () => {
    const [email, setEmail] = React.useState('');
    const [username, setUsername] = React.useState('');
    const [password, setPassword] = React.useState('');
    const [showPassword, setShowPassword] = React.useState(false);

    const handleClickShowPassword = () => setShowPassword((show) => !show);
    const handleMouseDownPassword = (event) => event.preventDefault();
    const handleSubmitButtonClick = (event) => {
        event.preventDefault();
        register({email, username, password})
            .then((response) => {
                console.log(response)
            })
            .catch(() => console.log('failed'));
    };

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
                Register
            </Typography>
            <form
                className={classes.form}
                onSubmit={handleSubmitButtonClick}
            >
                <FormControl
                    variant="outlined"
                    sx={{
                        my: 1,
                        width: '100%'
                    }}
                    required
                >
                    <InputLabel
                        htmlFor="email"
                    >
                        Email
                    </InputLabel>
                    <OutlinedInput
                        id="email"
                        label="Email"
                        onChange={event => setEmail(event.target.value)}
                    />
                </FormControl>
                <FormControl
                    variant="outlined"
                    sx={{
                        my: 1,
                        width: '100%'
                    }}
                    required
                >
                    <InputLabel
                        htmlFor="username"
                    >
                        Username
                    </InputLabel>
                    <OutlinedInput
                        id="username"
                        label="Username"
                        onChange={event => setUsername(event.target.value)}
                    />
                </FormControl>
                <FormControl
                    variant="outlined"
                    sx={{
                        my: 1
                    }}
                    required
                >
                    <InputLabel
                        htmlFor="password"
                    >
                        Password
                    </InputLabel>
                    <OutlinedInput
                        id="password"
                        label="Password"
                        type={showPassword ? 'text' : 'password'}
                        endAdornment={
                            <InputAdornment>
                                <IconButton
                                    aria-label="password-visibility-toggle"
                                    onClick={handleClickShowPassword}
                                    onMouseDown={handleMouseDownPassword}
                                    edge="end"
                                >
                                    {showPassword ? <VisibilityOff /> : <Visibility />}
                                </IconButton>
                            </InputAdornment>
                        }
                        onChange={event => setPassword(event.target.value)}
                    />
                </FormControl>
                <Button
                    type="submit"
                    variant="contained"
                    size="large"
                    sx={{
                        width: '100%',
                        my: 1
                    }}
                >
                    Register
                </Button>
            </form>
        </Box>
    );
};

export default Register;