function App() {
  async function handleOnClick() {
    // console.log("버튼되나?");
    const response = await fetch("http://127.0.0.1:8000");
    const data = await response.json();
    console.log(data);
  }
  return (
    <div>
      <h1>리액트 + Fast API 통신</h1>
      <button onClick={handleOnClick}>읽어오기</button>
    </div>
  );
}

export default App;
