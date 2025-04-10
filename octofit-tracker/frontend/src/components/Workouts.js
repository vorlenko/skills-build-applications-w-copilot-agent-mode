import { Table } from 'react-bootstrap';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://special-telegram-5rwggpx5vjfp69x-3000.app.github.dev/api/workouts')
      .then(response => response.json())
      .then(data => setWorkouts(data));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Workouts</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Name</th>
            <th>Duration (mins)</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map(workout => (
            <tr key={workout.id}>
              <td>{workout.name}</td>
              <td>{workout.duration}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default Workouts;
