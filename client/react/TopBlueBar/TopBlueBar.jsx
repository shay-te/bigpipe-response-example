import Icon from '../Base/Icon/Icon.jsx';

var TopBlueBar = createReactClass({
	render: function () {
	    var iconSize = 20;
		return (
		    <div className='top-blue-bar'>
		        <div className='top-blue-bar-content tbl-flds t-f-vmiddle'>
                    <div style={{width: '28px'}}><Icon icon='fa-globe' size={28} /></div>
                    <div><input type='text' /></div>
                    <div>
                        <div className='top-blue-bar-icons'>
                            <div><Icon icon='fa-user-friends' size={iconSize} /></div>
                            <div><Icon icon='fa-bell' size={iconSize} /></div>
                            <div><Icon icon='fa-comment' size={iconSize} /></div>
                            <div><Icon icon='fa-question-circle' size={iconSize} /></div>
                        </div>
                    </div>
		        </div>
		    </div>
		);
	}
});

export default TopBlueBar;
