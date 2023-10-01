//import React from 'react';
//import ReactDOM from 'react-dom/client';

const {useState, useEffect} = React

const app = <><ModelStack/><h1>Hello</h1></>

function Model(props) {
    return <li><h3>{props.name}</h3></li>
}

function ModelStack() {
    const [data, setData] = useState(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)

    useEffect(() => {
        fetch(`${window.location.origin}/api/models`).then(
            (response) => {
                if(!response.ok){
                    throw new Error(response.status)
                }
                return response.json()
            }
        ).then(
            (actualData) => {
                console.log(actualData.models)
                setData(actualData.models)
                setError(null)
            }
        ).catch(
            (err) => {
                setError(err.message)
                setData(null)
            }
        ).finally(
            () => {
                setLoading(false)
            }
        )
    }, [])
    return (
        <div>
            <h1>Models</h1>
            { loading && <div>Un momento svp...</div> }
            { error && <div>{`Theres is a problem: ${error}`}</div> }
            <ul>
                {
                    data && data.map((model)=> <Model name={model}/>)
                }
            </ul>
        </div>
    )
}


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(app)