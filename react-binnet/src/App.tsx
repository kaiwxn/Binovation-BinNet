import { useEffect, useState } from 'react'
import './App.css'
import axios from 'axios';

function App() {
    const [data, setData] = useState<Apple[]>([])

    interface Apple {
        name: string;
        color: string;
        photo_url: string;
    }

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
      <div style={{ textAlign: 'left' }}>
      {data ? <pre>{JSON.stringify(data, null, 2)}</pre> : 'Loading...'}
      </div>
    );
}

export default App