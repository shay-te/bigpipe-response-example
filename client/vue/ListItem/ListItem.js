var ListItem = Vue.component('ListItem', {
    props: [],
    data: function () {
        return {
            title: ''
        }
    },
    addNewItem: function() {
        if(this.newItem.trim().length > 0) {
            this.items.push(this.newItem);
            this.newItem = "";
        }
    },
    template:  `
        <div class="list-item">
            {{ title }}
        </div>
    `
})

export default ListItem;