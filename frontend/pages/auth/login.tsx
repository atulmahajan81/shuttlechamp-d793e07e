import React from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';
import { useRouter } from 'next/router';

interface LoginFormInputs {
  email: string;
  password: string;
}

const Login: React.FC = () => {
  const { register, handleSubmit, formState: { errors } } = useForm<LoginFormInputs>();
  const router = useRouter();

  const onSubmit = async (data: LoginFormInputs) => {
    try {
      const response = await axios.post('/api/v1/auth/login', data);
      // Handle login success
      router.push('/');
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  return (
    <div className="flex justify-center items-center h-screen">
      <form onSubmit={handleSubmit(onSubmit)} className="bg-white p-6 rounded shadow-md w-80">
        <h2 className="text-xl mb-4">Login</h2>
        <div className="mb-4">
          <label className="block">Email</label>
          <input
            type="email"
            {...register('email', { required: 'Email is required' })}
            className="w-full px-3 py-2 border rounded"
          />
          {errors.email && <p className="text-red-500 text-sm">{errors.email.message}</p>}
        </div>
        <div className="mb-4">
          <label className="block">Password</label>
          <input
            type="password"
            {...register('password', { required: 'Password is required' })}
            className="w-full px-3 py-2 border rounded"
          />
          {errors.password && <p className="text-red-500 text-sm">{errors.password.message}</p>}
        </div>
        <button type="submit" className="bg-primary-color text-white px-4 py-2 rounded mt-2">Login</button>
      </form>
    </div>
  );
};

export default Login;