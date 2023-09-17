import {Outlet} from 'react-router-dom';
import Box from '@mui/material/Box';
import Header from '../components/Header';

const AuthorizedLayout = () => {
    return (
        <Box>
            <Header />
            <Outlet />
        </Box>
    )
};

export default AuthorizedLayout;