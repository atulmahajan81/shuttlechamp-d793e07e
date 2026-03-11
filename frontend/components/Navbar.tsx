import React from 'react';
import Link from 'next/link';

const Navbar: React.FC = () => {
  return (
    <nav className="bg-primary-color text-white p-4">
      <div className="container mx-auto flex justify-between items-center">
        <Link href="/">
          <a className="text-xl font-bold">ShuttleChamp</a>
        </Link>
        <div className="space-x-4">
          <Link href="/tournaments">
            <a>Tournaments</a>
          </Link>
          <Link href="/matches">
            <a>Matches</a>
          </Link>
          <Link href="/auth/login">
            <a>Login</a>
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;