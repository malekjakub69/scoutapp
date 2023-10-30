import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import { FC } from 'react';
import { Button } from './components/shareds/Button';

export const queryClient = new QueryClient({ defaultOptions: { queries: { refetchOnWindowFocus: false } } });

const App: FC = () => (
    <QueryClientProvider client={queryClient}>
        <div className="m-8">
            <Button variant="primary" mode="dark">
                Button text
            </Button>
        </div>
        <ReactQueryDevtools />
    </QueryClientProvider>
);

export default App;
