import Icon from '../Base/Icon/Icon.jsx';


var NavigationMenuItem = createReactClass({
	getDefaultProps: function() {
		return {
			icon: '',
			label: ''
		};
	},
	render: function () {
		return (
		    <div className='navigation-menu-item tbl-flds t-f-vmiddle'>
                <div className='nav-menu-item-icon'>
                    <Icon icon={this.props.icon} size={18}/>
                </div>
                <div className='nav-menu-item-text ellipsis'>{this.props.label}</div>
		    </div>
		);
	}
});

export default NavigationMenuItem;