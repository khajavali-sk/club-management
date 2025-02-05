import { motion } from "framer-motion";
import { FaUsers, FaCalendarCheck, FaBell } from "react-icons/fa";

export default function Features() {
  return (
    <section id="features" className="grid grid-cols-1 md:grid-cols-3 gap-10 px-10 py-20 text-center">
      {[
        { icon: <FaUsers size={50} />, title: "Quick Member Registration", desc: "Auto-fill student details for a seamless experience." },
        { icon: <FaCalendarCheck size={50} />, title: "Effortless Event Management", desc: "Easily track participants and event progress." },
        { icon: <FaBell size={50} />, title: "Smart Notifications", desc: "Get event reminders via email or in-app alerts." },
      ].map((feature, index) => (
        <motion.div 
          key={index} 
          initial={{ opacity: 0, y: 20 }} 
          animate={{ opacity: 1, y: 0 }} 
          transition={{ duration: 0.8, delay: index * 0.2 }}
          className="p-6 rounded-lg shadow-lg transition-all duration-300 hover:shadow-2xl hover:scale-105 cursor-pointer"
        >
          <div className="mx-auto mb-4">{feature.icon}</div>
          <h2 className="text-xl font-semibold">{feature.title}</h2>
          <p className="text-sm">{feature.desc}</p>
        </motion.div>
      ))}
    </section>
  );
}
