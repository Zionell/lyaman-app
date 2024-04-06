<template>
    <div :class="$style.IndexPage">
        <transition name="fade" mode="out-in">
            <LoaderPage v-if="isLoading" />

            <div v-else>
                <HomeHero v-if="hero && hero.title" :data="hero"/>

                <SectionTemplate
                    v-if="workProcess && workProcess.work_process_items"
                    :title="workProcess.title.data.attributes"
                >
                    <HomeWorkProcess :data="workProcess.work_process_items.data"/>
                </SectionTemplate>

                <SectionTemplate
                    v-if="cases && cases.case_items"
                    :title="cases.title.data.attributes"
                >
                    <HomeCases :data="cases.case_items.data"/>
                </SectionTemplate>

                <SectionTemplate
                    v-if="reviews && reviews.length"
                    :title="reviewsTitle"
                >
                    <HomeReviews :data="reviews"/>
                </SectionTemplate>

                <SectionTemplate
                    v-if="services && services.services"
                    :title="services.title.data.attributes"
                >
                    <HomeServices :data="services.services.data"/>
                </SectionTemplate>

                <HomeForm/>
            </div>
        </transition>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

import HomeHero from '~/components/pages/home/HomeHero';
import HomeForm from '~/components/pages/home/form/HomeForm';
import SectionTemplate from '~/components/common/SectionTemplate';
import HomeWorkProcess from '~/components/pages/home/workProcess/HomeWorkProcess';
import HomeCases from '~/components/pages/home/cases/HomeCases.vue';
import HomeServices from '~/components/pages/home/services/HomeServices.vue';
import HomeReviews from '~/components/pages/home/HomeReviews.vue';
import LoaderPage from '~/components/common/LoaderPage.vue';

export default {
    name: 'IndexPage',

    components: {
        LoaderPage,
        HomeReviews,
        HomeServices,
        HomeCases,
        HomeHero,
        SectionTemplate,
        HomeWorkProcess,
        HomeForm,
    },

    data() {
        return {
            isLoading: true,
            hero: {},
            workProcess: {},
            cases: {},
            services: {},
            reviews: [],
        };
    },

    computed: {
        ...mapState({
            menuItems: state => state.general.menuItems,
        }),

        reviewsTitle() {
            return this.menuItems.find(m => m.value === 'reviews');
        },
    },

    mounted() {
        this.fetchData();
    },

    methods: {
        ...mapActions({
            fetchContacts: 'general/fetchContacts',
        }),

        async fetchData() {
            try {
                const [
                    hero,
                    workProcess,
                    cases,
                    services,
                    reviews,
                ] = await Promise.all([
                    this.$axios.$get(this.$api.heroBlock),
                    this.$axios.$get(this.$api.workProcesses),
                    this.$axios.$get(this.$api.cases),
                    this.$axios.$get(this.$api.services),
                    this.$axios.$get(this.$api.reviews),
                    this.fetchContacts(),
                ]);

                this.hero = hero?.data?.attributes || {};
                this.workProcess = workProcess?.data?.attributes || {};
                this.cases = cases?.data?.attributes || {};
                this.services = services?.data?.attributes || {};
                this.reviews = reviews?.data || [];
            } catch (e) {
                console.warn(e);
            } finally {
                this.isLoading = false;
            }
        },
    },
};
</script>

<style lang="scss" module>
    .IndexPage {
        overflow: hidden;
    }
</style>
