import { application } from "express";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";


application() {
  render(){

    return (
      <>
      <Router>
        <Header />
        <Switch>
          <Route exact path='/'>
            <Main />
          </Route>
          <Route exact path='/aboutus'>
            <Aboutus />
          </Route>
        </Switch>
        <Footer />
      </Router>
      </>
    )
  }
}