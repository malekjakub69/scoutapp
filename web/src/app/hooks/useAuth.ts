import { useQuery } from '@tanstack/react-query';
import { AuthApi } from 'src/api';
import queryKeys from './queryKeys';

const useAuth = () => {
    const {
        data: user,
        isLoading: authLoading,
        isError: authError
    } = useQuery({
        queryKey: queryKeys.AUTH_KEY,
        queryFn: () => AuthApi.authenticate(),
        staleTime: 10 * 60 * 1000,
        retry: false
    });

    return { user, authLoading, authError };
};

export default useAuth;
