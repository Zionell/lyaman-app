<template>
    <label :class="[$style.checkbox, { [$style.error]: error !== '' }]">
        <CheckboxSvg :checked="value" :error="error !== ''"/>
        <input
            v-model="value"
            :class="$style.input"
            type="checkbox"
            @input="$emit('input', value)"
        />
        {{ labelValue }}
    </label>
</template>

<script>
export default {
    name: 'VCheckbox',

    props: {
        labelValue: {
            type: String,
            default: 'text',
        },

        error: {
            type: String,
            default: '',
        },
    },

    data() {
        return {
            value: false,
        };
    },
};
</script>

<style lang="scss" module>
    .checkbox {
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .input {
        display: none;
    }

    .error {
        color: $error;
    }
</style>
