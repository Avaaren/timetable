import React, { Component } from 'react';

import TimetableService from '../services/TimetableService'

const timetableService = new TimetableService();


class TimetableList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            timetables: [],
        };
    }

    componentDidMount() {
        var self = this;
        timetableService.getTimetables().then(function (result) {
            self.setState({ timetables: result })
        });
    }

    render() {

        return (
            <div className="customers--list">
                <table className="table">
                    <thead key="thead">
                        <tr>
                            <th>#</th>
                            <th>Номер пары</th>
                            <th>Группа</th>
                            <th>День</th>
                            <th>Название</th>
                            <th>Кабинет</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.timetables.map(c =>
                            <tr key={c.pk}>
                                <td>{c.pk}  </td>
                                <td>{c.number_of_class}</td>
                                <td>{c.group}</td>
                                <td>{c.day}</td>
                                <td>{c.name_of_class}</td>
                                <td>{c.cabinet}</td>
                            </tr>)}
                    </tbody>
                </table>
            </div>
        );
    }
}
export default TimetableList