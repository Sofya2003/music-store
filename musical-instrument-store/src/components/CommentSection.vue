<template>
    <div class="comment">
            <p class="comment__title">Отзывы</p>
            <ul>
                <li v-for="item in commentList" :key="item.id" class="comment__item">
                    <p class="comment__name">{{ item.name }}</p>
                    <p class="comment__rate">Оценка: </p>
                    <p class="">{{ item.text }}</p>
                </li>
            </ul>
        </div>
</template>

<script>
export default {
    data() {
        return {
            commentList: [{name: 'Боренька', text: 'Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош'},
            {name: 'Боренька', text: 'Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош'},
            {name: 'Боренька', text: 'Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош Харош'}
            ],
        }
    }
}
</script>

<style scoped>
.comment {
    max-width: 372px;
    width: 100%;
}

.comment__title {
    font-style: normal;
    font-weight: 400;
    font-size: 24px;
    line-height: 39px;
    margin-bottom: 20px;
}

.comment__name, .comment__rate {
    font-weight: bold;
}

.comment__item {
    border: 1px solid black;
    border-radius: 15px;
    padding: 25px 30px;
    margin-bottom: 20px;
}

@media (min-width: 1000px) {
    .comment {
    max-width: 900px;
}
}
</style>