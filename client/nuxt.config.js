import headConfig from './config/headConfig';
import { plugins } from './config/plugins';

require('dotenv')
    .config();

const isDev = process.env.NODE_ENV === 'development';

export default {
    target: 'static',

    loadingIndicator: {
        name: 'pulse',
        color: '#3B8070',
        background: 'white',
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
        '~/assets/scss/castom__scroll',
        '~/assets/scss/style',
    ],

    styleResources: {
        scss: [
            './assets/scss/shared/_function.scss',
            './assets/scss/shared/_mixins.scss',
            './assets/scss/shared/_fonts.scss',
            './assets/scss/shared/_vars.scss',
            './assets/scss/shared/_text.scss',
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

    axios: {
        baseURL: 'https://raw.githubusercontent.com/Lyamann/study/main',
    },

    build: {
        publicPath: '/n/',

        analyze: isDev,

        // Set libraries to transpile by babel
        transpile: !isDev && [],

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
        terser: !isDev && {
            terserOptions: {
                mangle: {
                    safari10: true,
                },
            },
        },

        // Postcss settings
        postcss: !isDev && {
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
