import { Table } from 'react-bootstrap';

const Activities = () => {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://special-telegram-5rwggpx5vjfp69x-3000.app.github.dev/api/activities')
      .then(response => response.json())
      .then(data => setActivities(data));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Activities</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Activity Type</th>
            <th>Duration (mins)</th>
          </tr>
        </thead>
        <tbody>
          {activities.map(activity => (
            <tr key={activity.id}>
              <td>{activity.activity_type}</td>
              <td>{activity.duration}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default Activities;
