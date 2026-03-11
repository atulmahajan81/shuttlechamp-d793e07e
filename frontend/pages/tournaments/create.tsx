import React from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';
import { useRouter } from 'next/router';
import Layout from '../../components/Layout';

interface CreateTournamentForm {
  name: string;
  location: string;
  start_date: string;
  end_date: string;
}

const CreateTournamentPage: React.FC = () => {
  const { register, handleSubmit, formState: { errors } } = useForm<CreateTournamentForm>();
  const router = useRouter();

  const onSubmit = async (data: CreateTournamentForm) => {
    try {
      await axios.post('/api/v1/tournaments', data);
      router.push('/tournaments');
    } catch (error) {
      console.error('Failed to create tournament:', error);
    }
  };

  return (
    <Layout>
      <div className="p-6 max-w-md mx-auto">
        <h1 className="text-2xl font-bold mb-4">Create Tournament</h1>
        <form onSubmit={handleSubmit(onSubmit)}>
          <div className="mb-4">
            <label className="block">Name</label>
            <input
              type="text"
              {...register('name', { required: 'Name is required' })}
              className="w-full px-3 py-2 border rounded"
            />
            {errors.name && <p className="text-red-500 text-sm">{errors.name.message}</p>}
          </div>
          <div className="mb-4">
            <label className="block">Location</label>
            <input
              type="text"
              {...register('location', { required: 'Location is required' })}
              className="w-full px-3 py-2 border rounded"
            />
            {errors.location && <p className="text-red-500 text-sm">{errors.location.message}</p>}
          </div>
          <div className="mb-4">
            <label className="block">Start Date</label>
            <input
              type="date"
              {...register('start_date', { required: 'Start date is required' })}
              className="w-full px-3 py-2 border rounded"
            />
            {errors.start_date && <p className="text-red-500 text-sm">{errors.start_date.message}</p>}
          </div>
          <div className="mb-4">
            <label className="block">End Date</label>
            <input
              type="date"
              {...register('end_date', { required: 'End date is required' })}
              className="w-full px-3 py-2 border rounded"
            />
            {errors.end_date && <p className="text-red-500 text-sm">{errors.end_date.message}</p>}
          </div>
          <button type="submit" className="bg-primary-color text-white px-4 py-2 rounded mt-2">Create</button>
        </form>
      </div>
    </Layout>
  );
};

export default CreateTournamentPage;