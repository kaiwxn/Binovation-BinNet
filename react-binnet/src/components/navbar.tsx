
function Navbar() {
	return (
		<div className="navbar bg-base-100 shadow-lg align-center">
			<div className="flex-1">
				<a className="btn btn-ghost text-3xl rounded-b p-5">BinNet</a>
			</div>
			<div className="flex-none">
				<a href="" className="bg-base-100 mr-2.5">
					HOME
				</a>
				<a
					href="/binnetapp/index"
					className="bg-base-100 mr-2.5"
				>
					OVERVIEW
				</a>
				<a
					href="/binnetapp/detail"
					className="bg-base-100 mr-2.5"
				>
					STATISTICS
				</a>
			</div>
		</div>
	);
}

export default Navbar;
