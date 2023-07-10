import { createStore } from 'vuex'
import Axios from 'axios';

const store = createStore({
    state: {
        instruments: null,
        subcategory: null,
    },
    getters: {
        INSTRUMENTS: state =>{
            return state.instruments;
        },
        SUBCATEGORY: state =>{
            return state.subcategory;
        },
    },
    mutations: {
        SET_INSTRUMENTS: (state,payload) => {
            state.instruments = payload;
        },
        SET_SUBCATEGORY: (state,payload) => {
            state.subcategory = payload;
        },
    },
    actions: {
        GET_INSTRUMENTS: async (context) => {
            let {data} = await Axios.get('http://localhost:8086/api/v1/instruments/');
            context.commit('SET_INSTRUMENTS', data.results);
        },

        GET_INSTRUMENTS_FILTER_CATEGORY: async (context, cat) => {
            let {data} = await Axios.get(`http://localhost:8086/api/v1/instruments/?category=${cat}`);
            context.commit('SET_INSTRUMENTS', data.results);
        },

        GET_SUBCATEGORY_FILTER_CATEGORY: async (context, cat) => {
            let {data} = await Axios.get(`http://localhost:8086/api/v1/subcategory/?id=${cat}`);
            context.commit('SET_SUBCATEGORY', data);
        },

        GET_INSTRUMENTS_FILTER_SUBCATEGORY: async (context, input) => {

            let {data} = await Axios.get(`http://localhost:8086/api/v1/instruments/?category=${input.cat}&subcategory=${input.sub}`);
            context.commit('SET_INSTRUMENTS', data.results);
        },

    }
  })

  export default store

