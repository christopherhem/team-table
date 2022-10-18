import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const usersApi = createApi({
    reducerPath: 'users',
    baseQuery: fetchBaseQuery({
        //baseUrl: process.env.MONO_HOST
        baseUrl: "http://localhost:8080/"
    }),
    tagTypes: ['User', 'Token'],
    endpoints: builder => ({
        createUsers: builder.mutation({
            query: data => {
                console.log(data)
                return {
                url: 'api/users',
                body: data,
                method: 'POST',
                credentials: 'include'
            }
            },
            invalidatesTags: ['User'],
        }),
        getUsers: builder.query({
            query: () => 'api/users',
            providesTags: ['User'],
        }),
        createToken: builder.mutation({
            query: data => ({
                url: '/token',
                body: data,
                method: 'POST',
                credentials: 'include',
            }),
            invalidatesTags: ['Token'],
        }),
        getToken: builder.query({
            query: () => ({
                url: '/token',
                credentials: 'include',
            }),
            providesTags: ['Token'],
        }),
        signOut: builder.mutation({
            query: () => ({
                url: '/token',
                method: 'delete',
                credentials: 'include',
            }),
            invalidatesTags: ['Token'],
        })
    }),
});
export const {
    useGetUsersQuery,
    useCreateUsersMutation,
    useCreateTokenMutation, 
    useSignOutMutation,
    useGetTokenQuery, } = usersApi;