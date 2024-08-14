function Button({ onClick, children }) {
  return <button onClick={onClick}>{children}</button>;
}

function App() {
  const handleClick = (e) => {
    console.log("clicked", e?.target);
  };

  return (
    <div>
      <button onClick={(e) => handleClick(e)}>
        엘리먼트 버튼
      </button>
      <Button onClick={() => console.log("clicked element")}>
        컴포넌트 버튼
      </Button>
    </div>
  );
}

export default App;
