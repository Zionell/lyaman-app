<template>
    <div :class="$style.IndexPage">
        <HomeHero v-if="hero && hero.title" :data="hero"/>

        <SectionTemplate
            v-if="projectSteps && projectSteps.steps"
            :title="projectSteps.title"
        >
            <HomeAboutCourse :data="projectSteps.steps"/>
        </SectionTemplate>

        <SectionTemplate
            v-if="workProcess && workProcess.steps"
            :title="workProcess.title"
            is-blue
        >
            <HomeWorkProcess :data="workProcess.steps"/>
        </SectionTemplate>

        <HomeForm/>
    </div>
</template>

<script>
import HomeHero from '~/components/pages/home/HomeHero';
import HomeForm from '~/components/pages/home/form/HomeForm';
import SectionTemplate from '~/components/common/SectionTemplate';
import HomeAboutCourse from '~/components/pages/home/aboutCourse/HomeAboutCourse';
import HomeWorkProcess from '~/components/pages/home/workProcess/HomeWorkProcess';

export default {
    name: 'IndexPage',

    components: {
        HomeHero,
        SectionTemplate,
        HomeAboutCourse,
        HomeWorkProcess,
        HomeForm,
    },

    async asyncData({ app }) {
        try {
            const [
                hero,
                projectSteps,
                workProcess,
            ] = await Promise.all([
                app.$axios.$get(app.$api.header),
                app.$axios.$get(app.$api.projectSteps),
                app.$axios.$get(app.$api.workProcess),
            ]);

            return {
                hero: hero || {},
                projectSteps: projectSteps || {},
                workProcess: workProcess || {},
            };
        } catch (e) {
            console.warn(e);
        }
    },

    data() {
        return {
            hero: {},
            projectSteps: {},
            workProcess: {},
        };
    },
};
</script>

<style lang="scss" module>
    .IndexPage {
        //
    }
</style>
