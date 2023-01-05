export const state = () => ({
    menuItems: [],
    socialLinks: [],
});

export const getters = {};

export const mutations = {
    SET_MENU_ITEMS(state, payload) {
        state.menuItems = payload;
    },
    SET_SOCIAL_LINKS(state, payload) {
        state.socialLinks = payload;
    },
};

export const actions = {
    async fetchMenuItems({ commit }) {
        try {
            const res = await this.$axios.$get(this.$api.general);
            commit('SET_MENU_ITEMS', res?.menu_items);
            commit('SET_SOCIAL_LINKS', res?.social_links);
        } catch (e) {
            console.log(e);
        }
    },
};
