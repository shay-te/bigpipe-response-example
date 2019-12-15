import Image from '../Base/Image/Image.jsx';

var ComponentPost = createReactClass({
	getDefaultProps: function() {
		return {
			title: '',
			content: '',
			image: undefined
		};
	},
	render: function () {
	    var image;
	    if(this.props.image) {
	        image = <Image url={this.props.image} height='300px' backgroundSize='cover'/>
	    }
		return (
		    <div className='component-post white-box shadow'>
		        <div className='comp-post-title ellipsis'>{gettext(this.props.title)}</div>
		        <div className='comp-post-content'>
		            <div>{this.props.content}</div>
		        </div>
                <div>{image}</div>
		    </div>
		);
	}
});

export default ComponentPost;