<template>
    <div class="login">
        <h2>Вход</h2>
        <form action="">
            <input type="email" placeholder="email@.gmail.com">
            <input type="password" placeholder="Введите пароль">
            <button class="cta-btn" @click="login()">Войти</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
        }
    },
    methods: {
        login() {
        },
    }
}
</script>

<style scoped>
h2 {
    font-style: normal;
    font-weight: 400;
    font-size: 44px;
    line-height: 58px;
}
.login {
    max-width: 372px;
    min-height: 634px;
    margin: 0 auto;
}

form {
    display: flex;
    flex-direction: column;
    border: 1px solid rgba(0, 0, 0, 0.39);
    box-shadow: 0px 0px 7px 3px rgba(0, 0, 0, 0.14);
    border-radius: 15px;
    padding: 30px 0;
}

input {
    margin: 0 auto 20px;
    padding: 5px 10px;
    max-width: 340px;
    width: 100%;
    height: 45px;
    border: 1px solid #000000;
    border-radius: 15px;
}

.cta-btn {
    margin: 0 auto;
    background: #FCBA06;
    border-radius: 15px;
    max-width: 340px;
    width: 100%;
    padding: 10px 15px;
}
</style>