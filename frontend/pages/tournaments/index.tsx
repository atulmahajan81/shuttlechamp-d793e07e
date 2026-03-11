import React from 'react';
import { useQuery } from 'react-query';
import axios from 'axios';
import Layout from '../../components/Layout';
import TournamentCard from '../../components/TournamentCard';

const fetchTournaments = async () => {
  const { data } = await axios.get('/api/v1/tournaments');
  return data.tournaments;
};

const TournamentsPage: React.FC = () => {
  const { data, isLoading, isError } = useQuery('tournaments', fetchTournaments);

  if (isLoading) return <p>Loading...</p>;
  if (isError) return <p>Error loading tournaments</p>;

  return (
    <Layout>
      <div className="p-6">
        <h1 className="text-2xl font-bold mb-4">Tournaments</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {data && data.length > 0 ? data.map((tournament: any) => (
            <TournamentCard key={tournament.id} tournament={tournament} />
          )) : <p>No tournaments available</p>}
        </div>
      </div>
    </Layout>
  );
};

export default TournamentsPage;