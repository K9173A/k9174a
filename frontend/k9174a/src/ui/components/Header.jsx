import * as React from 'react';
import {Link} from 'react-router-dom';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import CloudIcon from '@mui/icons-material/Cloud';
import IconButton from '@mui/material/IconButton';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';

const Header = () => {
    const links = {
        '/login': 'Login',
        '/storage': 'Storage',
        '/about': 'About',
        '/profile': 'Profile'
    };

    return (
        <Box>
            <AppBar
                position="static"
                sx={{
                    flexDirection: 'row',
                    justifyContent: 'space-between'
                }}
            >
                <IconButton
                    size="large"
                    edge="start"
                    color="inherit"
                    aria-label="menu"
                    sx={{
                        mx: 2
                    }}
                    disableRipple
                >
                    <CloudIcon
                        sx={{ mr: 1 }}
                    />
                    <Typography
                        variant="h6"
                        component="div"
                    >
                        K9174A
                    </Typography>
                </IconButton>
                <Toolbar>
                    {Object.entries(links).map(
                        ([link, title]) => <Button component={Link} to={link} color="inherit">{title}</Button>
                    )}
                </Toolbar>
            </AppBar>
        </Box>
    );
};

export default Header;