
var LandingPage = createReactClass({
	render: function () {
		return (
			<html>
				<head>
                    <script type="text/javascript" src="public/bigpipe.js"></script>
                    <script type="text/javascript" src="jsi18n"></script>
                    <script type="text/javascript" src="public/lib/react.js"></script>
                    <script type="text/javascript" src="public/lib/react-dom.js"></script>
                    <script type="text/javascript" src="public/lib/create-react-class.js"></script>
				</head>
				<body>
                    <div className='landing-page'>
                        I am landing page
                        <div id='pagelet_1'></div>
                    </div>
				</body>
			</html>
		);
	}
});

export default LandingPage;
