import React from "react";

class DragItem extends React.Component {
  drag = (e) => {
    e.dataTransfer.setData("text/plain", e.target.id);
  };

  noAllowDrop = (e) => {
    e.stopPropagation();
  };

  render() {
    return (
      <img
        id={this.props.id}
        draggable='true'
        onDragStart={this.drag}
        onDragOver={this.noAllowDrop}
        alt='placeholder'
        src='https://via.placeholder.com/50'
      ></img>
    );
  }
}

export default DragItem;
