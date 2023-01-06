import {
    faviconsLinks,
    faviconsMeta,
} from './head/favicons';

require('dotenv')
    .config();

const isDev = process.env.NODE_ENV === 'development';

const headConfig = {
    htmlAttrs: { lang: 'ru' },

    title: 'Аскерова Ляман | Интернет-маркетолог',

    // Head meta
    meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },

        {
            hid: 'description',
            name: 'description',
            content: 'Онлайн обучение digital-маркетингу с нуля. Индивидуальные занятие с программой подобранной под вас, разбор домашних заданий. Продвигай свой бизнес или работай маркетологом онлайн.',
        },

        // Open Graph / Facebook / WhatsApp
        { hid: 'og:type', name: 'og:type', content: 'website' },
        { hid: 'og:url', name: 'og:url', content: 'https://lyaman-askerova.kz/' },
        { hid: 'og:title', name: 'og:title', content: 'Аскерова Ляман | Интернет-маркетолог' },
        {
            hid: 'og:site_name',
            name: 'og:site_name',
            content: 'Аскерова Ляман | Интернет-маркетолог',
        },
        {
            hid: 'og:description',
            name: 'og:description',
            content: 'Онлайн обучение digital-маркетингу с нуля. Индивидуальные занятие с программой подобранной под вас, разбор домашних заданий. Продвигай свой бизнес или работай маркетологом онлайн.',
        },
        { hid: 'og:image', name: 'og:image', content: '/images/seo.jpg' },
        { hid: 'og:image:type', name: 'og:image:type', content: '/images/seo.jpg' },
        { hid: 'og:image:width', name: 'og:image:width', content: '300' },
        { hid: 'og:image:height', name: 'og:image:height', content: '300' },

        // Twitter
        { hid: 'twitter:card', name: 'twitter:card', content: 'summary_large_image' },
        { hid: 'twitter:url', name: 'twitter:url', content: 'https://lyaman-askerova.kz/' },
        {
            hid: 'twitter:title',
            name: 'twitter:title',
            content: 'Аскерова Ляман | Интернет-маркетолог',
        },
        {
            hid: 'twitter:description',
            name: 'twitter:description',
            content: 'Онлайн обучение digital-маркетингу с нуля. Индивидуальные занятие с программой подобранной под вас, разбор домашних заданий. Продвигай свой бизнес или работай маркетологом онлайн.',
        },
        { hid: 'twitter:image', name: 'twitter:image', content: '/images/seo.jpg' },

        // Favicons
        ...faviconsMeta,
    ],

    // Head links
    link: [
        // Favicons
        ...faviconsLinks,
    ],

    script: [
        isDev ?
            {
                innerHTML: '(function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)}; m[i].l=1*new Date(); for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }} k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)}) (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym"); ym(91931534, "init", { clickmap:true, trackLinks:true, accurateTrackBounce:true, webvisor:true }); ',
                async: true,
            }
            : {},
    ],

    noscript: [
        isDev ?
            {
                innerHTML: '<div><img src="https://mc.yandex.ru/watch/91931534" style="position:absolute; left:-9999px;" alt="" /></div>',
                body: true,
            }
            : {},
    ],

    __dangerouslyDisableSanitizers: ['script', 'noscript'],
};

export default headConfig;
