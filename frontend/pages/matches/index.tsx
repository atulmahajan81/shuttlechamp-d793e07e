import React from 'react';
import { useQuery } from 'react-query';
import axios from 'axios';
import Layout from '../../components/Layout';

const fetchMatches = async () => {
  const { data } = await axios.get('/api/v1/matches');
  return data.matches;
};

const MatchesPage: React.FC = () => {
  const { data, isLoading, isError } = useQuery('matches', fetchMatches);

  if (isLoading) return <p>Loading...</p>;
  if (isError) return <p>Error loading matches</p>;

  return (
    <Layout>
      <div className="p-6">
        <h1 className="text-2xl font-bold mb-4">Matches</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {data && data.length > 0 ? data.map((match: any) => (
            <div key={match.id} className="p-4 bg-white rounded shadow-md">
              <h2 className="text-lg font-semibold">{match.title}</h2>
              <p>{match.schedule}</p>
            </div>
          )) : <p>No matches available</p>}
        </div>
      </div>
    </Layout>
  );
};

export default MatchesPage;