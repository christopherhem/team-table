import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const usersApi = createApi({
    reducerPath: 'users',
    baseQuery: fetchBaseQuery({
        //baseUrl: process.env.MONO_HOST
        baseURL: "http://localhost:8080"
    }),
    tagTypes: ['User', 'Token', 'UserCoverEventsList', 'UserShiftSwapEventsList', 'CoverEvent', 'ShiftSwapEvent'],
    endpoints: builder => ({
        createUsers: builder.mutation({
            query: data => ({
                url: 'api/users',
                body: data,
                method: 'POST',
                credentials: 'include',
            }),
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
        }),
        getUserCoverEvents: builder.query({
            query: () => '/api/table/user/cover_events/',
            providesTags: ['UserCoverEventsList'],
        }),
        getUserShiftSwapEvents: builder.query({
            query: () => '/api/table/user/shift_swap_events/',
            providesTags: ['UserShiftSwapEventsList'],
        }),
        getCoverEvent: builder.query({
            query: (id) => `/api/table/cover_events/${id}`,
            providesTags: ['CoverEvent']
        }),
        getShiftSwapEvent: builder.query({
            query: (id) => `/api/table/shift_swap_events/${id}`,
            providesTags: ['ShiftSwapEvent']
        }),
        CreateCoverEvent: builder.mutation({
            query: () => ({
                url: '/api/table/cover_events/',
                method: 'post',
                credentials: 'include'
            }),
            invalidatesTags: ['UserCoverEventsList']
        }),
        CreateShiftSwapEvent: builder.mutation({
            query: () => ({
                url: '/api/table/shift_swap_events/',
                method: 'post',
                credentials: 'include'
            }),
            invalidatesTags: ['UserShiftSwapEventsList']
        })
    }),
});
export const {
    useCreateCoverEventMutation,
    useGetUserCoverEventsQuery,
    useGetCoverEventQuery,
    useGetUserShiftSwapEventsQuery,
    useGetUsersQuery,
    useCreateUsersMutation,
    useCreateTokenMutation,
    useSignOutMutation,
    useGetTokenQuery, } = usersApi;
