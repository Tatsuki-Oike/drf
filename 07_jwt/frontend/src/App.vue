<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import axios from 'axios'

const token = ref(null);
const refreshToken = ref(null);
const data: Ref<any> = ref(null);
const verifyMsg = ref("")

const user = {
  "username": "admin",
  "password": "userpass"
}

const fetchToken = async () => {
  const response = await axios.post(
    "http://127.0.0.1:8000/api-auth/token/", 
    user,
    {
      headers: {
        'Content-Type': 'application/json'
      }
    }
  );
  token.value = response.data.access;
  refreshToken.value = response.data.refresh;
}

const refresh = async () => {
  const response = await axios.post(
    "http://127.0.0.1:8000/api-auth/token/refresh/", 
    {
      "refresh": refreshToken.value
    },
    {
      headers: {
        'Content-Type': 'application/json',
      }
    }
  );
  token.value = response.data.access;
}

const fetchData = async () => {
  try{

    const verifyResponse = await axios.post(
      "http://127.0.0.1:8000/api-auth/token/verify/", 
      {"token": token.value},
      {
        headers: {
          'Content-Type': 'application/json',
        }
      }
    );
    verifyMsg.value = verifyResponse.data

    const response = await axios.get(
      "http://127.0.0.1:8000/api/hello/", 
      {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token.value}`
        }
      }
    );    
    data.value = response.data;
  } catch(error) {
    data.value = error
  }
}

</script>

<template>
  <h1 class="mt-3">Hello</h1>
  <p>Token: {{ token }}</p>
  <p>Refresh Token: {{ refreshToken }}</p>
  <p>Verify Msg: {{ verifyMsg }}</p>
  <p>Data: {{ data }}</p>
  <button class="btn btn-primary" v-on:click="fetchToken">
    Tokenの取得
  </button>
  <button class="btn btn-primary mx-3" v-on:click="refresh">
    Tokenの再発行
  </button>
  <button class="btn btn-primary" v-on:click="fetchData">
    APIの実行
  </button>
</template>
