import { useMutation, useQueryClient } from '@tanstack/react-query';
import { useNavigate } from 'react-router-dom';
import { AuthApi } from '../../api';

const useLogout = () => {
    const navigate = useNavigate();
    const queryClient = useQueryClient();

    const {
        mutateAsync: logout,
        isLoading,
        isError
    } = useMutation({
        mutationFn: async () => AuthApi.logout(),
        onSuccess: () => {
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            navigate('/login');
        }
    });

    return { logout, isLoading, isError };
};

export default useLogout;
