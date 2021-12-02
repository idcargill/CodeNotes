import React from "react";
import PropTypes from "prop-types";

class Draggable extends React.Component {
  drag = (e) => {
    e.dataTransfer.setData("text/plain", e.target.id);
    console.log(e.target.id);
    // console.log("Draggable: ", this);
  };

  noAllowDrop = (e) => {
    e.stopPropagation();
  };

  render() {
    return (
      <div
        id={this.props.id}
        draggable='true'
        onDragStart={this.drag}
        onDragOver={this.noAllowDrop}
        style={this.props.style}
      >
        {this.props.children}
      </div>
    );
  }
}

export default Draggable;
