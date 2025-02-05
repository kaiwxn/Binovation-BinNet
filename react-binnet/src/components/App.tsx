import { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "./navbar";
import { BrowserRouter, Routes, Route } from "react-router-dom";

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
			{/* <BrowserRouter>
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/binnetapp/index" element={<Index />} />
					<Route path="/binnetapp/detail" element={<Detail />} />
				</Routes>
			</BrowserRouter> */}
		</>
	);
}

export default App;
