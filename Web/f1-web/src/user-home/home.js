import { useEffect, useState } from "react";
import { Container, Col, Row, ListGroup } from "react-bootstrap";
import { endpoints } from "../api";


const HomePage = () => {
  const [tableData, setTableData] = useState({});

  const getLoginSummary = async () => {
    const summary = await endpoints.user.getLoginSummary();
    console.log(summary);
    setTableData(summary);
  };
  useEffect(() => {
    getLoginSummary();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const TableData = () => {
    return (
      <Container>
        <Row>
          <Col>
            <h2>Teams</h2>
            <TeamsList teams={tableData["teams"]} />
          </Col>
          <Col>
            <h2>Drivers</h2>
            <DriversList drivers={tableData["drivers"]} />
          </Col>
        </Row>
        <Row>
          <Col>
            <h2>Leagues</h2>
            <LeaguesList leagues={tableData["leagues"]} />
          </Col>
        </Row>
      </Container>
    );
  };

  const TeamsList = ({ teams }) => {
    const sortedTeams = teams
      ? [...teams].sort((a, b) => b.points - a.points)
      : [];

    return (
      <ListGroup>
        {sortedTeams.length > 0 ? (
          sortedTeams.map((team) => (
            <ListGroup.Item key={team.id}>
              {team.name} - {team.points}
            </ListGroup.Item>
          ))
        ) : (
          <ListGroup.Item>No teams available</ListGroup.Item>
        )}
      </ListGroup>
    );
  };

  const DriversList = ({ drivers }) => {
    const sortedDrivers = drivers
      ? [...drivers].sort((a, b) => b.points - a.points)
      : [];

    return (
      <ListGroup>
        {sortedDrivers.length > 0 ? (
          sortedDrivers.map((driver) => (
            <ListGroup.Item key={driver.id}>
              {driver.name} - {driver.points}
            </ListGroup.Item>
          ))
        ) : (
          <ListGroup.Item>No drivers available</ListGroup.Item>
        )}
      </ListGroup>
    );
  };

  const LeaguesList = ({ leagues }) => (
    <ListGroup>
      {leagues ? (
        leagues.map((league) => (
          <ListGroup.Item key={league.id}>{league.name}</ListGroup.Item>
        ))
      ) : (
        <ListGroup.Item>No leagues available</ListGroup.Item>
      )}
    </ListGroup>
  );

  return (
    <div>
      
      
      <TableData />
    </div>
  );
};

export { HomePage };
