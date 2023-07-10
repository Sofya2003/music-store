<template>
    <div class="register">
        <h2 v-show="section < 5">Регистрация</h2>
        <form id="regForm" action="" v-show="section >= 1 && section <= 4">
            <div class="tab" v-show="section == 1">
                <p class="form-title">
                    ФИО:
                </p>
                <p>
                    <input placeholder="Имя" oninput="this.className = ''">
                </p>
                <p>
                    <input placeholder="Фамилия" oninput="this.className = ''">
                </p>
                <p>
                    <input placeholder="Отчество" oninput="this.className = ''">
                </p>
            </div>
            <div class="tab" v-show="section == 2">
                <p class="form-title">
                    Контактная информация:
                </p>
                <p>
                    <input name="email" placeholder="example@mail.ru" oninput="this.className = ''" required>
                </p>
                <p>
                    <input placeholder="+79157779944" oninput="this.className = ''">
                </p>
            </div>
            <div class="tab" v-show="section == 3">
                <p class="form-title">
                    Дата рождения:
                </p>
                <p>
                    <input placeholder="dd" oninput="this.className = ''">
                </p>
                <p>
                    <input placeholder="mm" oninput="this.className = ''">
                </p>
                <p>
                    <input placeholder="yyyy" oninput="this.className = ''">
                </p>
            </div>
            <div class="tab" v-show="section == 4">
                <p class="form-title">
                    Логин и пароль:
                </p>
                <p>
                    <input placeholder="Логин" oninput="this.className = ''">
                </p>
                <p>
                    <input placeholder="Пароль" oninput="this.className = ''">
                </p>
            </div>
            <div v-show="section <= 4" class="control">
                <button type="button" class="prev" id="prevBtn" @click="prev()">Назад</button>
                <button type="button" class="next" v-show="section < 4" id="nextBtn" @click="next()">Вперед</button>
                <button type="submit" class="next" v-show="section == 4" id="nextBtn" @click="next()">Отправить</button>
            </div>
            <div v-show="section <= 4">
                <button type="button" id="1" class="step active" @click="swith(1)"></button>
                <button type="button" id="2" class="step" @click="swith(2)"></button>
                <button type="button" id="3" class="step" @click="swith(3)"></button>
                <button type="button" id="4" class="step" @click="swith(4)"></button>
            </div>
        </form>
        <p v-show="section == 5" class="end">Вы зарегистрированы! Подтвердите почту!</p>
    </div>
</template>

<script>

import axios from 'axios'

export default {
    data() {
        return {
            section: 1,
            prevActive: 1,
        }
    },
    methods: {

        async next() {
            if (this.section + 1 < 5) {
                this.section += 1;
                console.log(this.section);
                document.getElementById(this.prevActive).classList.toggle('active');
                document.getElementById(String(this.section)).classList.toggle('active');
                this.prevActive = this.section;
            } else {
                this.section += 1
                const response = await axios.get(`http://localhost:8086/main`);
                console.log(response.data);
            }
        },


        prev() {
            if (this.section - 1 > 0) {
                this.section -= 1;
                document.getElementById(this.prevActive).classList.toggle('active');
                document.getElementById(String(this.section)).classList.toggle('active');
                this.prevActive = this.section;
            }
            console.log(this.section)
        },
        swith(n) {
            this.section = n;
            document.getElementById(this.prevActive).classList.toggle('active');
            document.getElementById(String(n)).classList.toggle('active');
            this.prevActive = n;
            console.log(this.section)
        },
    }
}
</script>

<style scoped>
/* .wrapper {
    margin: 0 auto;
} */

h2 {
    font-style: normal;
    font-weight: 400;
    font-size: 44px;
    line-height: 58px;
    margin: 20px auto;
}

.end {
    font-style: normal;
    font-weight: 400;
    font-size: 30px;
    line-height: 58px;
    margin: 20px auto;
}

.register {
    max-width: 372px;
    min-height: 634px;
    margin: 0 auto;
}

form {
    max-width: 372px;
    display: flex;
    flex-direction: column;
    border: 1px solid rgba(0, 0, 0, 0.39);
    box-shadow: 0px 0px 7px 3px rgba(0, 0, 0, 0.14);
    border-radius: 15px;
    padding: 20px 0;
    margin: 0 auto;
    text-align: center;
}

.form-title {
    margin-bottom: 20px;
}

.control {
    max-width: 340px;
    width: 100%;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
}

.next {
    background-color: #FCBA06;
    padding: 5px 10px;
    border-radius: 10px;
    border: 2px solid #FCBA06;
}

.prev {
    padding: 5px 10px;
    border-radius: 10px;
    border: 2px solid #FCBA06;
}

.next:hover {
    background-color: white;
    transition: .3s;
}

.prev:hover {
    background-color: #FCBA06;
    transition: .3s;
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

.step {
    height: 15px;
    width: 15px;
    margin: 0 2px;
    background-color: #bbbbbb;
    border: none;
    border-radius: 50%;
    display: inline-block;
    opacity: 0.5;
}

/* Mark the active step: */
.step.active {
    background-color: #000000;
}
</style>