import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { FaGithub, FaSignInAlt, FaUsers, FaCalendarCheck, FaBell, FaRocket, FaCogs, FaChartLine } from "react-icons/fa";
import { SiClubhouse } from "react-icons/si";
import "../index.css";

export default function ClubLandingPage() {
  const [darkMode, setDarkMode] = useState(true);
  const [bgColor, setBgColor] = useState("bg-gray-900");

  useEffect(() => {
    const colorShift = setInterval(() => {
      setBgColor(prev => prev === "bg-gray-900" ? "bg-blue-900" : "bg-gray-900");
    }, 5000);
    return () => clearInterval(colorShift);
  }, []);

  return (
    <div className={`min-h-screen transition-all duration-300 relative ${bgColor} ${darkMode ? "text-white" : "text-gray-900"}`}>
      {/* Glowing Light Background */}
      <div className="glowing-light"></div>

      {/* Navbar */}
      <nav className={`flex justify-between items-center px-10 py-4 shadow-md transition-all duration-300 ${darkMode ? "bg-gray-800" : "bg-gray-100"}`}>
        <div className="flex items-center space-x-3">
          <SiClubhouse size={30} />
          <h1 className="text-2xl font-bold">Club Event Manager</h1>
        </div>
        <div className="flex items-center space-x-6">
          <button onClick={() => setDarkMode(!darkMode)} className="px-4 py-2 rounded bg-blue-500 text-white hover:bg-blue-600 transition">
            {darkMode ? "Light Mode" : "Dark Mode"}
          </button>
          <a href="#login" className="px-4 py-2 rounded bg-green-500 text-white hover:bg-green-600 transition flex items-center space-x-2">
            <FaSignInAlt /> <span>Login</span>
          </a>
        </div>
      </nav>
      
      {/* Hero Section */}
      <header className="hero-section text-center py-32">
        <motion.h1 
          initial={{ opacity: 0, y: -50 }} 
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="text-6xl font-extrabold"
        >
          The Future of Club Event Management
        </motion.h1>
        <p className="mt-4 text-lg max-w-2xl mx-auto">
          Organize and manage your club events efficiently with automation, AI insights, and real-time collaboration.
        </p>
        <motion.button 
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
          className="mt-6 px-8 py-3 bg-blue-500 text-white text-lg rounded hover:bg-blue-600 transition"
        >
          Get Started
        </motion.button>
      </header>

      {/* Animated Features Section */}
      <section className="grid grid-cols-1 md:grid-cols-3 gap-10 px-10 py-20 text-center">
        {[
          { icon: <FaUsers size={50} />, title: "Seamless User Management", desc: "Add, update, and monitor members with ease." },
          { icon: <FaCalendarCheck size={50} />, title: "Automated Event Scheduling", desc: "Keep track of event dates, reminders, and deadlines." },
          { icon: <FaBell size={50} />, title: "Smart Notifications", desc: "Stay updated with real-time alerts and emails." },
          { icon: <FaRocket size={50} />, title: "AI Insights", desc: "Predict event success with AI-powered analytics." },
          { icon: <FaCogs size={50} />, title: "Customizable Workflows", desc: "Design workflows tailored to your club’s needs." },
          { icon: <FaChartLine size={50} />, title: "Performance Metrics", desc: "Analyze participation trends and engagement levels." },
        ].map((feature, index) => (
          <motion.div key={index} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8, delay: index * 0.2 }} className="p-6 rounded-lg shadow-lg transition-all duration-300 hover:shadow-2xl hover:scale-105 cursor-pointer">
            <div className="mx-auto mb-4">{feature.icon}</div>
            <h2 className="text-xl font-semibold">{feature.title}</h2>
            <p className="text-sm">{feature.desc}</p>
          </motion.div>
        ))}
      </section>
      
      {/* Scrolling Section */}
      <section className="scrolling-section py-10">
        <motion.div className="scrolling-content flex space-x-10 px-10" animate={{ x: ["0%", "-100%"] }} transition={{ repeat: Infinity, duration: 20, ease: "linear" }} whileHover={{ animationPlayState: "paused" }}>
          <div className="scroll-item flex-shrink-0 bg-gray-200 dark:bg-gray-700 p-6 rounded-lg shadow-lg">🚀 Club Growth Tips</div>
          <div className="scroll-item flex-shrink-0 bg-gray-200 dark:bg-gray-700 p-6 rounded-lg shadow-lg">📢 Upcoming Events</div>
          <div className="scroll-item flex-shrink-0 bg-gray-200 dark:bg-gray-700 p-6 rounded-lg shadow-lg">💡 Member Insights</div>
        </motion.div>
      </section>

      {/* Footer */}
      <footer className={`text-center py-5 border-t transition-all duration-300 ${darkMode ? "bg-gray-800" : "bg-gray-100"}`}>
        <p>© 2025 Club Event Manager | All Rights Reserved</p>
        <div className="mt-3 flex justify-center space-x-4">
          <a href="#" className="hover:text-blue-500 transition"><FaGithub size={24} /></a>
        </div>
      </footer>
    </div>
  );
}