var Icon = createReactClass({
    getDefaultProps: function() {
        return {
            icon: "",
            size: undefined
        }
    },
    render: function() {
        var style = {};
        if(this.props.size) {
            style.fontSize = this.props.size;
        }
        return (<i style={style} className={"icon fa " + this.props.icon}></i>);
    }
});

export default Icon;