<template>
  <div class="player-card">
    <img :src="player.image" alt="Player Image" />
    <h3>{{ player.name }}</h3>
    <p>{{ player.role }}</p>
    <p>{{ player.team }}</p>
  </div>
</template>

<script>
export default {
  props: {
    player: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.player-card {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  text-align: center;
  width: 150px;
}
.player-card img {
  border-radius: 50%;
  width: 100px;
  height: 100px;
}
</style>