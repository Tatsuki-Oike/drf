<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const data = ref(null);

const fetchData = async () => {
  const response = await axios.get("http://127.0.0.1:8000/api/hello/", {
    headers: {
      'Content-Type': 'application/json'
    }
  });
  data.value = response.data;
}

fetchData()

</script>

<template>
  <h1 class="mt-3">Hello</h1>
  {{ data }}
</template>
