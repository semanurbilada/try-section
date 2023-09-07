import { configureStore } from '@reduxjs/toolkit';
import profileReducer from './profile/reducer';

const store = configureStore({
    reducer: {
        profile: profileReducer,
    },
});

export default store;