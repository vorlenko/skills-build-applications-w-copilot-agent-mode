import { Table } from 'react-bootstrap';

const Teams = () => {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://special-telegram-5rwggpx5vjfp69x-8000.app.github.dev/api/teams/')
      .then(response => response.json())
      .then(data => setTeams(data));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Teams</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Team Name</th>
          </tr>
        </thead>
        <tbody>
          {teams.map(team => (
            <tr key={team.id}>
              <td>{team.name}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default Teams;
