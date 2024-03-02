<template>
    <div :class="$style.IndexPage">
        <HomeHero v-if="hero && hero.title" :data="hero"/>

        <SectionTemplate
            v-if="workProcess && workProcess.work_process_items"
            :title="workProcess.title.data.attributes"
        >
            <HomeWorkProcess :data="workProcess.work_process_items.data"/>
        </SectionTemplate>

        <SectionTemplate
            v-if="cases && cases.case_items && false"
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
</template>

<script>
import HomeHero from '~/components/pages/home/HomeHero';
import HomeForm from '~/components/pages/home/form/HomeForm';
import SectionTemplate from '~/components/common/SectionTemplate';
import HomeWorkProcess from '~/components/pages/home/workProcess/HomeWorkProcess';
import HomeCases from '~/components/pages/home/cases/HomeCases.vue';
import HomeServices from '~/components/pages/home/services/HomeServices.vue';
import HomeReviews from '~/components/pages/home/HomeReviews.vue';
import { mapState } from 'vuex';

export default {
    name: 'IndexPage',

    components: {
        HomeReviews,
        HomeServices,
        HomeCases,
        HomeHero,
        SectionTemplate,
        HomeWorkProcess,
        HomeForm,
    },

    async asyncData({ app }) {
        try {
            const [
                hero,
                workProcess,
                cases,
                services,
                reviews,
            ] = await Promise.all([
                app.$axios.$get(app.$api.heroBlock),
                app.$axios.$get(app.$api.workProcesses),
                app.$axios.$get(app.$api.cases),
                app.$axios.$get(app.$api.services),
                app.$axios.$get(app.$api.reviews),
            ]);

            return {
                hero: hero?.data?.attributes || {},
                workProcess: workProcess?.data?.attributes || {},
                cases: cases?.data?.attributes || {},
                services: services?.data?.attributes || {},
                reviews: reviews?.data || [],
            };
        } catch (e) {
            console.warn(e);
        }
    },

    data() {
        return {
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
};
</script>

<style lang="scss" module>
    .IndexPage {
        overflow: hidden;
    }
</style>
