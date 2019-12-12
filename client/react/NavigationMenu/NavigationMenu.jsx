import NavigationMenuItem from '../NavigationMenuItem/NavigationMenuItem.jsx';


var NavigationMenu = createReactClass({
	getDefaultProps: function() {
		return {
		    title: '',
			menu_items: []
		};
	},
	render: function () {
	    var navigationItems = [];
	    for(var i = 0 ; i < this.props.menu_items.length ; i++) {
	        navigationItems.push( <NavigationMenuItem {...this.props.menu_items[i]} /> );
	    }
		return (
		    <div className='navigation-menu'>
		        <div>{this.props.title}</div>
		        {navigationItems}
		    </div>
		);
	}
});

export default NavigationMenu;