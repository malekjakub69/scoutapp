import { defineConfig, loadEnv } from 'vite';

import react from '@vitejs/plugin-react-swc';
import svgrPlugin from 'vite-plugin-svgr';
import viteTsconfigPaths from 'vite-tsconfig-paths';

export default defineConfig(({ command, mode }) => {
    // Load env file based on `mode` in the current working directory.
    // Set the third parameter to '' to load all env regardless of the `VITE_` prefix.
    const env = loadEnv(mode, process.cwd(), '');

    return {
        plugins: [react(), viteTsconfigPaths(), svgrPlugin()],
        server: {
            port: 3000,
            host: '0.0.0.0',
        }
    };
});
