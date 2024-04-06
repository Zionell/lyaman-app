export const state = () => ({
    menuItems: [],
    socialLinks: [],
});

export const mutations = {
    SET_MENU_ITEMS(state, payload) {
        payload.data.forEach(d => state.menuItems.push(d.attributes));
    },

    SET_SOCIAL_LINKS(state, payload) {
        payload.data.forEach(d => state.socialLinks.push(d.attributes));
    },
};

export const actions = {
    async fetchContacts({ commit }) {
        try {
            const [
                menuItems,
                messengers,
            ] = await Promise.all([
                this.$axios.$get(this.$api.menuItems),
                this.$axios.$get(this.$api.messengers),
            ]);
            commit('SET_MENU_ITEMS', menuItems);
            commit('SET_SOCIAL_LINKS', messengers);
        } catch (e) {
            console.log(e);
        }
    },
};
