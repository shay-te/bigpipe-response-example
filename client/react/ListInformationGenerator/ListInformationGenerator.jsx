import Image from '../Base/Image/Image.jsx';
import ListingInformationGrid from '../ListingInformationGrid/ListingInformationGrid.jsx';
import ComponentPost from '../ComponentPost/ComponentPost.jsx';
import InformationBox from '../InformationBox/InformationBox.jsx';

var ListInformationGenerator = createReactClass({

    getDefaultProps: function() {
        return {renderComponents: []};
    },

	render: function () {
        var content = [];
        for(var i=0 ; i < this.props.renderComponents.length ; i++) {
            var renderComponent = this.props.renderComponents[i];
            var context = renderComponent.context;
            context.key = i;
            if(renderComponent.component == "ListingInformationGrid") {
                var children = [];
                for(var imageIndex=0 ; imageIndex < context.images.length ; imageIndex++) {
                    children.push(<Image backgroundSize='cover' url={context.images[imageIndex]} />);
                }
                var element = React.createElement(InformationBox, {title : context.title}, [
                    React.createElement(ListingInformationGrid, context, children)
                ])
                content.push(element);
            } else if(renderComponent.component == "ComponentPost") {
                content.push(React.createElement(ComponentPost, context, []));
            }
        }
		return (
		    <div className='list-info-generator'>
                {content}
		    </div>
		);
	}
});

export default ListInformationGenerator;