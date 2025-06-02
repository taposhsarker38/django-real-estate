import React, { useEffect } from "react";
import { Col, Container, Row } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { toast } from "react-toastify";
import { getProperties } from "../features/properties/propertySlice";
import Spinner from "../components/Spinner";
const PropertiesPage = () => {
	const { properties, isLoading, isError, message } = useSelector(
		(state) => state.properties
	);

	const dispatch = useDispatch();

	useEffect(() => {
		if (isError) {
			toast.error(message, { icon: "😭" });
		}
		dispatch(getProperties());
	}, [dispatch, isError, message]);

	if (isLoading) {
		return <Spinner />;
	}
  return (
    <>
      <Container>
          <Row>
              <Col className='mg-top'>
                  <h1>Properties</h1>
              </Col>
          </Row>
      </Container>
    </>
  )
}

export default PropertiesPage