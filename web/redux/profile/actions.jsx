export const SET_BIO = 'SET_BIO';
export const SET_PROFILE_PICTURE = 'SET_PROFILE_PICTURE';
export const SET_BACKGROUND_PICTURE = 'SET_BACKGROUND_PICTURE';

export const SET_USER_TITLE = 'SET_USER_TITLE';
export const SET_FOLLOWING = 'SET_FOLLOWING';
export const SET_FOLLOWING_STATUS = 'SET_FOLLOWING_STATUS';

export const setBio = (bio) => ({
  type: SET_BIO,
  payload: bio,
});

export const setUserTitle = (title) => ({ 
  type: SET_USER_TITLE,
  payload: title,
});

export const setProfilePicture = (url) => ({
  type: SET_PROFILE_PICTURE,
  payload: url,
});

export const setBackgroundPicture = (url) => ({
  type: SET_BACKGROUND_PICTURE,
  payload: url,
});

export const setFollowing = (count) => ({
  type: SET_FOLLOWING,
  payload: count,
});

export const setFollowingStatus = (count) => ({
  type: SET_FOLLOWING_STATUS,
  payload: count,
});