import { configureStore } from '@reduxjs/toolkit'
import { setupListeners } from '@reduxjs/toolkit/query'
import { usersApi } from './UsersApi'
import { teamsApi } from './TeamsApi';

export const store = configureStore({
    reducer: {
        [usersApi.reducerPath]: usersApi.reducer,
        [teamsApi.reducerPath]: teamsApi.reducer,
    },
    middleware: getDefaultMiddleware =>
        getDefaultMiddleware()
            .concat(usersApi.middleware, teamsApi.middleware)
});

setupListeners(store.dispatch)
