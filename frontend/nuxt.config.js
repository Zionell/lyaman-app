import headConfig from './config/headConfig';
import { plugins } from './config/plugins';

require('dotenv')
    .config();

const env = {
    IS_DEV: process.env.NODE_ENV === 'development',
    SERVER_API_URL: process.env.SERVER_API_URL,
};

export default {
    loadingIndicator: {
        name: 'pulse',
        color: '#3B8070',
        background: 'white',
    },

    server: {
        port: 3000,
        host: '0.0.0.0',
    },

    head: headConfig,

    // Router settings
    router: {
        linkActiveClass: '_active-link',
        linkExactActiveClass: '_exact-link',
    },

    loading: {
        color: '#d9ff6c',
        height: '2px',
        throttle: 0,
    },

    css: [
        '~/assets/scss/nullstyle',
        '~/assets/scss/custom__scroll',
        '~/assets/scss/style',
    ],

    styleResources: {
        scss: [
            '~/assets/scss/shared/_function.scss',
            '~/assets/scss/shared/_mixins.scss',
            '~/assets/scss/shared/_fonts.scss',
            '~/assets/scss/shared/_vars.scss',
        ],
    },

    plugins: plugins,

    components: [
        {
            path: '~/components/ui',
            extensions: ['vue'],
            pathPrefix: false,
        },
    ],

    // Stylelint options
    stylelint: {
        files: [
            'assets/**/*.{s?(a|c)ss}',
            '**/components/**/*.{s?(a|c)ss}',
            '**/{components,layouts,services,pages}/**/*.vue',
        ],
    },


    modules: [
        '@nuxtjs/axios',
        '@nuxtjs/svg-sprite',
        '@nuxtjs/dotenv',
        '@nuxtjs/eslint-module',
        '@nuxtjs/stylelint-module',
        '@nuxtjs/style-resources',
    ],

    buildModules: [
        '@nuxt/image',
    ],

    image: {
        domains: [env.SERVER_API_URL || 'lyaman-askerova.kz'],
        providers: {
            customProvider: {
                name: 'customProvider',
                provider: '~/assets/js/imageProvider',
                options: {
                    baseURL: env.SERVER_API_URL,
                },
            },
        },
    },

    // axios: {
    //     proxy: true,
    // },

    build: {
        publicPath: '/n/',

        analyze: env.IS_DEV,

        // Set libraries to transpile by babel
        transpile: !env.IS_DEV && [],

        // You can extend webpack config here
        babel: {},

        loaders: {
            scss: {
                sourceMap: false,
            },
            vue: {
                cacheBusting: false,
            },
        },

        extractCss: true,

        // Terser settings
        terser: !env.IS_DEV && {
            terserOptions: {
                mangle: {
                    safari10: true,
                },
            },
        },

        // Postcss settings
        postcss: !env.IS_DEV && {
            preset: {
                autoprefixer: {
                    grid: true,
                },
            },
        },

        extend(config, ctx) {
            // Fixes npm packages that depend on `fs` module
            config.node = {
                fs: 'empty',
            };
        },
    },

};
