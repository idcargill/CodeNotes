import React from "react";
import PropTypes from "prop-types";

export default class Droppable extends React.Component {
  drop = (e) => {
    e.preventDefault();
    console.log(e.target);
    const data = e.dataTransfer.getData("text/plain");
    console.log(data);
    e.target.appendChild(document.getElementById(data));
  };

  allowDrop = (e) => {
    e.preventDefault();
  };

  render() {
    return (
      <div id={this.props.id} onDrop={this.drop} onDragOver={this.allowDrop} style={this.props.style}>
        {this.props.children}
      </div>
    );
  }
}

Droppable.propTypes = {
  id: PropTypes.string,
  style: PropTypes.object,
  children: PropTypes.node,
};
