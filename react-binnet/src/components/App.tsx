import { useEffect, useState } from 'react'
import './App.css'
import axios from 'axios';

function App() {
    const [data, setData] = useState(0)

    useEffect(() => {
        axios.get('http://localhost:8000/binnetapp/')
        .then((res) => {
            setData(res.data)
        })
        .catch((err) => {
            console.log(err)
        })
    }, [])

    return (
      <div>
      {data ? <pre>{JSON.stringify(data, null, 2)}</pre> : 'Loading...'}
      <h1 className="text-3xl font-bold underline p-10"> Lorem ipsum dolor sit amet, consectetur adipisicing elit. A, veniam?</h1>
      <button className="btn btn-outline btn-secondary">Secondary</button>
      <input type="checkbox" aria-label="Checkbox" className="btn" />
      </div>
    );
}

export default App