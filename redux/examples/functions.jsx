import { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { setAddSkill } from '../redux/profile/profileSlice';

// One of my functions that i worked but not used in the actual file so here we are:

export default function Functions() {
    const dispatch = useDispatch();
    const skills = useSelector(state => state.profile.skills);

    const [ newSkill, setNewSkill ] = useState(''); // get the current info
    const [ skillList, setSkillList ] = useState([]); // store the skills for preview

    // 1. With 'add' button, it adds the skill to the array;
    const handleAddSkill = () => {
        if (newSkill.trim() !== '') {
            setSkillList([...skillList, newSkill]); 
            setNewSkill(''); // clear the input
        }
    }; 

    // 2. With 'save' button, it saves the skill to the main area (profile);
    const handleSaveSkills = () => {
        if (skillList.length > 0) {
            dispatch(setAddSkill(skillList));
            setSkillList('');
        }
    };

    return(
        <div>{/* ..... */}</div>
    );
}