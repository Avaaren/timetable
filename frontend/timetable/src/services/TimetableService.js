import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class TimetableService{

    constructor(){}


    getTimetables() {
        const url = `${API_URL}/api/timetable/`;
        return axios.get(url).then(response => {console.log(response.data); return response.data});
    }
    getTimetablesByGroup(group_slug){
        const url = `${API_URL}/api/timetable/${group_slug}`;
        return axios.get(url).then(response => response.data);
    }
    getTimetable(id) {
        const url = `${API_URL}/api/timetable/${id}/edit/`;
        return axios.get(url).then(response => response.data);
    }
    deleteTimetable(id){
        console.log(id);
        const url = `${API_URL}/api/timetable/${id}/delete/`;
        return axios.delete(url);
    }
    createTimetable(timetable){
        const url = `${API_URL}/api/timetable/add/`;
        return axios.post(url,timetable);
    }
    updateTimetable(timetable){
        const url = `${API_URL}/api/timetable/${timetable.id}/edit/`;
        return axios.put(url,timetable);
    }
}