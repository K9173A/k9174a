import { useCookies } from 'react-cookie';
import { Navigate, Outlet } from 'react-router-dom';
import Box from '@mui/material/Box';
import Header from '../components/Header';

const AuthorizedLayout = () => {
    const [cookies] = useCookies(['K9174A_TOKEN']);

    if (cookies.K9174A_TOKEN) {
        return (
            <Box>
                <Header />
                <Outlet />
            </Box>
        );
    } else {
        return <Navigate to='/login' />
    }
};

export default AuthorizedLayout;