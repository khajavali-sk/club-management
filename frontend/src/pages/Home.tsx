// import { useState } from "react";
// import Navbar from "../components/Navbar";
// import Hero from "../components/Hero";
// import Login from "../components/Login";
// import Features from "../components/Features";
// import Footer from "../components/Footer";

// export default function Home() {
//   const [darkMode, setDarkMode] = useState(true);

//   return (
//     <div className={darkMode ? "bg-gray-900 text-white" : "bg-white text-gray-900"}>
//       <Navbar darkMode={darkMode} toggleDarkMode={() => setDarkMode(!darkMode)} />
//       <Hero />
//       <Login />
//       <Features />
//       <Footer darkMode={darkMode} />
//     </div>
//   );
// }

import ClubLandingPage from "../components/ClubLandingPage";

export default function Home() {
  return <ClubLandingPage />;
}

