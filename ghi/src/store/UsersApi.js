import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const usersApi = createApi({
    reducerPath: 'users',
    baseQuery: fetchBaseQuery({
        //baseUrl: process.env.MONO_HOST
        baseUrl: "http://localhost:8080/"
    }),
    tagTypes: ['Dashboard', 'User', 'Token', 'User', 'Token'],
    endpoints: builder => ({
        createUsers: builder.mutation({
            query: data => ({
                url: 'api/users',
                body: data,
                method: 'POST',
                credentials: 'include'
            }),
            invalidatesTags: ['User'],
        }),
        getUsers: builder.query({
            query: () => 'api/users',
            providesTags: ['User'],
        }),
        createToken: builder.mutation({
            query: data => 
            {
            console.log("Data:"
            , data.values)
            return {
                url: '/token',
                body: data,
                method: 'POST',
                credentials: 'include',
            }
            
            },
            invalidatesTags: ['Token'],
        }),
        getToken: builder.query({
            query: () => ({
                url: '/token',
                credentials: 'include',
            }),
            providesTags: ['Token'],
        }),
        logIn: builder.mutation({
            query: info => {
              let formData = null;
              if (info instanceof HTMLElement) {
                formData = new FormData(info);
              } else {
                formData = new FormData();
                formData.append('username', info.email);
                formData.append('password', info.password);
              }
              return {
                url: '/token',
                method: 'post',
                body: formData,
                credentials: 'include',
              };
            },
            providesTags: ['User'],
            invalidatesTags: result => {
              return (result && ['Token']) || [];
            },
            // async onQueryStarted(arg, { dispatch, queryFulfilled }) {
            //   try {
            //     await queryFulfilled;
            //     dispatch(clearForm());
            //   } catch (err) {}
            // },
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
    useLogInMutation,
    useGetTokenQuery, } = usersApi;