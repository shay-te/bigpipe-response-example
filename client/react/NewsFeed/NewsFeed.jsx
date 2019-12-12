import ComponentPost from '../ComponentPost/ComponentPost.jsx';

var NewsFeed = createReactClass({
	getDefaultProps: function() {
		return {
			feed: []
		};
	},
	render: function () {
	    var newsFeed = []
	    for(var i = 0 ; i < this.props.feed.length ; i++) {
	        newsFeed.push( <ComponentPost {...this.props.feed[i]} /> );
	    }
		return (
		    <div className='news-feed'>{newsFeed}</div>
		);
	}
});

export default NewsFeed;