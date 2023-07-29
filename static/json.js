const jsonFnc = async (ev) => {
    
    const response = await fetch("jjjson", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"abc": 123})
    })
    
    const j = await response.json();
    
    const ret = document.getElementById("result");
    ret.innerHTML = JSON.stringify(j);

}

const jb = document.getElementById("jsontest");

jb.addEventListener('click', jsonFnc);
