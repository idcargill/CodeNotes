import React from "react";
import styled from "styled-components";
import Draggable from "../Draggable";
import Droppable from "../Droppable";

const Wrapper = styled.div`
  width: 100%;
  padding: 32px;
  display: flex;
  justify-content: center;
`;

const Item = styled.div`
  padding: 8px;
  color: #555;
  background-color: white;
  border-radius: 3px;
`;

const droppableStyle = {
  backgroundColor: "#555",
  width: "250px",
  height: "400px",
  margin: "32px",
};

export default class DaDtest extends React.Component {
  render() {
    return (
      <Wrapper>
        <Droppable id='dr1' style={droppableStyle}>
          <Draggable id='bean' style={{ margin: "8px" }}>
            <Item id='bean'>Bean</Item>
          </Draggable>
          <Draggable id='turnip' style={{ margin: "8px" }}>
            <Item>Turnip</Item>
          </Draggable>
        </Droppable>
        <Droppable id='dr2' style={droppableStyle}></Droppable>
      </Wrapper>
    );
  }
}
