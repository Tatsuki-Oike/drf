<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue';
import axios from 'axios'

type TokenType = {
  "key": string
}
const token: Ref<TokenType> = ref({"key": ""})
const data: Ref<any> = ref(null);
const logoutMsg: Ref<string> = ref("")

const user = {
  "username": "admin",
  "password": "userpass"
}

const fetchToken = async () => {
  const response = await axios.post("http://127.0.0.1:8000/api-auth/login/", 
  user,
  {
    headers: {
      'Content-Type': 'application/json'
    }
  });
  token.value = response.data;
}

const fetchData = async () => {
  try{
    const response = await axios.get("http://127.0.0.1:8000/api/hello/", 
    {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token.value.key}`
      }
    });
    data.value = response.data;
  } catch(error) {
    data.value = error
  }
}

const logout = async () => {
  const response = await axios.post("http://127.0.0.1:8000/api-auth/logout/", 
  null,
  {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Token ${token.value.key}`
    }
  });
  logoutMsg.value = response.data;
}

</script>

<template>
  <h1 class="mt-3">Hello</h1>
  <p>Token: {{ token }}</p>
  <p>Data: {{ data }}</p>
  <p>LogoutMsg: {{ logoutMsg }}</p>
  <button class="btn btn-primary" v-on:click="fetchToken">Tokenの取得</button>
  <button class="btn btn-primary mx-3" v-on:click="fetchData">APIの実行</button>
  <button class="btn btn-primary" v-on:click="logout">Tokenの消去</button>
</template>
