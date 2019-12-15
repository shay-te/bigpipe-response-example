var InformationBox = createReactClass({
	getDefaultProps: function() {
		return {
			title: ''
		};
	},

	render: function () {
		return (
		    <div className='information-box white-box shadow'>
		        <div className='info-post-title ellipsis'>{this.props.title}</div>
		        <div className='info-post-content'>{this.props.children}</div>
		    </div>
		);
	}
});

export default InformationBox;