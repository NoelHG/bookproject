import React, { useState } from "react";
import axios from "axios";
import './App.css';

export default function App() {

    let [books, setBooks] = useState();
    let [count, setCount] = useState();
    let [author, setAuthor] = useState('');

    let search = () => {
        axios.get('/api/books/', {
            params: {
                count: count,
                author: author
                }
            }
        ).then((res) => setBooks(res.data)).catch((err) => console.log(err));
    }

    console.log(count);
    console.log(author);
    console.log(books);

    let onChange = (event, updateFunction) => {
        let inputValue = event.target.value;
        updateFunction(inputValue);
    };

    return <div className="App">
        <input value={author} type="text" placeholder="Author" onChange={(e) => onChange(e, setAuthor)} />
        <input value={count} type="number" placeholder="Count" onChange={(e) => onChange(e, setCount)} />
        <button onClick={(e) => search()}>Search</button>
        <div>
            {books && books.map ( (book) => <div key={book.title + book.author}>
                <span>{book.title}</span> - <span>{book.author}</span><br/>
            </div>) }
        </div>
    </div>
}
