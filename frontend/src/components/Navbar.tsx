import { SiClubhouse } from "react-icons/si";

interface NavbarProps {
  darkMode: boolean;
  toggleDarkMode: () => void;
}

export default function Navbar({ darkMode, toggleDarkMode }: NavbarProps) {
  return (
    <nav className={`flex justify-between items-center px-10 py-4 shadow-md transition-all duration-300 ${darkMode ? "bg-gray-800 text-white" : "bg-gray-100 text-gray-900"}`}>
      <div className="flex items-center space-x-3">
        <SiClubhouse size={30} />
        <h1 className="text-2xl font-bold">Club Event Manager</h1>
      </div>
      <div className="flex items-center space-x-6">
        <a href="#features" className="hover:underline">Features</a>
        <a href="#pricing" className="hover:underline">Pricing</a>
        <a href="#contact" className="hover:underline">Contact</a>
        <a href="#login" className="px-4 py-2 rounded bg-blue-500 text-white hover:bg-blue-600 transition">Login</a>
        <button onClick={toggleDarkMode} className="px-4 py-2 rounded bg-blue-500 text-white hover:bg-blue-600 transition">
          {darkMode ? "Light Mode" : "Dark Mode"}
        </button>
      </div>
    </nav>
  );
}
