import { motion } from "framer-motion";

export default function Hero() {
  return (
    <header className="flex flex-col items-center text-center py-20 px-10">
      <motion.h1 
        initial={{ opacity: 0, y: -50 }} 
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="text-5xl font-extrabold"
      >
        The Best Way to Manage Your Club Events
      </motion.h1>
      <p className="mt-4 text-lg max-w-2xl">
        Effortlessly manage registrations, organize teams, and streamline event coordination with our all-in-one platform.
      </p>
      <motion.button 
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
        className="mt-6 px-8 py-3 bg-blue-500 text-white text-lg rounded hover:bg-blue-600 transition"
      >
        Get Started
      </motion.button>
    </header>
  );
}
