export default function Login() {
    return (
      <section id="login" className="flex flex-col items-center py-20 px-10">
        <h2 className="text-3xl font-bold mb-6">Login to Your Account</h2>
        <div className="bg-gray-100 dark:bg-gray-800 p-6 rounded-lg shadow-lg w-full max-w-md">
          <input type="email" placeholder="Email" className="w-full p-3 mb-4 rounded border dark:bg-gray-700" />
          <input type="password" placeholder="Password" className="w-full p-3 mb-4 rounded border dark:bg-gray-700" />
          <button className="w-full py-3 bg-blue-500 text-white rounded hover:bg-blue-600 transition">Login</button>
          <p className="mt-4 text-center">Don't have an account? <a href="#signup" className="text-blue-500 hover:underline">Sign up</a></p>
        </div>
      </section>
    );
  }
  