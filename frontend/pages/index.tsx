import Layout from '../components/Layout';
import Head from 'next/head';

export default function Home() {
  return (
    <Layout>
      <Head>
        <title>ShuttleChamp Dashboard</title>
        <meta name="description" content="Manage your tournaments, matches, and players with ShuttleChamp." />
      </Head>
      <div className="p-6">
        <h1 className="text-2xl font-bold mb-4">Welcome to ShuttleChamp</h1>
        <p className="text-lg">Your one-stop platform for managing tournaments, players, and more.</p>
      </div>
    </Layout>
  );
}