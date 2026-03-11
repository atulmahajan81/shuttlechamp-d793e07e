import React from 'react';

interface TournamentCardProps {
  tournament: {
    id: string;
    name: string;
    location: string;
  };
}

const TournamentCard: React.FC<TournamentCardProps> = ({ tournament }) => {
  return (
    <div className="p-4 bg-white rounded shadow-md">
      <h2 className="text-lg font-semibold">{tournament.name}</h2>
      <p>{tournament.location}</p>
    </div>
  );
};

export default TournamentCard;