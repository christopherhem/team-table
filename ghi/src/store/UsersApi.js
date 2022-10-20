import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const usersApi = createApi({
    reducerPath: 'users',
    baseQuery: fetchBaseQuery({
        //baseUrl: process.env.MONO_HOST
        baseUrl: "http://localhost:8080/",
        prepareHeaders: (headers, { getState }) => {
            const selector = usersApi.endpoints.getToken.select();
            const { data: tokenData } = selector(getState());
            if (tokenData && tokenData.access_token) {
              headers.set('Authorization', `Bearer ${tokenData.access_token}`);
            }
            return headers;
          }

    }),
    tagTypes: ['Dashboard', 'User', 'Token', 'UserCoverEventsList', 'UserShiftSwapEventsList', 'CoverEvent', 'ShiftSwapEvent', 'UserTeams'],
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
            invalidatesTags: ['UserCoverEventsList']
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
        }),
        getUserCoverEvents: builder.query({
            query: () => ({
                url: '/api/table/user/cover_events/',
                credentials: 'include'
            }),
            providesTags: ['UserCoverEventsList'],
        }),
        getUserShiftSwapEvents: builder.query({
            query: () => ({
                url: '/api/table/user/shift_swap_events/',
                credentials: 'include'
            }),
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
            query: (data) => ({
                url: '/api/table/cover_events/',
                method: 'post',
                body: data,
                credentials: 'include'
            }),
            invalidatesTags: ['UserCoverEventsList']
        }),
        CreateShiftSwapEvent: builder.mutation({
            query: (data) => ({
                url: '/api/table/shift_swap_events/',
                method: 'post',
                body: data,
                credentials: 'include'
            }),
            invalidatesTags: ['UserShiftSwapEventsList']
        }),
        UpdateCoverEvent: builder.mutation({
            query: (id, data) => ({
                url: `/api/table/cover_events/${id}`,
                method: 'put',
                body: data,
                credentials: 'include'
            }),
            invalidatesTags: ['CoverEvent', 'UserCoverEventsList']
        }),
        UpdateShiftSwapEvent: builder.mutation({
            query: (id, data) => ({
                url: `/api/table/shift_swap_events/${id}`,
                method: 'put',
                body: data,
                credentials: 'include'
            }),
            invalidatesTags: ['ShiftSwapEvent', 'UserShiftSwapEventsList']
        }),
        DeleteCoverEvent: builder.mutation({
            query: (id) => ({
                url: `/api/table/cover_events/${id}`,
                method: 'delete',
                credentials: 'include'
            })
        }),
        DeleteShiftSwapEvent: builder.mutation({
            query: (id) => ({
                url: `/api/table/shift_swap_events/${id}`,
                method: 'delete',
                credentials: 'include'
            })
        }),
        GetUsersTeams: builder.query({
            query: () => ({
                url: '/api/main/teams/byuser/',
                credentials: 'include'
            }),
            providesTags: ['UserTeams']
        })
    }),
});
export const {
    useGetUsersTeamsQuery,
    useDeleteCoverEventMutation,
    useUpdateShiftSwapEventMutation,
    useUpdateCoverEventMutation,
    useCreateShiftSwapEventMutation,
    useCreateCoverEventMutation,
    useGetUserCoverEventsQuery,
    useGetCoverEventQuery,
    useGetUserShiftSwapEventsQuery,
    useGetShiftSwapEventQuery,
    useGetUsersQuery,
    useCreateUsersMutation,
    useCreateTokenMutation,
    useSignOutMutation,
    useLogInMutation,
    useGetTokenQuery, } = usersApi;
