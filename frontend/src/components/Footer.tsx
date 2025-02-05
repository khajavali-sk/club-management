import { FaGithub } from "react-icons/fa";

export default function Footer({ darkMode }: { darkMode: boolean }) {
  return (
    <footer className={`text-center py-5 border-t transition-all duration-300 ${darkMode ? "bg-gray-800" : "bg-gray-100"}`}>
      <p>© 2025 Club Event Manager | All Rights Reserved</p>
      <div className="mt-3 flex justify-center space-x-4">
        <a href="#" className="hover:text-blue-500 transition"><FaGithub size={24} /></a>
      </div>
    </footer>
  );
}
