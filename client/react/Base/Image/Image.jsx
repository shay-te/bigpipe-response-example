var Image = createReactClass({

	getDefaultProps: function() {
		return {
			url: '',
			width: '100%',
			height: '100%',
			backgroundSize: 'auto',
			borderRadius: undefined
		};
	},

	render: function () {
		var style = {
			backgroundImage: "url(" + this.props.url + ")",
			width: this.props.width,
			height: this.props.height,
			backgroundSize: this.props.backgroundSize,
			backgroundRepeat: 'no-repeat',
			backgroundPosition: 'center'
		};

		if(this.props.borderRadius != undefined) {
			style.borderRadius = this.props.borderRadius;
		}

		return (<div className="image" style={style} onClick={this.props.onClick}></div>);
	}

});

export default Image;