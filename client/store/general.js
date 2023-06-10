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
    async fetchContacts({ commit }) {
        try {
            const [
                menuItems,
                contacts,
            ] = await Promise.all([
                this.$axios.$get(this.$api.menuItems),
                this.$axios.$get(this.$api.contacts),
            ]);
            commit('SET_MENU_ITEMS', menuItems);
            commit('SET_SOCIAL_LINKS', contacts);
        } catch (e) {
            console.log(e);
        }
    },
};
