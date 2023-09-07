import { 
  SET_BIO, 
  SET_USER_TITLE,
  SET_FOLLOWING,
  SET_FOLLOWING_STATUS,
  SET_PROFILE_PICTURE, 
  SET_BACKGROUND_PICTURE,
} from './actions';

const initialState = {
  bio: '',
  userTitle: '',
  following: 0,
  followingStatus: false,
  profilePicture: null,
  backgroundPicture: null,
};

const profileReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_BIO:
      return {
        ...state,
        bio: action.payload,
      };
    case SET_USER_TITLE:
      return {
        ...state,
        userTitle: action.payload,
      };
    case SET_FOLLOWING:
      return {
        ...state,
        following: action.payload,
      };
    case SET_FOLLOWING_STATUS:
      return {
        ...state,
        followingStatus: !state.followingStatus,
      };
    case SET_PROFILE_PICTURE:
      return {
        ...state,
        profilePicture: action.payload,
      };
    case SET_BACKGROUND_PICTURE:
      return {
        ...state,
        backgroundPicture: action.payload,
      };
    default:
      return state;
  }
};

export default profileReducer;