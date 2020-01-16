import ListItem from '../ListItem/ListItem.js';

var DynamicList = Vue.component('DynamicList', {
    props: [],
    data: function () {
        return {
            title: '',
            newItem: '',
            items: []
        }
    },
    addNewItem: function() {
        if(this.newItem.trim().length > 0) {
            this.items.push(this.newItem);
            this.newItem = "";
        }
    },
    template: `
        <div class="dynamic-list">
            <h3>{{ title }}</h3>
            <div>
                <input type="text" v-model="newItem">
                <input type="button" >
            </div>
            <ListItem
                v-for="item in items"
                v-bind:key="item"
                v-bind:title="item"
            ></ListItem>
        </div>
    `
});

export default DynamicList;
