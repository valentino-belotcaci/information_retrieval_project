<template>
  <div id="app" class="page">
    <section class="main-section">
      <div class="left"></div>
      <div class="center">
        <img src="./assets/logo12.png" alt="logo" class="logo">
        <div class="Card">
          <div class="CardInner">
            <label>Search for your Tattoo</label>
            <div class="container">
              <div class="Icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#657789" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="feather feather-search"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>

              </div>
              <div class="InputContainer">
                <input placeholder="Search..." v-model="searchQuery"/>
                <div class="btn">
                  <button @click="search" role="button">Search</button>
                </div>
              </div>
            </div>
          </div>
          <div class="container-res">
            <!-- Loop over sortedResults to display each result -->
            <div v-for="result in searchResults.slice(0, 10)" :key="result.docno" class="result-container">
              <div class="text">
                <div class="result-item">
                  <a :href="result.link" target="_blank">{{ result.docno }}</a>
                </div>
                <div class="result-text">{{ truncateText(result.text) }}</div>
              </div>
              <div class="feedback">
                <button @click="sendFeedback(result.docno, true)">
                  <img src="./assets/thumb-up.png" alt="">
                </button>
                <button @click="sendFeedback(result.docno, false)" class="dislike">
                  <img src="./assets/thumb-down.png" alt="">
                </button>
              </div>
              <!-- Add more details if necessary -->
            </div>
          </div>
        </div>
      </div>
      <div class="right"></div>
    </section>
  </div>
</template>




<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchQuery: '',
      searchResults: [], // Populate this with your search results
    };
  },
  methods: {
    search() {
      axios.get(`http://localhost:8000/?query=${this.searchQuery}`)
        .then(response => {
          console.log(response.data);
          // Check if response.data is a string and needs JSON parsing
          this.searchResults = JSON.parse(response.data);
          console.log(this.searchResults);
          // Update the URL with the search query
          const newUrl = `${window.location.pathname}?query=${encodeURIComponent(this.searchQuery)}`;
          window.history.pushState({ path: newUrl }, '', newUrl);
        })
        .catch(error => {
          console.error('Error searching:', error);
        });
    },
    truncateText(text) {
    const words = text.split(' ');
    if (words.length > 40) {
      return words.slice(0, 40).join(' ') + '...';
    }
    return text;
  },
  sendFeedback(docno, isRelevant) {
    const docIndex = this.searchResults.findIndex(doc => doc.docno === docno);
    if (docIndex !== -1) {
      if (isRelevant && docIndex > 0) {
        // Swap with the previous item for relevant feedback
        [this.searchResults[docIndex - 1], this.searchResults[docIndex]] =
          [this.searchResults[docIndex], this.searchResults[docIndex - 1]];
      } else if (!isRelevant && docIndex < this.searchResults.length - 1) {
        // Swap with the next item for irrelevant feedback
        [this.searchResults[docIndex + 1], this.searchResults[docIndex]] =
          [this.searchResults[docIndex], this.searchResults[docIndex + 1]];
      }
    }
  },
},
};
</script>



<style>

*{
  font-family: 'Orbitron', sans-serif;
}
.page{
  font-size: 1em;
  color: white;
  height: 100vh;
  display: flex;
  flex-direction: column;

}

.main-section/*contenitor of nav, main and aside*/
{
  align-items: center;
  justify-content: center;
  display: flex;
  flex: 1;
}

.left, .right{
  text-align: center;
  padding-top: 6rem;
  padding-bottom: 2rem;
  flex: 1 1 0rem;
}

.center{
  flex: 3 3;
  text-align: center;
  width:100%;
}

body{
  background-image: url("assets/tattoo.jpg");
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  color: white;
}

.logo{
  width: 200px;
}

@import url('https://fonts.googleapis.com/css?family=Orbitron&display=swap');
@import url('https://fonts.googleapis.com/css?family=Hind&display=swap');

* {
  -webkit-font-smoothing: antialiased;
  color: #acbdce;
}

:root {
  --border-radius: 10px;
}



