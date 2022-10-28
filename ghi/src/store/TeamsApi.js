import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { usersApi } from './UsersApi';

export const teamsApi = createApi({
    reducerPath: 'teams',
    baseQuery: fetchBaseQuery({
        /*
        ideally if this application were scaled then this baseurl would be a
        variable that came from the monoservice list of user's team relations
        since this is not to scale it is simplified to the only teams microservice
        */
        baseUrl:"http://localhost:8100/",
        prepareHeaders:(headers,{getState})=>{
            const selector = usersApi.endpoints.getToken.select();
            const {data:tokenData}=selector(getState())
            if (tokenData && tokenData.access_token){
                headers.set('Authorization',`Bearer ${tokenData.access_token}`);
            }
            return headers;
        }
    }),
    tagTypes:['ValidCoverSwaps', 'Team','Token','Roles','Members','Permissions','TeamEvents','TeamTypes','EventTypes', 'ValidSwapList'],
    endpoints: builder=>({
        createTeam: builder.mutation({
            query: data => ({
                url: 'api/teams/',
                body: data,
                method: 'POST',
                credentials: 'include'
            }),
            invalidatesTags: ['Team'],
        }),
        updateTeam: builder.mutation({
            query: ({tid, ...data}) => ({
                url: `api/teams/${tid}`,
                body: data,
                method: 'PUT',
                credentials: 'include'
            }),
            invalidatesTags: ['Team'],
        }),
        deleteTeam: builder.mutation({
            query: tid => ({
                url: `api/teams/${tid}`,
                method: 'DELETE',
                credentials: 'include'
            }),
            invalidatesTags: ['Team'],
        }),
        getTeam: builder.query({
            query: tid => ({
                url: `api/teams/${tid}`,
                credentials: 'include'
            }),
            providesTags: ['Team'],
        }),
        getRoles: builder.query({
            query: (tid)=>({
               url: `api/teams/${tid}/roles`,
               credentials:'include'
            }),
            providesTags: ['Roles']
        }),
        createRole: builder.mutation({
            query: (data)=>({
                url: `api/teams/roles`,
                body: data,
                method: "POST",
                credentials: 'include'
            }),
            invalidatesTags:['Roles']
        }),
        updateRole: builder.mutation({
            query:({tid, rid, ...data})=>({
                url:`api/teams/${tid}/roles/${rid}`,
                body: data,
                method: 'PUT',
                credentials:'include'
            }),
            invalidatesTags: ['Roles']
        }),
        deleteRole: builder.mutation({
            query: (tid,rid)=>({
                url: `api/teams/${tid}/roles${rid}`,
                method: 'DELETE',
                credentials: 'include'
            }),
            invalidatesTags : ['Roles']
        }),
        getMembers : builder.query({
            query:(tid)=>({
                url: `api/teams/${tid}/members/`,
                credentials: 'include'
            }),
            providesTags: ['Members']
        }),
        createMember : builder.mutation({
            query: (data) =>({
                url: `api/teams/members/`,
                body: data,
                method: "POST",
                credentials: 'include'
            }),
            invalidatesTags: ['Members']
        }),
        updateMember : builder.mutation({
            query: ({tid,mid,...data})=>({
                url: `api/teams/${tid}/members/${mid}`,
                body: data,
                method: "PUT",
                credentials: 'include'
            }),
            invalidatesTags: ['Members']
        }),
        deleteMember : builder.mutation({
            query: (tid,mid)=>({
                url: `api/teams/${tid}/members/${mid}`,
                method: 'DELETE',
                credentials: 'include'
            }),
            invalidatesTags : ['Members']
        }),
        getEvents : builder.query({
            query:(tid)=>({
                url: `api/teams/${tid}/events/`,
                credentials: 'include'
            }),
            providesTags: ['TeamEvents']
        }),
        getEventTypes : builder.query({
            query:()=>({
                url: `api/teams/event_types/`,
                credentials: 'include'
            }),
            providesTags: ['EventTypes']
        }),
        getTypes : builder.query({
            query:()=>({
                url: `api/teams/types/`,
                credentials: 'include'
            }),
            providesTags: ['TeamTypes']
        }),
        createType : builder.mutation({
            query: (data)=>({
                url: `api/teams/types/`,
                body: data,
                method: "POST",
                credentials: 'include'
            }),
            invalidatesTags: ['TeamTypes']
        }),
        updateType : builder.mutation({
            query: ({id,...data})=>({
                url: `api/teams/types/${id}`,
                body: data,
                method: "PUT",
                credentials: 'include'
            }),
            invalidatesTags: ['TeamTypes']
        }),
        deleteType : builder.mutation({
            query: (id)=>({
                url: `api/teams/types/${id}`,
                method: 'DELETE',
                credentials: 'include'
            }),
            invalidatesTags : ['']
        }),
        getValidSwaps : builder.query({
            query:(id)=>({
                url:`/api/swapbyswap/${id}`,
                credentials: 'include'
            }),
            providesTags:['ValidSwapList']
        }),
        getValidCoverSwaps: builder.query({
            query:(id) =>({
                url: `/api/swapbycover/${id}`,
                credentials: 'include'
            }),
            providesTags: ['ValidCoverSwaps']
        })
    }),

});
export const {
    useGetValidCoverSwapsQuery,
    useGetValidSwapsQuery,
    useCreateMemberMutation,
    useCreateRoleMutation,
    useCreateTeamMutation,
    useCreateTypeMutation,
    useDeleteMemberMutation,
    useDeleteRoleMutation,
    useDeleteTeamMutation,
    useDeleteTypeMutation,
    useGetEventTypesQuery,
    useGetEventsQuery,
    useGetMembersQuery,
    useGetRolesQuery,
    useGetTeamQuery,
    useGetTypesQuery,
    useUpdateMemberMutation,
    useUpdateRoleMutation,
    useUpdateTeamMutation,
    useUpdateTypeMutation
} = teamsApi;
