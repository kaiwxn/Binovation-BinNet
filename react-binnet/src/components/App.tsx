import { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";
import Navbar from "./navbar";

function App() {
	const [data, setData] = useState(0);

	useEffect(() => {
		axios
			.get("http://localhost:8000/binnetapp/")
			.then((res) => {
				setData(res.data);
			})
			.catch((err) => {
				console.log(err);
			});
	}, []);

	return (
		<>
			<Navbar />
			{data ? (
				<pre className="text-black">{JSON.stringify(data, null, 2)}</pre>
			) : (
				"Loading..."
			)}
		</>
	);
}

export default App;
