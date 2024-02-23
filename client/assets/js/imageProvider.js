import { joinURL } from 'ufo';

export function getImage(src, { modifiers, baseURL } = {}, { options, nuxtContext, $img }) {
    const { width, height, format, fit, ...providerModifiers } = modifiers;
    const operations = [];

    const operationsString = operations.join(',');
    return {
        url: joinURL(baseURL + src, operationsString),
    };
}
