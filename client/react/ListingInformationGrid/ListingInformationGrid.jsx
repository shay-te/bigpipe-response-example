var ListingInformationGrid = createReactClass({
    getInitialState: function() {
        return {width: 10};
    },

    componentDidMount() {
        this.setState({ width: this.refs.listInfoGrid.clientWidth });
    },

    render: function () {
        var boxSize = (this.state.width / 2) - 4;
        var style = {width: boxSize, height: boxSize, display: 'inline-block'};
        var newChildren = [];
        for(var i=0 ; i < this.props.children.length ; i++) {
            newChildren.push(<div key={i} style={style}>{this.props.children[i]}</div>);
        }

        return (
            <div className='list-info-grid' ref="listInfoGrid">
                {newChildren}
            </div>
        );
    }
});

export default ListingInformationGrid;