.Card {
  padding: 1px;
  border-radius: var(--border-radius);
  background: linear-gradient(-67deg, rgba(#c8d8e7, .7), rgba(255,255,255,.8));
  overflow: hidden;
  box-shadow: 
    -2px -2px 6px rgba(#fff, .6),
    2px 2px 12px #c8d8e7;
  width: 100%;
}

.CardInner {
  padding: 16px 16px;
  background-color: #e2e9f4;
  border-radius: var(--border-radius);
}

.container {
  display: flex;
}

.Icon {
  min-width: 46px;
  min-height: 46px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--border-radius);
  margin-right: 12px;
  box-shadow: 
    -2px -2px 6px rgba(#fff, .6),
    2px 2px 12px #c8d8e7;
    
  svg {
    transform: translate(-1px, -1px);    
  }
}

label {
  font-family: "Hind", sans-serif;
  display: block;
  color: black;
  margin-bottom: 12px;
  background: linear-gradient(45deg, rgba(#6b7b8f, 1), #3c4b66);
  -webkit-background-clip: text;

}

.InputContainer {
  width: 100%;
}

input {
  background-color: #e3edf7;
  padding: 16px 32px;
  border: none;
  display: block;
  font-family: 'Orbitron', sans-serif;
  font-weight: 600;
  color: black;
  -webkit-appearance: none;
  transition: all 240ms ease-out;
  width: 100%;
  
  &::placeholder {
    color: #6d7f8f;
  }
  
  &:focus {
    outline: none;
    color: #6d7f8f;
    background-color: lighten(#e3edf7, 3%);
  }
};
  
.InputContainer {
  --top-shadow: inset 1px 1px 3px #c5d4e3, inset 2px 2px 6px #c5d4e3;
  --bottom-shadow: inset -2px -2px 4px rgba(255,255,255, .7);
  
  position: relative;
  border-radius: var(--border-radius);
  overflow: hidden;
  
  &:before,
  &:after {
    left: 0;
    top: 0;
    display: block;
    content: "";
    pointer-events: none;
    width: 100%;
    height: 100%;
    position: absolute;
  }
  
  &:before {
    box-shadow: var(--bottom-shadow);
  }
  
  &:after {
    box-shadow: var(--top-shadow);
  }
}

.result-container{
  text-align: left;
  margin: 1rem;
  background-color:  #e2e9f4;
  padding: 20px;
  border-radius: 10px;
  color: black;
  display: flex;
  width: 91%;

}

.result-container:hover{
  scale:0.97;
  transition: 2s;
  background-color: #FCFFC4;
}

.result-container a{
  color: black;
  text-decoration: none;
}

.result-container a:hover{
  color: #52F668;
  text-decoration: underline;
}

.container-res{
  width: 100%;
  font-size: 18px;
  margin-top: 50px;
  margin-bottom: 50px;
  align-items: center;
  justify-content: center;
  display: inline-block;
}

.result-text{
  font-size: 18px;
  color: #626262;
}

.InputContainer button{
  background-color: #52F668;
  border-radius: 8px;
  border-style: none;
  box-sizing: border-box;
  color: black;
  cursor: pointer;
  display: inline-block;
  font-family: "Haas Grot Text R Web", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 14px;
  font-weight: 500;
  height: 40px;
  line-height: 20px;
  list-style: none;
  margin: 0;
  outline: none;
  padding: 10px 16px;
  position: relative;
  text-align: center;
  text-decoration: none;
  transition: color 100ms;
  vertical-align: baseline;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.InputContainer button:hover,
.InputContainer button:focus {
  background-color: #96FAA4;
}

.btn {
  margin-top: 20px;
}

.feedback button img{
  width: 24px;
}

.text{
  width: 88%;
  float: left;
}

.feedback{
  width: 12%;
  text-align: right;
}

.feedback button{
  margin-left: 10px;
  margin-right: 10px;
  padding: 0;
  border: none;
  background: none;
  border-radius: 50px;
}

.feedback button:nth-child(2):hover{
  scale: 1.03;
  background-color: #FF8491;
}

.feedback button:nth-child(1):hover{
  scale: 1.03;
  background-color: #52F668;
}

</style>

