import NavigationMenu from '../NavigationMenu/NavigationMenu.jsx';

var NavigationMenuList = createReactClass({
	getDefaultProps: function() {
		return {
			menus: []
		};
	},
	render: function () {
	    var menu = [];
	    for(var i = 0 ; i < this.props.menus.length ; i++) {
	        menu.push( <NavigationMenu {...this.props.menus[i]} /> );
	    }
		return (
		    <div className='navigation-menu-list'>
		        {menu}
		    </div>
		);
	}
});

export default NavigationMenuList;